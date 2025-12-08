#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>

using namespace std;

#define INPUT_FILE "input.txt"

class UnionFind {
  vector<int> parent;
  vector<int> rank;

public:
  UnionFind(int n) : parent(n), rank(n, 0) {
    for (int i = 0; i < n; ++i) {
      parent[i] = i; 
    }
  }

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void unite(int x, int y) {
    int rootX = find(x);
    int rootY = find(y);

    if (rootX == rootY) return; 

    if (rank[rootX] < rank[rootY]) {
      parent[rootX] = rootY;
    } else if (rank[rootX] > rank[rootY]) {
      parent[rootY] = rootX;
    } else {
      parent[rootY] = rootX;
      rank[rootX]++;
    }
  }

  bool connected(int x, int y) {
    return find(x) == find(y);
  }

  int countSets() {
    set<int> uniqueRoots;
    for (int i = 0; i < parent.size(); ++i) {
      uniqueRoots.insert(find(i));
    }
    return uniqueRoots.size();
  }

  vector<int> getSets() {
    map<int, int> setSize;
    for (int i = 0; i < parent.size(); ++i) {
      int root = find(i);
      setSize[root]++;
    }
    vector<int> sizes;
    for (auto& p : setSize) {
      sizes.push_back(p.second);
    }
    return sizes;
  }
};

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
  vector<vector<int>> points;
  vector<pair<double, vector<int>>> dists;

  for (const auto& line : lines) {
    int num = 0;
    vector<int> cords;
    for (int j = 0; j < line.size(); ++j) {
      if (line[j] == ',') {
        cords.push_back(num);
        num = 0;
        continue;
      }
      num = num * 10 + (line[j] - '0');
    }
    cords.push_back(num);
    points.push_back(cords);
  }

  for (int i = 0; i < points.size(); ++i) {
    for (int j = i + 1; j < points.size(); ++j) {
      double dist = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2) + pow(points[i][2] - points[j][2], 2);
      dists.push_back({dist, {i, j}});
    }
  }

  sort(dists.begin(), dists.end());

  UnionFind uf(points.size());

  int K = 1000;

  for (int idx = 0; idx < K; ++idx) {
    int i = dists[idx].second[0];
    int j = dists[idx].second[1];
    uf.unite(i, j);
  }

  vector<int> sets = uf.getSets();
  sort(sets.begin(), sets.end(), greater<>());
  res = sets[0] * sets[1] * sets[2];

  cout << "Part 1: " << res << endl;
}

void part2(const vector<string>& lines) {
  long res = 0;
  vector<vector<int>> points;
  vector<pair<double, vector<int>>> dists;

  for (const auto& line : lines) {
    int num = 0;
    vector<int> cords;
    for (int j = 0; j < line.size(); ++j) {
      if (line[j] == ',') {
        cords.push_back(num);
        num = 0;
        continue;
      }
      num = num * 10 + (line[j] - '0');
    }
    cords.push_back(num);
    points.push_back(cords);
  }

  for (int i = 0; i < points.size(); ++i) {
    for (int j = i + 1; j < points.size(); ++j) {
      double dist = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2) + pow(points[i][2] - points[j][2], 2);
      dists.push_back({dist, {i, j}});
    }
  }

  sort(dists.begin(), dists.end());

  UnionFind uf(points.size());

  int idx = 0;
  while(uf.countSets() != 1) {
    int i = dists[idx].second[0];
    int j = dists[idx].second[1];
    ++idx;
    uf.unite(i, j);
  }
  res = points[dists[idx-1].second[0]][0] * points[dists[idx-1].second[1]][0];

  cout << "Part 2: " << res << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}