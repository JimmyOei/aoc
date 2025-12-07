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
  vector<vector<long>> ranges;
  
  // process ranges
   int i = 0;
  for (; i < lines.size(); ++i) {
    if (lines[i] == "") {
      ++i;
      break;
    }

    int dashFind = lines[i].find('-');
    long start = stol(lines[i].substr(0, dashFind));
    long end = stol(lines[i].substr(dashFind+1));
    ranges.push_back({start, end});
  }

  sort(ranges.begin(), ranges.end());

  vector<vector<long>> merged;
  for (const auto& range : ranges) {
    if (merged.empty() || merged.back()[1] < range[0]) {
      merged.push_back(range);
    } else {
      merged.back()[1] = max(merged.back()[1], range[1]);
    }
  }

  for (; i < lines.size(); ++i) {
    long num = stol(lines[i]);
    for (int j = 0; j < merged.size(); ++j) {
      if (num > merged[j][1]) {
        continue;
      }

      if (num >= merged[j][0]) {
        ++res;
      }
      break;
    }
  }

  cout << "Part 1: " << res << endl;
}

void part2(const vector<string>& lines) {
  long res = 0;
  vector<vector<long>> ranges;
  
  // process ranges
   int i = 0;
  for (; i < lines.size(); ++i) {
    if (lines[i] == "") {
      ++i;
      break;
    }

    int dashFind = lines[i].find('-');
    long start = stol(lines[i].substr(0, dashFind));
    long end = stol(lines[i].substr(dashFind+1));
    ranges.push_back({start, end});
  }

  sort(ranges.begin(), ranges.end());

  vector<vector<long>> merged;
  for (const auto& range : ranges) {
    if (merged.empty() || merged.back()[1] < range[0]) {
      merged.push_back(range);
    } else {
      merged.back()[1] = max(merged.back()[1], range[1]);
    }
  }

  for (const auto& range : merged) {
    res += (range[1]-range[0]) + 1;
  }
  
  cout << "Part 2: " << res << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}