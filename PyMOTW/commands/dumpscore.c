/* Simple example app to cause a core dump. */

#include <stdio.h>
#include <signal.h>

#include <sys/types.h>
#include <sys/time.h>
#include <sys/resource.h>

int main(int argc, char ** argv) {

    struct rlimit limit;

    limit.rlim_cur = limit.rlim_max = RLIM_INFINITY;
    setrlimit(RLIMIT_CORE, &limit);

    return raise(SIGABRT);
}