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

vector<string> getRanges(const vector<string>& lines) {
  vector<string> ranges;
  for (const auto& line : lines) {
    stringstream ss(line);
    string range;
    while (getline(ss, range, ',')) {
      ranges.push_back(range);
    }
  }
  return ranges;
}

void part1(const vector<string>& lines) {
  long sum = 0;
  vector<string> ranges = getRanges(lines);
  for (const auto& range : ranges) {
    vector<string> parts;
    int dashIndex = range.find('-');
    string firstPart = range.substr(0, dashIndex);
    string secondPart = range.substr(dashIndex + 1);
    long firstNum = stol(firstPart);
    long secondNum = stol(secondPart);

    for (long i = firstNum; i <= secondNum; ++i) {
      string num = to_string(i);
      if (num.size() % 2 != 0) {
        continue;
      }

      int p = 0;
      int q = num.size() / 2;
      bool match = true;
      for (; q < num.size(); ++p, ++q) {
        if (num[p] != num[q]) {
          match = false;
          break;
        }
      }
      if (match) {
        sum += i;
      }
    }
  } 

  cout << "Part 1: " << sum << endl;
}

void part2(const vector<string>& lines) {
  long sum = 0;
  vector<string> ranges = getRanges(lines);
  for (const auto& range : ranges) {
    vector<string> parts;
    int dashIndex = range.find('-');
    string firstPart = range.substr(0, dashIndex);
    string secondPart = range.substr(dashIndex + 1);
    long firstNum = stol(firstPart);
    long secondNum = stol(secondPart);

    for (long i = firstNum; i <= secondNum; ++i) {
      string num = to_string(i);

      int p = 0;
      int q = 1;
      int k = 1;
      while (q < num.size()) {
        if (p == k) {
          p = 0;
        }
        if (num[p] == num[q]) {
          ++p;
          ++q;
        } else {
          p = 0;
          ++k;
          q = k;
        }
      }

      if (p == k) {
        sum += i;
      }
    }
  } 

  cout << "Part 2: " << sum << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}