/**
 * @file     main.c
 * @brief    main
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.7
 **/

/* 
 * TODO(day2-fileIO): 支持命令行文件参数
 * 1. 若 argc == 2，用 fopen(argv[1],"r") 打开文件
 *    失败时 perror() 并返回 EXIT_FAILURE
 * 2. 把当前 stdin 读取逻辑封装成函数，对 FILE *fp 循环 fgets
 * 3. 结束后 if (fp != stdin) fclose(fp)
 * 4. 自测：./build/main poem.txt 与 echo "" | ./build/main
 */

#include <stdio.h>
#include "../include/freq.h"

int main (int argc, char *argv[])
{
    (void)argc;
    (void)argv;

    char buf[1024];
    int freq[ALPHA_SIZE] = {0};

    printf("Enter a statement to count letters:\n");

    if (fgets(buf, sizeof(buf), stdin) == NULL)
        return 0;

    count_letters(buf, freq);

    for (int i = 0; i < ALPHA_SIZE; i++)
    {
        if (freq[i] != 0)
        {
            printf("%c : %d\n", 'a' + i, freq[i]);
        }
    }

    char c = most_frequent(freq);

    if (c == 'a' && freq[0] == 0)
    {
        printf("No letters found.\n");
    }
    else
    {
        printf("Most frequent: %c\n", c);
    }

    return 0;
}