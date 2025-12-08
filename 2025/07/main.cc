#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <set>

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
  queue<int> q;
  q.push(lines[0].find('S'));
  int m = lines.size();
  int n = lines[0].size();

  for (int i = 1; i < m; ++i) {
    set<int> seen;
    auto qSize = q.size();
    
    while(qSize--) {
      int j = q.front();
      q.pop();
      if (seen.find(j) != seen.end()) {
        continue;
      }

      if (lines[i][j] == '^') {
        ++res;
        if (j > 0) {
          q.push(j-1);
        }
        if (j+1 < n) {
          q.push(j+1);
        }
      }
      else {
        q.push(j);
      }
      seen.insert(j);
    }
  }

  cout << "Part 1: " << res << endl;
}

void part2(const vector<string>& lines) {
  long res = 0;
  int m = lines.size();
  int n = lines[0].size();
  vector<long> cols;
  cols.resize(n, 0);
  cols[lines[0].find('S')] = 1;

  for (int i = 1; i < m; ++i) {
    long nextJ = 0;
    for (int j = 0; j < n; ++j) {
      if (lines[i][j] == '^') {
        if (j > 0) {
          cols[j-1] += cols[j];
        }
        long tmp = cols[j];
        cols[j] = nextJ;
        nextJ = tmp;
      }
      else {
        cols[j] += nextJ;
        nextJ = 0;
      }
    }
  }
  
  for(int j = 0; j < n; ++j) {
    res += cols[j];
  }

  cout << "Part 2: " << res << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}