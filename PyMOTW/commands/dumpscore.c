/* Simple example app to cause a core dump. */

#include "stdio.h"

int main(int argc, char ** argv) {
    char * p = NULL;
    printf(p);
}