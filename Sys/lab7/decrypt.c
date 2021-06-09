//PS IN1 320 LAB07
//Michał Jucewicz
//jm44353@zut.edu.pl
#define _GNU_SOURCE

#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <signal.h>
#include <crypt.h>

pthread_mutex_t lock;
int decrypt;

char *extract_salt(char *hash)
{
    char *salt;
    int i=0;
    int iter=0;
    while (i<3)
    {
        if(hash[iter]=='$')
        {
            i++;
        }
        iter++;
    }
    salt=(char *)malloc(sizeof(char)*iter);
    for(i=0;i<iter-1;i++)
    {
        salt[i]=hash[i];
    }
    return salt;
}

typedef struct args
{
    char *map;
    long block_start;
    long block_end;
    char *target;
    char *salt;
    int benchmark_flag; 
}args;

void *decrypt_block(void *arg)
{
    args *ar = (args *)arg;
    int step=sizeof(char);
    char *temp;
    struct crypt_data enc;
    int l;
    long i=ar->block_start;
    pthread_mutex_lock(&lock);
    decrypt=1;
    pthread_mutex_unlock(&lock);
    while (i<ar->block_end && decrypt==1)    
    {
        l = 0;
        while (ar->map[i+l] != '\n')
        {
            l++;
        }
        temp=(char *)malloc(sizeof(char)*l);
        for(int j=0;j<l;j++)
        {
            temp[j]=ar->map[i+j];
        }
        crypt_r(temp,ar->salt,&enc);
        if(strcmp(enc.output,ar->target)==0 && ar->benchmark_flag == 0)
        {
            printf("Password found: %s\n",temp);
            decrypt=0;
            free(temp);
            exit(0);
        }
        free(temp);
        if(decrypt==0)
        {
            pthread_exit(0);
        }
        i+=(l+1);
    }
}

int decryption(char *passwd,int threads,char *filename,int benchmark_flag)
{
    int th;
    char *addr;
    int fd;
    char *salt;
    struct stat sb;
    size_t length;
    ssize_t s;

    salt=extract_salt(passwd);
    fd = open(filename, O_RDONLY);
    if (fd == -1)
    {
        printf("File opening error\n");
    }
    if (fstat(fd, &sb) == -1)           
    {
        printf("Unable to get file size\n");
    }
    addr=mmap(NULL,sb.st_size,PROT_READ,MAP_PRIVATE,fd,0);
    close(fd);
    args * arguments = (args*)malloc(sizeof(args)*threads);
    long offset=0;
    long off_to_add = sb.st_size/threads;
    pthread_t *thrds = (pthread_t *)malloc(sizeof(pthread_t)*threads);
    for(int i=0;i<threads;i++)
    {
        arguments[i].map=addr;
        arguments[i].target=passwd;
        arguments[i].block_start=offset;
        arguments[i].salt=salt;
        arguments[i].block_end=off_to_add*(i+1);
        arguments[i].benchmark_flag=benchmark_flag;
        th=pthread_create(&thrds[i],NULL,decrypt_block,&arguments[i]);
        if(th)
        {
            printf("Thread creating error\n");
        }
        offset+=off_to_add;
    }
    for(int i=0;i<threads;i++)
    {
        pthread_join(thrds[i],NULL);
    }
    if(decrypt==1 && benchmark_flag ==0)
    {
        printf("Password not found in dictionary\n");
    }
    free(thrds);
    free(arguments);
}

int main(int argc,char **argv)
{
    char *passwd;
    char *filename;
    int threads;
    int c;
    int benchmark_flag=1;

    while ((c = getopt (argc, argv, "t:p:f:")) != -1)
    {
        switch (c)
        {
        case 'f':
            filename=optarg;
            break;
        case 'p':
            passwd=optarg;
            break;
        case 't':
            benchmark_flag=0;
            sscanf(optarg,"%d",&threads);
        default:
            break;
        }
    }
    int max_thrds=sysconf(_SC_NPROCESSORS_ONLN);
    if(max_thrds<threads && !benchmark_flag)
    {
        printf("Too many threads to create\n");
        exit(1);
    }    
    if(benchmark_flag)
    {
        printf("Benchmark\n");
        struct timespec *results;
        results=(struct timespec *)malloc(sizeof (struct timespec)*max_thrds);
        struct timespec start, end;
        for(int i=0;i<max_thrds;i++)
        {
            printf("\rTesting for %d out of %d available threads",i+1,max_thrds);
            fflush(stdout);
            clock_gettime(CLOCK_REALTIME,&start);
            decryption(passwd,i+1,filename,benchmark_flag);
            clock_gettime(CLOCK_REALTIME,&end);
            end.tv_sec=end.tv_sec-start.tv_sec;
            if(end.tv_nsec>start.tv_nsec)
            {
                end.tv_nsec=end.tv_nsec-start.tv_nsec;
            }
            else
            {
                end.tv_sec=end.tv_sec-1;
                end.tv_nsec=1000-(end.tv_nsec-start.tv_nsec);
            }
            results[i]=end;
        }
        printf("\nResults:\n");
        for(int i=0;i<max_thrds;i++)
        {
            printf("Threads: %d time: %ld.%ld s\n",i+1,results[i].tv_sec,results[i].tv_nsec);
        }
    }
    else
    {
        decryption(passwd,threads,filename,benchmark_flag);
    }
}