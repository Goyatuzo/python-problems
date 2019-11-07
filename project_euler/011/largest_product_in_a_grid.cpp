#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/**
Completed this one by just multiplying the numbers that lie east, south east, and south
of each element in the 
*/

int southEastProduct(int (&input)[20][20], int x, int y) {
    if (x > 16 || y > 16) {
        return -1;
    }
    
    int product = 1;
    
    for (int i = 0; i < 4; ++i) {
        product *= input[x + i][y + i];
    }
    
    return product;
}

int southWestProduct(int (&input)[20][20], int x, int y) {
    if (x < 3 || y > 16) {
        return -1;
    }
    
    int product = 1;
    
    for (int i = 0; i < 4; ++i) {
        product *= input[x - i][y + i];
    }
    
    return product;
}

int eastProduct(int (&input)[20][20], int x, int y) {
    if (x > 16) {
        return -1;
    }
    
    int product = 1;
    
    for (int i = 0; i < 4; ++i) {
        product *= input[x + i][y];
    }
    
    return product;
}

int southProduct(int (&input)[20][20], int x, int y) {
    // Boundary checking to make sure there are 3 north values.
    if (y > 16) {
        return -1;
    }
    
    int product = 1;
    
    for (int i = 0; i < 4; ++i) {
        product *= input[x][y + i];
    }
    
    return product;
}

int findMaxProduct(int (&input)[20][20]) {
    int max = -1;
    int j;
    
    for (int i = 0; i < 20; ++i) {
        for (int j = 0; j < 20; ++j) {
            // Find the max out of the three possible directions.
            int east = eastProduct(input, i, j);
            int southEast = southEastProduct(input, i, j);
            int south = southProduct(input, i, j);
            int southWest = southWestProduct(input, i, j);
            
            // Find the max out of the three.
            if (east > max) {
                max = east;
            }
            
            if (southEast > max) {
                max = southEast;
            }
            
            if (south > max) {
                max = south;
            }
            
            if (southWest > max) {
                max = southWest;
            }
        }
    }
    
    return max;
}

int main() {
    int grid[20][20];
    
    for (int i = 0; i < 20; ++i) {
        for (int j = 0; j < 20; ++j) {
            cin >> grid[j][i];
        }
    }
    
    
    cout << findMaxProduct(grid) << endl;
    
    return 0;
}
