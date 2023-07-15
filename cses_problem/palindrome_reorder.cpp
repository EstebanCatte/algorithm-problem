#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

bool compareByFrequency(const pair<char, int>& a, const pair<char, int>& b) {
    bool aIsEven = a.second % 2 == 0;
    bool bIsEven = b.second % 2 == 0;

    if (aIsEven && !bIsEven) {
        return true;
    } else if (!aIsEven && bIsEven) {
        return false;
    } else {
        return a.second < b.second;
    }
}

int main()
{
    string str, pal;
    cin >> str;
    char* characters = new char[str.length() + 1];
    char* anwser = new char[str.length() + 1];
    copy(str.begin(), str.end(), characters);

    // Compter le nombre d'occurrences de chaque caractère dans la chaîne
    map<char, int> charCount;
    for (int c=0; c<str.length(); c++) {
        charCount[characters[c]]++;
    }
    // Trier les caractères en fonction de leur fréquence
    vector< pair<char, int> > sortedChars(charCount.begin(), charCount.end());
    sort(sortedChars.begin(), sortedChars.end(), compareByFrequency);

    long int compt = 0;
    for (size_t i = 0; i < sortedChars.size(); i++) {
        //cout << sortedChars[i].first ;
        for(long int j=0; j<sortedChars[i].second; j++){
            characters[compt] = sortedChars[i].first;
            compt++;
        }
    }

    compt = 0;
    for(long int i=0; i<str.length(); i+=2){
        //cout << "Charac traite : " << characters[i] << endl;
        anwser[compt] = characters[i];
        compt++;
    }
    
    for(long int i=str.length()%2; i<str.length()+1; i+=2){
        //cout << "Charac traite : " << characters[i] << endl;
        anwser[compt] = characters[str.length() - i - 1];
        compt++;
    }

    int length = str.length();
    //check if is a palindrome
    for (long int i =0; i<length/2; i++){
        if (anwser[i] != anwser[length - 1 - i]){
            cout << "NO SOLUTION";
            return 0;
        }
    }

    for (int i = 0; i < str.length(); i++) {
        cout << anwser[i];
    }
    cout << endl;

    delete[] characters;
    delete[] anwser;

    return 0;
}







