#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <signal.h>
#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <time.h>


int wait=1;
int create_new = 1;
int ended=0;

void handler(int no, siginfo_t *info, void *ucontext)
{
    time_t t;
    struct tm *tm;
    time(&t);
    tm=localtime(&t);
    ended++;    
    printf("Sender PID: %d\nEnded with: %d\nEnded at: %s\n",info->si_pid,info->si_status,asctime(tm));
    wait=0;
}
void interrupt_handler(int no, siginfo_t *info, void *ucontext)
{
    create_new=0;
}

int main(int argc,char **argv)
{
    int max_duration=1;
    int interval=1;
    int children=0;
    int stop=0;
    int random;
    int fd=-1;
    int c,d;
    time_t t;
    struct tm *tm;
    struct sigaction sig;
    siginfo_t siginf;

    while ((c = getopt (argc, argv, "i:d:")) != -1)
    {
        switch (c)
        {
        case 'd':
            sscanf(optarg,"%d",&max_duration);
            break;
        case 'i':
            sscanf(optarg,"%d",&interval);
            break;
        default:
            break;
        }
    }

    sig.sa_flags=SA_SIGINFO;
    sig.sa_sigaction = handler;
    sigaction(SIGCHLD,&sig,NULL);
    sig.sa_sigaction=interrupt_handler;
    sigaction(SIGINT,&sig,NULL);
    while (!stop)
    {
        if(create_new)
        {
            int pid = fork();
            children++;
            if(pid==0)
            {
                sig.sa_sigaction=interrupt_handler;
                sigaction(SIGINT,&sig,NULL);
                random = rand()% max_duration;
                int tmp=1;
                int cpid=getpid();
                time(&t);
                tm=localtime(&t);
                printf("Child PID: %d\nGenerated value: %d\nCreated at: %s\n",cpid,random,asctime(tm));
                while (alarm(max_duration)!=0)
                {
                    tmp+=tmp*tmp+1;
                }
                exit(random);
                
            }
            else
            {
                while (wait)
                {}
                wait=1;
            }
        }
        else
        {
            if(children==ended)
            {
                exit(0);
            }
        }
        sleep(interval);
    }
}
