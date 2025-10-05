/**
 * @file     stopwatch_ns.c
 * @brief    output 10 pieces of ns
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

#include <iostream>
#include <chrono>
#include <unistd.h>

int main(int argc, char* argv[])
{
    (void)argc;
    (void)argv;

    using namespace std::chrono;

    for (int i = 0; i < 10; i++)
    {
        std::cout << "ns : " << duration_cast<nanoseconds>(steady_clock::now().time_since_epoch()).count()
    << std::endl;
    }

    return 0;
}