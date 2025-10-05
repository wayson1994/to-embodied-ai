/**
 * @file     hello_color.cpp
 * @brief    output Hello Color in red using escape characters
 * @version  1.0
 * @author   Wayson
 * @date     2025.10.5
 **/

 #include <iostream>

 int main(int argc, char *argv[])
 {
    (void)argc;
    (void)argv;

    std::cout<<"\033[31mHello Color\033[0m"<<std::endl;

    return 0;
 }