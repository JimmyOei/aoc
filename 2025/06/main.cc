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
  long res = 0;
  vector<long> eqs;
  vector<bool> mult;

  for (const char c : lines.back()) {
    if (c == '*') {
      mult.push_back(true);
      eqs.push_back(1);
    }
    else if (c == '+') {
      mult.push_back(false);
      eqs.push_back(0);
    }
  }

  for (int i = 0; i < lines.size()-1; ++i) {
    long num = 0;
    int idx = 0;
    for (int j = 0; j < lines[i].size(); ++j) {
      if (lines[i][j] == ' ') {
        if (num > 0) {
          if (mult[idx]) {
            eqs[idx] *= num;
          }
          else {
            eqs[idx] += num;
          }
          num = 0;
          ++idx;
        }
        continue;
      }
      num = num * 10 + (lines[i][j] - '0');
    }
    if (num > 0) {
      if (mult[idx]) {
        eqs[idx] *= num;
      }
      else {
        eqs[idx] += num;
      }
    }
  }
  
  for (long num : eqs) {
    res += num;
  }

  cout << "Part 1: " << res << endl;
}

void part2(const vector<string>& lines) {
  long res = 0;
  vector<vector<long>> eqs;
  vector<pair<bool, int>> mult;

  int prev = 0;
  for (int i = 0; i < lines.back().size(); ++i) {
    if (lines.back()[i] == '*') {
      mult.push_back({true, i});
    }
    else if (lines.back()[i] == '+') {
      mult.push_back({false, i});
    }
  }

  eqs.resize(mult.size());

  for (int i = 0; i < mult.size(); ++i) {
    int digits;
    if (i < mult.size() - 1) {
      digits = mult[i+1].second - mult[i].second - 1;
    } else {
      digits = lines.back().size() - mult[i].second;
    }
    for (int j = 0; j < digits; ++j) {
      eqs[i].push_back(0);
    }
  }

  for (int i = 0; i < lines.size()-1; ++i) {
    int idx = 0;
    bool digit = false;
    for (int j = 0; j < lines[i].size(); ++j) {
      if (lines[i][j] == ' ') {
        if(digit) {
          digit = false;
          ++idx;
        }
        continue;
      }
      digit = true;
      eqs[idx][j-mult[idx].second] = eqs[idx][j-mult[idx].second] * 10 + (lines[i][j] - '0');
    }
  }
  
  for (int i = 0; i < mult.size(); ++i) {
    long nums = 1;
    for (const long num : eqs[i]) {
      if(mult[i].first) {
        nums *= num;
      }
      else {
        nums += num;
      }
    }
    if (!mult[i].first) {
      --nums;
    }
    res += nums;
  }

  cout << "Part 2: " << res << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}