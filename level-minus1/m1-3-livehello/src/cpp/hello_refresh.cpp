/**
 * @file     hello_refresh.cpp
 * @brief    dynamic Hello: counter updates in place 10×/sec.
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

 #include <iostream>
 #include <chrono>
 #include <thread>

 int main(int argc, char* argv[])
 {
    using namespace std::chrono;
    
    const auto period = milliseconds(100);

    std::cout << std::unitbuf;

    for (int counter = 0; counter < 100; counter++)
    {
        std::count << "\rHello " << counter << std::flush;

        std::this_thread::sleep_for(period);
    }

    puts("");
    return 0;
 }