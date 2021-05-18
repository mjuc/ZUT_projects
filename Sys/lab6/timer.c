//PS IN1 320 LAB06
//Michał Jucewicz
//jm44353@zut.edu.pl
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <stdio.h>
#include <pthread.h>

clock_t *begin;
static pthread_key_t key;
static pthread_once_t once = PTHREAD_ONCE_INIT;

static void freeMemory(void *buffer)
{
    free(buffer);
}
static void createKey(void)
{
    pthread_key_create(&key, freeMemory);
}

void start()
{
    pthread_once(&once,createKey);
    begin=pthread_getspecific(key);
    if(begin==NULL)
    {
        begin=(clock_t*)malloc(sizeof(clock_t));
        *begin=clock();
        pthread_setspecific(key,begin);
    }
}

double stop()
{
    clock_t end = clock();
    double elapsed = (double)(end - *begin) * 1000.0 / CLOCKS_PER_SEC;
    return elapsed;
}