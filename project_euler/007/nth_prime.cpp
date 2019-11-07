#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
#include <limits.h>

using namespace std;

vector<int> primeList(int highestDigit) {
    unordered_map<int, bool> sieve;
    
    vector<int> primes;
    
for (int i = 2; i < highestDigit; ++i) {
        if (sieve.count(i) == 0) {
            primes.push_back(i);
        }
        
        for (int j = 1; (j * i) < highestDigit; ++j) {
            sieve.emplace(i * j, false);
        }
    }
    
    return primes;
}

int main() {
    int t;
    cin >> t;
    
    vector<int> primes = primeList(500000);
    
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        
        cout << primes[n - 1] << endl;
    }
    
    return 0;
}
