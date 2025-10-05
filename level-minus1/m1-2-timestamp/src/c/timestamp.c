/**
 * @file     timestamp.c
 * @brief    output timestamp
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

 #include <stdio.h>
 #include <time.h>

 int main (int argc, char* argv[])
 {
    (void)argc;
    (void)argv;

    time_t current_time;

    // get the current time
    current_time = time(NULL);

    // output the Unix timestamp (seconds since 1970-01-01 UTC) up to now
    printf("timestamp : %ld\n", current_time);

    return 0;
 }