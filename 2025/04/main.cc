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
  int m = lines.size();
  int n = lines[0].size();
  vector<pair<int, int>> dirs = {
    {1 , 0},
    {-1, 0},
    {0, 1},
    {0, -1},
    {1, 1},
    {-1, -1},
    {1, -1},
    {-1, 1}
  };

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (lines[i][j] != '@') {
        continue;
      }

      int cnt = 0;
      for (const auto&dir : dirs) {
        int newi = i+dir.first;
        int newj = j+dir.second;
        if (newi < 0 || newi >= m || newj < 0 || newj >+ n) {
          continue;
        }

        if (lines[newi][newj] == '@') {
          ++cnt;
        }
      }

      if (cnt < 4) {
        ++res;
      }
    }
  }

  cout << "Part 1: " << res << endl;
}

void part2(vector<string>& lines) {

  int res = 0;
  int m = lines.size();
  int n = lines[0].size();
  vector<pair<int, int>> dirs = {
    {1 , 0},
    {-1, 0},
    {0, 1},
    {0, -1},
    {1, 1},
    {-1, -1},
    {1, -1},
    {-1, 1}
  };

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (lines[i][j] != '@') {
        continue;
      }
      vector<pair<int, int>> check = {{i, j}};
      
      while (!check.empty()) {
        pair<int, int> curr = check.back();
        check.pop_back();
        if (lines[curr.first][curr.second] != '@') {
          continue;
        }

        vector<pair<int, int>> adj;
        for (const auto&dir : dirs) {
          int newi = curr.first+dir.first;
          int newj = curr.second+dir.second;
          if (newi < 0 || newi >= m || newj < 0 || newj >+ n) {
            continue;
          }

          if (lines[newi][newj] == '@') {
            adj.push_back({newi, newj});
          }
        }

        if (adj.size() < 4) {
          lines[curr.first][curr.second] = 'X';
          ++res;
          check.insert(check.end(), adj.begin(), adj.end());
        }
      }
    }
  }

  cout << "Part 2: " << res << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}