#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

/**
 * Convert line string input into vector<int> and remove spaces.
 * 
 * @param line - Line from input file
 * @return vector<int> - Line values as integer vector (with spaces removed)
 */
vector<int> convertLineToVector(string line)
{
    vector<int> vals;
    string delimiter = " ";
    size_t pos = 0;

    while((pos = line.find(delimiter)) != string::npos) {
        int val = stoi(line.substr(0, pos));
        vals.push_back(val);

        line.erase(0, pos + delimiter.length());
    }
    vals.push_back(stoi(line));

    return vals;
}

/**
 * Desc comparison function
 */
bool comp(int a, int b) {
    return a > b;
}

/**
 * Return whether the param vector is sorted asc *or* desc.
 * 
 * @param values - Integer vector to check
 * @return bool - True if the vector is sorted either asc *or* desc, false otherwise.
 */
bool isOrdered(vector<int> values)
{
    return is_sorted(values.begin(), values.end()) || is_sorted(values.begin(), values.end(), comp);
}

/**
 * Return whether adjancent values of the param vector *always* differ by at least one and at most three.
 * 
 * @param values - Integer vector to check
 * @return bool - True if adjancent values of the param vector *always* differ by at least one and at most three, false otherwise.
 */
bool isAdjacent(vector<int> values)
{
    for(int i = 0; i < values.size() - 1; i++) {
        int absDiff = abs(values[i] - values[i + 1]);
        if(absDiff < 1 || absDiff > 3) {
            return false;
        }
    }

    return true;
}


/**
 * Day 2 part 1 entry point.
 * 
 * @return int - Exit code
 */
int main()
{

    // Open input file
    ifstream input;
    input.open("input.txt");

    // Read through file
    int safeLines = 0;
    
    string line;
    while (getline(input, line)) {
        // Turn string line into int vector
        vector<int> vals = convertLineToVector(line);

        if(isOrdered(vals) && isAdjacent(vals)) {
            safeLines++;
        }
        else {
            bool stillSafe = true;
            for(int i = 0; i < vals.size(); i++) {
                vector<int> temp = vals;
                temp.erase(temp.begin() + i);

                // std::cout << "Is ordered: " << isOrdered(temp) << std::endl;
                // std::cout << "Is adjacent: " << isAdjacent(temp) << std::endl;
                // std::cout << std::endl;

                // If copy is now safe after removing one entry, the list is safe :)
                if(isOrdered(temp) && isAdjacent(temp)) {
                    safeLines++;
                    break;
                }
            }
        }
    }

    // Output
    std::cout << "# of safe lines: " << safeLines << std::endl;

    // Cleanup
    input.close();
    return 0;
}