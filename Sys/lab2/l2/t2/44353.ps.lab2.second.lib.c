#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <pwd.h>

void printUser(char *input)
{
    struct passwd *tmp = getpwnam(input);
    printf("%s\n%d\n",tmp->pw_name,tmp->pw_uid);
}