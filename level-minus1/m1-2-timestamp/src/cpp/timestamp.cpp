/**
 * @file     timestamp.cpp
 * @brief    output timestamp
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

 #include <chrono>
 #include <iostream>

 int main (int argc, char* argv[])
 {
    (void)argc;
    (void)argv;
    
    using namespace std::chrono;
    auto ts = duration_cast<seconds>(system_clock::now().time_since_epoch());
    std::cout<<"timestamp : "<<ts.count()<<std::endl;

    return 0;
 }