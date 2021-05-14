#include <unistd.h>
#include <stdio.h>

void main(int argc,char** argv)
{
    char *salt;
    char *passwd;
    char *result;
    int c;
    while ((c = getopt (argc, argv, "s:p:")) != -1)
    {
        switch (c)
        {
        case 's':
            salt=optarg;
            break;
        case 'p':
            passwd=optarg;
            break;
        default:
            break;
        }
    }
    result=crypt(passwd,salt);
    printf("Password hash: %s\n",result);
}