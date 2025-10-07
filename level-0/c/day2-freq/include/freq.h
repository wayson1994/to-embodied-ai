/**
 * @file     freq.h
 * @brief    freq.h
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.7
 **/

#ifndef FREQ_H
#define FREQ_H

#define ALPHA_SIZE 26

void count_letters(const char *buf, int freq[ALPHA_SIZE]);

char most_frequent(const int freq[ALPHA_SIZE]);

#endif