#include <bits/stdc++.h>
#include <string>
using namespace std;

int find_largest_divisor(int N){
    int d=0;
    for(int divisor=2; divisor <= 26; divisor++){
        if (N%divisor == 0){
            d = divisor;
        }
    }
    return d;
}

/*
Create a string with the same number of occurence of char inside
Example :
For N = 3
returns : abc
for N = 52
returns : aabb...zz
*/
string solution(int N) {
    string anwser;
    int divisor = find_largest_divisor(N);
    if(!divisor || N<=0 || N>200000){
        return "";
    }
    int loop = (N/divisor);
    char carac;
    //Number of occurence
    for(int i = 0; i < loop; i++){
        //Number of charac
        for(int c = 0; c< divisor; c++){
            carac = static_cast<char>(c+97);
            anwser += carac;
        }
    }
    return anwser;
}

