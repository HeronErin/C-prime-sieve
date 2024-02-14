#pragma once
//    All credit to: https://github.com/mochow13/competitive-programming-library/blob/master/Math/Fast%20Integer%20Cube%20and%20Square%20Root.cpp
//    I do not claim this code.



unsigned int fast_sqrt_ui(unsigned int n){
    unsigned int c, g;

    c = g = 0x8000;
    for (; ;){
        if ((g * g) > n) g ^= c;
        c >>= 1;
        if (!c) return g;
        g |= c;
    }
}

int fast_cbrt(int n){
    int x, r = 30, res = 0;

    for (; r >= 0; r -= 3){
        res <<= 1;
        x = (3 * res * (res + 1)) + 1;
        if ((n >> r) >= x){
            res++;
            n -= (x << r);
        }
    }

    return res;
}

unsigned long long fast_sqrt_ull(unsigned long long n){
    unsigned long long c, g;

    c = g = 0x80000000;
    for (; ;){
        if ((g * g) > n) g ^= c;
        c >>= 1;
        if (!c) return g;
        g |= c;
    }
}

unsigned long long fast_cbrt_ull(unsigned long long n){
    int r = 63;
    unsigned long long x, res = 0;

    for (; r >= 0; r -= 3){
        res <<= 1;
        x = (res * (res + 1) * 3) + 1;
        if ((n >> r) >= x){
            res++;
            n -= (x << r);
        }
    }

    return res;
}