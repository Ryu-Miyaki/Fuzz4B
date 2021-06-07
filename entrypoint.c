#include <stdio.h>
#include <signal.h>

void __gcov_dump(void);
void my_handler(int signum){__gcov_dump();SIG_DFL(signum);}

int main(){
    struct sigaction new_action, old_action;
    new_action.sa_handler = my_handler;
    sigemptyset(&new_action.sa_mask);
    new_action.sa_flags = 0;
    
    // SIGILL
    sigaction(SIGILL, NULL, &old_action);
    if(old_action.sa_handler != SIG_IGN)
        sigaction(SIGILL, &new_action, NULL);
    // SIGABRT
    sigaction(SIGABRT, NULL, &old_action);
    if(old_action.sa_handler != SIG_IGN)
        sigaction(SIGABRT, &new_action, NULL);
    // SIGFPE
    sigaction(SIGFPE, NULL, &old_action);
    if(old_action.sa_handler != SIG_IGN)
        sigaction(SIGFPE, &new_action, NULL);
    // SIGSEGV
    sigaction(SIGSEGV, NULL, &old_action);
    if(old_action.sa_handler != SIG_IGN)
        sigaction(SIGSEGV, &new_action, NULL);
    
    entry();

    return 0;
}