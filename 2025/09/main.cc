#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

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

vector<vector<long>> parsePoints(const vector<string>& lines) {
  vector<vector<long>> points;
  for (const auto& line : lines) {
    long num = 0;
    vector<long> coords;
    for (char c : line) {
      if (c == ',') {
        coords.push_back(num);
        num = 0;
      } else {
        num = num * 10 + (c - '0');
      }
    }
    coords.push_back(num);
    points.push_back(coords);
  }
  return points;
}

void part1(const vector<string>& lines) {
  vector<vector<long>> points = parsePoints(lines);
  long long maxArea = 0;

  for (size_t i = 0; i < points.size(); ++i) {
    for (size_t j = i + 1; j < points.size(); ++j) {
      long long width = abs(points[i][0] - points[j][0]) + 1;
      long long height = abs(points[i][1] - points[j][1]) + 1;
      maxArea = max(maxArea, width * height);
    }
  }

  cout << "Part 1: " << maxArea << endl;
}

bool isOnBoundary(long px, long py, const vector<vector<long>>& polygon) {
  for (size_t i = 0; i < polygon.size(); ++i) {
    long x1 = polygon[i][0], y1 = polygon[i][1];
    long x2 = polygon[(i + 1) % polygon.size()][0], y2 = polygon[(i + 1) % polygon.size()][1];

    if (x1 == x2 && px == x1 && min(y1, y2) <= py && py <= max(y1, y2)) return true;
    if (y1 == y2 && py == y1 && min(x1, x2) <= px && px <= max(x1, x2)) return true;
  }
  return false;
}

bool isInsidePolygon(long px, long py, const vector<vector<long>>& polygon) {
  int count = 0;
  for (size_t i = 0; i < polygon.size(); ++i) {
    long x1 = polygon[i][0], y1 = polygon[i][1];
    long x2 = polygon[(i + 1) % polygon.size()][0], y2 = polygon[(i + 1) % polygon.size()][1];

    if (x1 == x2 && ((y1 <= py && py < y2) || (y2 <= py && py < y1)) && px < x1) {
      count++;
    }
  }
  return count % 2 == 1;
}

bool isInsideOrOnPolygon(long px, long py, const vector<vector<long>>& polygon) {
  return isOnBoundary(px, py, polygon) || isInsidePolygon(px, py, polygon);
}

bool isRectangleValid(long x1, long y1, long x2, long y2, const vector<vector<long>>& polygon) {
  if (x1 > x2) swap(x1, x2);
  if (y1 > y2) swap(y1, y2);

  if (!isInsideOrOnPolygon(x1, y1, polygon)) return false;
  if (!isInsideOrOnPolygon(x2, y2, polygon)) return false;
  if (!isInsideOrOnPolygon(x1, y2, polygon)) return false;
  if (!isInsideOrOnPolygon(x2, y1, polygon)) return false;

  long step = max(1L, max((x2 - x1) / 100, (y2 - y1) / 100));

  for (long x = x1; x <= x2; x += step) {
    if (!isInsideOrOnPolygon(x, y1, polygon)) return false;
    if (!isInsideOrOnPolygon(x, y2, polygon)) return false;
  }

  for (long y = y1; y <= y2; y += step) {
    if (!isInsideOrOnPolygon(x1, y, polygon)) return false;
    if (!isInsideOrOnPolygon(x2, y, polygon)) return false;
  }

  for (long x = x1; x <= x2; x += step) {
    for (long y = y1; y <= y2; y += step) {
      if (!isInsideOrOnPolygon(x, y, polygon)) return false;
    }
  }

  return true;
}

void part2(const vector<string>& lines) {
  vector<vector<long>> points = parsePoints(lines);
  long long maxArea = 0;

  for (size_t i = 0; i < points.size(); ++i) {
    for (size_t j = i + 1; j < points.size(); ++j) {
      if (isRectangleValid(points[i][0], points[i][1], points[j][0], points[j][1], points)) {
        long long width = abs(points[i][0] - points[j][0]) + 1;
        long long height = abs(points[i][1] - points[j][1]) + 1;
        maxArea = max(maxArea, width * height);
      }
    }
  }

  cout << "Part 2: " << maxArea << endl;
}

int main() {
  vector<string> lines = getInputLines();

  part1(lines);
  part2(lines);

  return 0;
}