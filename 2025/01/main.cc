#include <fstream>
#include <iostream>
#include <string>
#include <vector>

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
  int sum = 50;
  int seenNils = 0;
  for (const auto& line : lines) {
    if(line[0] == 'L') {
      sum = (100 + (sum - (stoi(line.substr(1)) % 100))) % 100;
    }
    else if(line[0] == 'R') {
      sum = (sum + (stoi(line.substr(1)) % 100)) % 100;
    }

    if (sum == 0) {
      seenNils++;
    }
  }
  
  cout << "Part 1: " << seenNils << endl;
}

void part2(const vector<string>& lines) {
  int sum = 50;
  int seenNils = 0;
  for (const auto& line : lines) {
    int value = stoi(line.substr(1));
    if(line[0] == 'L') {
      seenNils += floor((100 - (sum - value)) / 100);
      if (sum == 0) seenNils--;
      sum = (100 + (sum - (value % 100))) % 100;
    }
    else if(line[0] == 'R') {
      seenNils += floor((sum + value) / 100);
      sum = (sum + (value % 100)) % 100;
    }
  }

  cout << "Part 2: " << seenNils << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}