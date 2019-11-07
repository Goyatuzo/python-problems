#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;


unordered_map<int, int> generateCollatzLengths(int highest) {
    unordered_map<int, int> chain = {{1, 1}};
    unordered_map<int, int> lengths = {{1, 1}, {2, 2}};
    
    for (int i = 2; i <= highest; ++i) {
        int curr = i;
        int last;
        int count = 0;
        
        while (curr != 1 && chain.count(curr) == 0) {
            last = curr;
            
            if (curr % 2 == 0) {
                curr /= 2;
            } else {
                curr = 3 * curr + 1;
            }
            
            ++count;
            chain.emplace(last, curr);
        }
        
        // If the length exists, make sure to find the highest possible length.
        if (lengths.count(curr) != 0) {
            count += lengths[curr];
        }
        
        cout << "i: " << i << ", COUNT: " << count << endl;
        
        // Once the value has been found, add it to the lengths.
        if (lengths.count(curr) > 0) {
            lengths.emplace(i, count);
        }
        
        curr = i;
        // From here, it's making sure each element in the sequence has a length.
        while (count > 0) {
            curr = lengths[curr];
            
            cout << curr << endl;
            
            // If the current sequence exists, no more left to do.
            if (lengths.count(curr) > 0) {
                break;
            }
            lengths.emplace(curr, --count);
        }
    }
    
    return lengths;
}

int main() {
        unordered_map<int, int> results = generateCollatzLengths(20);
        
        for (int i = 1; i < 15; ++i) {
            cout << "i: " << i << ", length: " << results[i] << endl;
        }

    
    return 0;
}
