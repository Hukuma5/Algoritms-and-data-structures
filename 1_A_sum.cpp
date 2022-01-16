//
//  main.cpp
//  A-sum
//
//  Created by Никита Гуща on 13.09.2021.
//

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <iterator>

long long FindInt(std::string &s){
    long long k = 0;
    std::string buf = s;
    size_t digits = buf.find_first_of( "123456789-" );
    while (digits < buf.size()){
        digits = buf.find_first_of( "123456789-" );
            if (buf[digits] == '-'){
                if (digits + 1 < buf.size() && std::isdigit(buf[digits + 1])){
                    k += (atoi( buf.c_str() + digits ));
                    long long f = atoi( buf.c_str() + digits );
                    int h = 1;
                    while (f <= -10){
                        h++;
                        f /= 10;
                    }
                    int j = static_cast<int>(digits) + h + 1;
                    std::string buf2 = "";
                    for (int i = j; i < buf.size(); i++){
                        buf2 += buf[i];
                    }
                    
                    buf = buf2;
                    digits = buf.find_first_of( "123456789-" );
                } else if (digits + 1 < buf.size()){
                    std::string buf2 = "";
                    for (int i = digits + 1; i < buf.size(); i++){
                        buf2 += buf[i];
                    }
                    
                    buf = buf2;
                    digits = buf.find_first_of( "123456789-" );
                } else digits++;
            } else {
                k += atoi( buf.c_str() + digits );
                long long f = atoi( buf.c_str() + digits );
                int h = 1;
                while (f >= 10){
                    h++;
                    f /= 10;
                }
                int j = static_cast<int>(digits) + h;
                std::string buf2 = "";
                for (int i = j; i < buf.size(); i++){
                    buf2 += buf[i];
                }
                buf = buf2;
                digits = buf.find_first_of( "123456789-" );
            }
    }
    return k;
}

int main() {
    long long sum = 0;
    std::string t;
    while (std::getline(std::cin, t, ' ') || std::getline(std::cin, t, '\n')){
        long long hlp = FindInt(t);
        sum += hlp;
    }
    std::cout << sum;
    return 0;
}
