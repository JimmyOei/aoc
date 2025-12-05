#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

#define INPUT_FILE "input.txt"

vector<string> getInputLines() {
  ifstream file(INPUT_FILE);
  if (!file.is_open()) {
    cerr << "Error: Could not open input.txt" << endl;
    throw runtime_error("File open failed");
  }

  vector<string> lines;
  string line;
  while (getline(file, line)) {
    lines.push_back(line);
  }
  file.close();

  return lines;
}

void part1(const vector<string>& lines) {
  int res = 0;

  for (const auto& line : lines) {
    int lineSize = line.size();
    int largest = 0;
    int secondLargest = 0;
    for (int i = lineSize-2; i >= 0; --i) {
      int val = line[i] - '0';
      if (val >= largest) {
        secondLargest = largest;
        largest = val;
      }
    }
    if (line[lineSize-1] - '0' > secondLargest) {
      secondLargest = line[lineSize-1] - '0';
    }
    res += largest * 10 + secondLargest;
  }

  cout << "Part 1: " << res << endl;
}

void part2(const vector<string>& lines) {
  long res = 0;
  
  for (const auto& line : lines) {
    vector<int> nums;
    for (char c : line) {
      nums.push_back(c - '0');
    }

    int digits = 12;
    long sum = 0;
    int k = 0;
    for (int i = digits-1; i >= 0; --i) {
      int largest = 0;
      for (int j = k; j < nums.size()-i; ++j) {
        if (nums[j] > largest) {
          largest = nums[j];
          k = j+1;
        }
      }

      sum = sum * 10 + largest;
    }

    res += sum;
  }

  cout << "Part 2: " << res << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}