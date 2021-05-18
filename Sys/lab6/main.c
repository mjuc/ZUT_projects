//PS IN1 320 LAB06
//Michał Jucewicz
//jm44353@zut.edu.pl
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include "timer.h"


struct args
{
    int duration;
};

int check_if_run(clock_t in,int n)
{
    clock_t check=clock();
    int ct = (int)(check - in) / CLOCKS_PER_SEC;
    if(ct<n)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void *function(void *threadarg)
{
    int i=1;
    clock_t c = clock();
    struct args *arg;
    start();
    arg=(struct args *) threadarg;
    while (check_if_run(c,arg->duration) != 0)
    {
        i*=i+1;
    }
    pthread_t id = pthread_self();
    double usec = stop();
    printf("Thread: %ld\nTime elapsed: %f\n",id,usec);
}

int main(int argc,char** argv)
{
    int c;
    int th;
    int threads=1;
    int seconds=1;
    while ((c = getopt (argc, argv, "s:t:")) != -1)
    {
        switch (c)
        {
        case 's':
            sscanf(optarg,"%d",&seconds);
            break;
        case 't':
            sscanf(optarg,"%d",&threads);
            break;
        default:
            break;
        }
    }
    struct args argument;
    pthread_t *thrds = (pthread_t *)malloc(sizeof(pthread_t)*threads);
    argument.duration=seconds;
    for(int i=0;i<threads;i++)
    {
        th=pthread_create(&thrds[i],NULL,function,&argument);
        if(th)
        {
            printf("error\n");
        }
    }
    for(int i=0;i<threads;i++)
    {
        pthread_join(thrds[i],NULL);
    }
}