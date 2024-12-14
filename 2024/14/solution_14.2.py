import matplotlib.pyplot as plt

input = open('./input_14.txt', 'r')
lines = input.readlines()
lines = [line.strip().split(' ') for line in lines]

robots = []
for line in lines:
  point = line[0].split(',')
  vel = line[1].split(',')
  robots.append([[int(point[0][2:]), int(point[1])], [int(vel[0][2:]), int(vel[1])]])

m = 101
n = 103

def calc_next_point(px, py, vx, vy):
  nextx = px+vx
  nexty = py+vy
  if nextx < 0:
    nextx = m + nextx
  if nextx >= m:
    nextx = nextx - m
  if nexty < 0:
    nexty = n + nexty
  if nexty >= n:
    nexty = nexty - n

  return [nextx, nexty]

lseconds = 0
seconds = 10000
for s in range(seconds):
  for r in robots:
    px, py = r[0]
    vx, vy = r[1]
    r[0] = calc_next_point(px, py, vx, vy)
  if s >= lseconds:
    plt.figure()
    x_vals = [r[0][0] for r in robots]
    y_vals = [r[0][1] for r in robots]
    plt.scatter(x_vals, y_vals)
    plt.savefig(f'./output/{s}.png')
    plt.close()