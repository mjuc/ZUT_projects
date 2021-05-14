#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

pthread_mutex_t lock;

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
    salt=(char *)malloc(sizeof(char));
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
}args;


void *decrypt_block(void *arg)
{
    args *ar = (args *)arg;
    int step=sizeof(char);
    char *temp;
    char *enc;
    int l;
    for(long i=ar->block_start;i<ar->block_end;i+=(l+1))
    {
        l = 0;
        while (ar->map[i+l] != '\n')
        {
            l++;
        }
        pthread_mutex_lock(&lock);
        temp=(char *)malloc(sizeof(char)*l);
        for(int j=0;j<l;j++)
        {
            temp[j]=ar->map[i+j];
        }
        enc=crypt(temp,ar->salt);
        if(strcmp(enc,ar->target)==0)
        {
            printf("Password found: %s\n",temp);
            break;
        }
        pthread_mutex_unlock(&lock);
    }
}

int main(int argc,char **argv)
{
    char *salt;
    char *passwd;
    char *filename;
    int threads;
    int c;
    int th;
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
            sscanf(optarg,"%d",&threads);
        default:
            break;
        }
    }
    salt=extract_salt(passwd);
    int max_thrds=sysconf(_SC_NPROCESSORS_ONLN);
    if(threads>max_thrds)
    {
        threads=max_thrds;
    }

    char *addr;
    int fd;
    struct stat sb;
    size_t length;
    ssize_t s;

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
}