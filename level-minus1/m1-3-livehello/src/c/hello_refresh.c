/**
 * @file     hello_refresh.c
 * @brief    dynamic Hello: counter updates in place 10×/sec.
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

 #include <stdio.h>
 #include <time.h>
 #include <unistd.h>

 int main(int argc, char* argv[])
 {
    (void)argc;
    (void)argv;

    struct timespec req = {0, 100000000};
    for(int cnt = 0; cnt < 100; cnt++)
    {
        printf("\rHello %d", cnt);
        fflush(stdout);
        nanosleep(&req, NULL);
    }

    puts("");
    return 0;
 }