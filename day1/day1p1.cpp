#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    // Open input file
    ifstream input;
    input.open("input.txt");


    // Read through file, creating a list for each column
    vector<int> firstCol;
    vector<int> secCol;


    string line;
    string delimiter = " ";

    while (getline(input, line)) {
        firstCol.push_back(stoi(line.substr(0, line.find(delimiter))));
        secCol.push_back(stoi(line.substr(line.find(delimiter) + 1)));
    }

    // Sort lists
    sort(firstCol.begin(), firstCol.end());
    sort(secCol.begin(), secCol.end());

    // Calculate sum of diffs
    int totalDiff = 0;

    for(int i = 0; i < firstCol.size(); i++) {
        totalDiff += abs(firstCol[i] - secCol[i]);
    }

    // Output
    cout << totalDiff << endl;

    // Clean up
    input.close();
    return 0;
}