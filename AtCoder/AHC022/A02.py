class Input:
  def __init__(self, grid_size: int, exit_cell_count: int,
               standard_deviation: int, exit_cells):
    self.grid_size = grid_size
    self.exit_cell_count = exit_cell_count
    self.standard_deviation = standard_deviation
    self.exit_cells = exit_cells


class Temperature:
  def __init__(self, grid_size: int):
    self.temperature = [[-1] * grid_size for _ in range(grid_size)]

  def init(self, inp: Input):
    diff_temp = 10

    self.exit_temperatures = [0] * inp.exit_cell_count

    for i, (y, x) in enumerate(inp.exit_cells):
      temp = diff_temp * i
      self.temperature[y][x] = temp
      self.exit_temperatures[i] = temp

    for y in range(inp.grid_size):
      for x in range(inp.grid_size):
        if self.temperature[y][x] != -1: continue

        weighted_temp_sum = 0
        weight_sum = 0
        for i_exit, (y_exit, x_exit) in enumerate(inp.exit_cells):
          dx = abs(x - x_exit)
          dy = abs(y - y_exit)
          dist = min(inp.grid_size - dx, dx) + min(inp.grid_size - dy, dy)
          weight = inp.grid_size - dist

          weighted_temp_sum += weight * self.exit_temperatures[i_exit]
          weight_sum += weight

        self.temperature[y][x] = round(weighted_temp_sum / weight_sum)

  def init_old(self, inp: Input):
    diff_temp = 10
    max_temp = diff_temp * (inp.exit_cell_count - 1)
    bg_temp = max_temp // 2

    for y in range(inp.grid_size):
      for x in range(inp.grid_size):
        self.temperature[y][x] = bg_temp

    self.exit_temperatures = [0] * inp.exit_cell_count

    for i, (y, x) in enumerate(inp.exit_cells):
      temp = diff_temp * i
      self.temperature[y][x] = temp
      self.exit_temperatures[i] = temp

  def cost(self, inp: Input):
    result = 0
    for y in range(inp.grid_size):
      for x in range(inp.grid_size):
        temp = self.temperature[y][x]
        x_next = (x + 1) % inp.grid_size
        y_next = (y + 1) % inp.grid_size

        temp_x = self.temperature[y][x_next]
        temp_y = self.temperature[y_next][x]

        d_temp_x = abs(temp_x - temp)
        d_temp_y = abs(temp_y - temp)

        result += d_temp_x**2 + d_temp_y**2

    return result

  def __str__(self):
    lines = [' '.join(map(str, row)) for row in self.temperature]
    return '\n'.join(lines)


class Measurement:
  def __init__(self, i: int, y: int, x: int):
    self.i = i
    self.y = y
    self.x = x
    self.result = None

  def set_result(self, result: int):
    self.result = result

  def __str__(self):
    if self.result is not None:
      return "{} {} {} {}".format(self.i, self.y, self.x, self.result)
    return "{} {} {}".format(self.i, self.y, self.x)


class Measurements:
  def __init__(self, inp: Input):
    self.inp = inp
    self.events = []

  def next(self):
    measurements_per_exit_cell = 10
    target_cell = len(self.events) // measurements_per_exit_cell

    if target_cell >= self.inp.exit_cell_count:
      return None

    measure = Measurement(target_cell, 0, 0)
    self.events.append(measure)
    return measure


class Estimation:
  def __init__(self, inp: Input, temperature: Temperature,
               measurements: Measurements):
    self.inp = inp
    self.temperature = temperature
    self.measurements = measurements

  def exec(self):
    sum = [0] * (self.inp.exit_cell_count)
    cnt = [0] * (self.inp.exit_cell_count)
    for measure in self.measurements.events:
      sum[measure.i] += measure.result
      cnt[measure.i] += 1

    means = [s / c for s, c in zip(sum, cnt)]

    priority = []
    for i_hole, mean in enumerate(means):
      for i_exit, temp in enumerate(self.temperature.exit_temperatures):
        priority.append((abs(mean - temp), i_hole, i_exit))

    priority.sort()

    #print(sum)
    #print(means)
    #print(priority)

    result = [None] * inp.exit_cell_count
    exit_assigned = [False] * inp.exit_cell_count
    for _, i_hole, i_exit in priority:
      if result[i_hole] is None and not exit_assigned[i_exit]:
        result[i_hole] = i_exit
        exit_assigned[i_exit] = True

    return result


L, N, S = map(int, input().split())
YX = [tuple(map(int, input().split())) for _ in range(N)]

inp = Input(L, N, S, YX)

temp = Temperature(inp.grid_size)
temp.init(inp)
print(temp)

measurements = Measurements(inp)

while True:
  measure = measurements.next()
  if not measure: break

  print(measure)
  result = int(input())
  measure.set_result(result)

estimate = Estimation(inp, temp, measurements)
result = estimate.exec()

print(-1, -1, -1)
for e in result:
  print(e)
