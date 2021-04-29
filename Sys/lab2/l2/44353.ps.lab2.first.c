#include <stdlib.h>
#include <stdio.h>
#include <utmpx.h>
#include <sys/types.h>
#include <pwd.h>

int main(){
    struct utmpx *user_entry = getutxent();
    while ((user_entry = getutxent())!= (struct utmpx *) NULL) {
        if (user_entry->ut_type == USER_PROCESS){
            struct passwd *tmp = getpwnam(user_entry->ut_user);
            printf("%s\n%d\n",tmp->pw_name,tmp->pw_uid);
        }
    }
    return 0;
}
