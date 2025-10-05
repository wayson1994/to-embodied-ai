/**
 * @file     stopwatch.c
 * @brief    output elapsed 10s
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

#include <stdio.h>
#include <time.h>

int main(int argc, char* argv[])
{
    (void)argc;
    (void)argv;

    struct timespec req = {1, 0};

    for (int i = 0; i < 10; i++)
    {
        printf("elapsed : %d s\n", i + 1);
        fflush(stdout);
        nanosleep(&req, NULL);
    }    

    return 0;
}