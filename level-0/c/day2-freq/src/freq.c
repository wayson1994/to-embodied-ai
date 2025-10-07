/**
 * @file     freq.c
 * @brief    print letters count & output most frequent
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.7
 **/

#include "../include/freq.h"

void count_letters(const char *buf, int freq[ALPHA_SIZE])
{    
    for (int i = 0; buf[i] != '\0'; i++)
    {
        char c = buf[i];
        if (c >= 'A' && c <= 'Z')
        {
            c += 32; 
        }
        
        if (c >= 'a' && c <= 'z')
        {
            ++freq[c - 'a'];
        }        
    }
    
}

char most_frequent(const int freq[ALPHA_SIZE])
{
    

    int max = 0;
    for (int i = 0; i < ALPHA_SIZE; i++)
    {
        if (freq[max] < freq[i])
        {
            max = i;
        }        
    }    

    return (char)('a' + max);    
}