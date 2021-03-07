#include <stdlib.h> 
#include <stdio.h>
#include <unistd.h>

int main(){
    int id;
    long pid;
    id=fork();

    if(id == 0)
    {
        pid=getpid();
        printf("child process with pid: %ld\n",pid);
    }
    else
    {
        pid = getpid();
        printf("parent process with pid: %ld\n",pid);
    }
}