#include <stdlib.h>
#include <stdio.h>
#include <utmpx.h>

int main(){
    struct utmpx *user_entry = getutxent();
    while ((user_entry = getutxent())!= (struct utmpx *) NULL) {
        if (user_entry->ut_type == USER_PROCESS){
            printUser(user_entry->ut_user);
        }
    }
    return 0;
}
