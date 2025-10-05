/**
 * @file     stopwatch.cpp
 * @brief    output elapsed 10s
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

 #include <iostream>
 #include <chrono>
 #include <thread>

 int main(int argc, char* argv[])
 {
    (void)argc;
    (void)argv;

    using namespace std::chrono;

    const auto period = milliseconds(100);

    for (int counter = 0; counter < 10; counter++)
    {
        std::cout << "elapsed : " << counter + 1 << "s" <<std::flush;

        std::this_thread::sleep_for(period);
    }

    return 0;
 }