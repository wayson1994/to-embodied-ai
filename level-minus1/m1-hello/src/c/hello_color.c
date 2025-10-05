/**
 * @file     hello_color.c
 * @brief    output Hello Color in red using escape characters
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

#include <stdio.h>

int main(int argc, char *argv[])
{
    (void)argc;
    (void)argv;

    printf("\033[31mHello Color\033[0m\n");

    return 0;
}