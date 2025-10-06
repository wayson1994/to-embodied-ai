/**
 * @file     stopwatch_ns.c
 * @brief    output 10 pieces of ns
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

#define _GNU_SOURCE
#include <stdio.h>
#include <time.h>

int main(int argc, char *argv[])
{
    (void)argc;
    (void)argv;

    for (int count = 0; count < 10; count++)
    {
        struct timespec ts;

        if (clock_gettime(CLOCK_MONOTONIC, &ts) == -1)
        {
            perror("clock_gettime");
            return 1;
        }

        printf("ns : %ld%ld\n", ts.tv_sec, ts.tv_nsec);
    }

    return 0;
}
