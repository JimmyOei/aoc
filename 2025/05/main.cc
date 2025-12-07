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
  vector<vector<int>> ranges;
  
  // process ranges
  int i = 0;
  for (; i < lines.size(); ++i) {
    cout << i << " " << line << endl;
    if (line[i] == "") {
      break;
    }

    int dashFind = line.find('-');
    long start = stol(line.substr(0, dashFind));
    long end = stol(line.substr(dashFind+1));

    for (int j = 0; j < ranges.size(); ++j) {
      if (start > ranges[j][1]) {
        continue;
      }

      if (start < ranges[j][0]) {
        if (end >= ranges[j][0]) {
          ranges[j][0] = start;
          ranges[j][1] = max(ranges[j][1], end);
        }
        else {
          ranges.insert(j, {start, end});
        }
        break;
      }

      if (end <= ranges[j][1]) {
        break;
      }
      
      start = ranges[j][0];
      while(j < ranges.size()-1 && end > ranges[j][1]) {
        ranges.erase(ranges.begin()+j);
      }
      ranges[j][0] = start;
      ranges[j][1] = max(ranges[j][1], end);
    }

    for (const auto& v : ranges) {
      cout << v[0] << "-" << v[1] << endl;
    }
  }

  cout << "Part 1: " << res << endl;
}

void part2(const vector<string>& lines) {
  int res = 0;
  

  cout << "Part 2: " << res << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}