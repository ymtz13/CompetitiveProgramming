from collections import defaultdict
import random
from math import ceil, exp

random.seed(100)

NEIGHBORS = [(dy, dx) for dy in (-1, 0, 1, 2) for dx in (-2, -1, 0, 1, 2)]
# NEIGHBORS = [(dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1)]


def popcount(b):
    cnt = 0
    while b:
        cnt += b & 1
        b >>= 1
    return cnt


class Input:
    def __init__(
        self, grid_size: int, exit_cell_count: int, standard_deviation: int, exit_cells
    ):
        self.grid_size = grid_size
        self.exit_cell_count = exit_cell_count
        self.standard_deviation = standard_deviation
        self.exit_cells = exit_cells


class Temperature:
    MIN_TEMP = 0
    MAX_TEMP = 1000

    def __init__(self, inp: Input):
        self.inp = inp
        self.temperature = [[-1] * inp.grid_size for _ in range(inp.grid_size)]

    def init(self):
        inp = self.inp

        LOW = 0
        HIGH = 1
        MID = -1
        temp_level = [[MID] * inp.grid_size for _ in range(inp.grid_size)]

        for _ in range(100):
            for y, x in inp.exit_cells:
                for dy, dx in NEIGHBORS:
                    yy = (y + dy) % inp.grid_size
                    xx = (x + dx) % inp.grid_size
                    temp_level[yy][xx] = random.choice((LOW, HIGH))

            fingerprints = [0] * inp.exit_cell_count
            for i_exit, (y, x) in enumerate(inp.exit_cells):
                for i_neighbor, (dy, dx) in enumerate(NEIGHBORS):
                    yy = (y + dy) % inp.grid_size
                    xx = (x + dx) % inp.grid_size
                    fingerprints[i_exit] += (1 << i_neighbor) * temp_level[yy][xx]

            if len(set(fingerprints)) == inp.exit_cell_count:
                # print('unique fingerprint generated.')
                break

        self.fingerprints = fingerprints

        mid_temp = 500
        temp_diff = min(500, round(inp.standard_deviation / 1.2))
        self.temp_diff = temp_diff

        self.high_temp = high_temp = mid_temp + temp_diff
        self.low_temp = low_temp = mid_temp - temp_diff

        for y in range(inp.grid_size):
            for x in range(inp.grid_size):
                level = temp_level[y][x]
                if level == HIGH:
                    self.temperature[y][x] = high_temp
                if level == MID:
                    self.temperature[y][x] = mid_temp
                if level == LOW:
                    self.temperature[y][x] = low_temp

    def cost(self):
        result = 0
        grid_size = len(self.temperature)
        for y in range(grid_size):
            for x in range(grid_size):
                temp = self.temperature[y][x]
                x_next = (x + 1) % grid_size
                y_next = (y + 1) % grid_size

                temp_x = self.temperature[y][x_next]
                temp_y = self.temperature[y_next][x]

                d_temp_x = abs(temp_x - temp)
                d_temp_y = abs(temp_y - temp)

                result += d_temp_x**2 + d_temp_y**2

        return result

    def zero_likelihood(self, temps):
        inp = self.inp

        prob_low = prob_high = 1

        for temp in temps:
            diff_low = temp - self.low_temp
            diff_high = temp - self.high_temp

            v_low = diff_low / inp.standard_deviation
            v_high = diff_high / inp.standard_deviation

            prob_low *= exp(-v_low * v_low / 2)
            prob_high *= exp(-v_high * v_high / 2)

        return prob_low / (prob_low + prob_high)

    def print_fingerprints(self, inp: Input):
        for i_exit, (fingerprint, (y, x)) in enumerate(
            zip(self.fingerprints, inp.exit_cells)
        ):
            print(
                "i_exit:{:3d} ({:4d},{:4d}): {:015b}".format(i_exit, y, x, fingerprint)
            )

    def __str__(self):
        lines = [
            " ".join(map(lambda v: "{:4d}".format(v), row)) for row in self.temperature
        ]
        return "\n".join(lines)


class Measurement:
    def __init__(self, i: int, y: int, x: int):
        self.i = i
        self.y = y
        self.x = x
        self.result = None

    def set_result(self, result: int):
        self.result = result

    def cost(self):
        return 100 * (10 + abs(self.y) + abs(self.x))

    def __str__(self):
        if self.result is not None:
            return "{} {} {} {}".format(self.i, self.y, self.x, self.result)
        return "{} {} {}".format(self.i, self.y, self.x)


class Measurements:
    def __init__(self, inp: Input):
        self.inp = inp
        self.events = []

    def next(self):
        neighbor_size = len(NEIGHBORS)
        measurements_per_cell = 100 // neighbor_size
        measurements_per_hole = neighbor_size * measurements_per_cell

        target_hole = len(self.events) // measurements_per_hole
        target_cell = (
            len(self.events) % measurements_per_hole
        ) // measurements_per_cell

        if target_hole >= self.inp.exit_cell_count:
            return None

        dy, dx = NEIGHBORS[target_cell]

        measure = Measurement(target_hole, dy, dx)
        self.events.append(measure)
        return measure

    def cost(self):
        return sum([e.cost() for e in self.events])


class Estimation:
    def __init__(
        self, inp: Input, temperature: Temperature, measurements: Measurements
    ):
        self.inp = inp
        self.temperature = temperature
        self.measurements = measurements

    def exec(self):
        sum = defaultdict(int)
        cnt = defaultdict(int)
        for measure in self.measurements.events:
            key = (measure.i, measure.y, measure.x)
            sum[key] += measure.result
            cnt[key] += 1

        means = {key: sum[key] / cnt[key] for key in sum}
        estimated_levels = {key: 0 if mean < 500 else 1 for key, mean in means.items()}

        inp = self.inp

        estimated_fingerprints = [0] * inp.exit_cell_count
        priority = []
        for i_hole in range(inp.exit_cell_count):
            for i_neighbor, (dy, dx) in enumerate(NEIGHBORS):
                estimated_level = estimated_levels[(i_hole, dy, dx)]
                estimated_fingerprints[i_hole] += (1 << i_neighbor) * estimated_level

        for i_hole, estimated_fingerprint in enumerate(estimated_fingerprints):
            pass
            # print("i_hole:{:3d} : {:015b}".format(i_hole, estimated_fingerprint))

        for i_hole, estimated_fingerprint in enumerate(estimated_fingerprints):
            for i_exit, fingerprint in enumerate(self.temperature.fingerprints):
                priority.append(
                    (popcount(estimated_fingerprint ^ fingerprint), i_hole, i_exit)
                )

        priority.sort()

        # print(sum)
        # print(means)
        # print(priority)

        result = [None] * inp.exit_cell_count
        exit_assigned = [False] * inp.exit_cell_count
        for _, i_hole, i_exit in priority:
            if result[i_hole] is None and not exit_assigned[i_exit]:
                result[i_hole] = i_exit
                exit_assigned[i_exit] = True

        return result


class Problem:
    def __init__(self):
        pass

    def readInput(self):
        L, N, S = map(int, input().split())
        YX = [tuple(map(int, input().split())) for _ in range(N)]
        return Input(L, N, S, YX)

    def sendTemperature(self, temperature: Temperature):
        print(temperature)

    def measure(self, measurement: Measurement):
        print(measurement)
        result = int(input())
        return result

    def sendEstimate(self, estimate: Estimation):
        print(-1, -1, -1)
        for e in estimate.exec():
            print(e)
        return 0


class TestProblem:
    def __init__(self):
        pass

    def readInput(self):
        L = 50  # [10,  50]
        N = 100  # [60, 100]
        S = 30**2  # [ 1, 900]

        cells = [(y, x) for y in range(L) for x in range(L)]
        exits = random.sample(cells, N)
        inp = Input(L, N, S, sorted(exits))

        self.inp = inp
        self.exits = exits

        return inp

    def sendTemperature(self, temperature: Temperature):
        self.temp = temperature

    def measure(self, measurement: Measurement):
        exit = self.exits[measurement.i]
        y = (exit[0] + measurement.y) % self.inp.grid_size
        x = (exit[1] + measurement.x) % self.inp.grid_size
        temp = self.temp.temperature[y][x]
        result = max(
            0, min(1000, round(random.gauss(temp, self.inp.standard_deviation)))
        )
        return result

    def sendEstimate(self, estimate: Estimation):
        error_count = 0
        for i_hole, i_exit in enumerate(estimate.exec()):
            if self.exits[i_hole] != self.inp.exit_cells[i_exit]:
                error_count += 1
        return error_count


class Score:
    MAX_SCORE = 10**9
    CONSTANT_COST = 10**5

    def __init__(
        self, error_count: int, temperature: Temperature, measurements: Measurements
    ):
        self.error_count = error_count
        self.base_score = ceil((10**14) * pow(0.8, error_count))

        self.temperature_cost = temperature.cost()
        self.measurement_cost = measurements.cost()
        self.total_cost = (
            self.temperature_cost + self.measurement_cost + self.CONSTANT_COST
        )

        self.score = ceil(self.base_score / self.total_cost)

    def print_detail(self):
        print("       max_score: {:16d}".format(self.MAX_SCORE))
        print("           score: {:16d}".format(self.score))
        print("     error_count: {:16d}".format(self.error_count))
        print("      base_score: {:16d}".format(self.base_score))
        print("temperature_cost: {:16d}".format(self.temperature_cost))
        print("measurement_cost: {:16d}".format(self.measurement_cost))
        print("   constant_cost: {:16d}".format(self.CONSTANT_COST))
        print("      total_cost: {:16d}".format(self.total_cost))

    def line(self):
        return "score:{:16d},  error_cnt:{:3d},  temp_cost:{:16d},  meas_cost:{:16d}".format(
            self.score, self.error_count, self.temperature_cost, self.measurement_cost
        )


def solve(ProblemClass):
    problem = ProblemClass()
    # problem = ProblemClass()
    inp = problem.readInput()

    temp = Temperature(inp)
    temp.init()
    problem.sendTemperature(temp)
    # temp.print_fingerprints(inp)

    measurements = Measurements(inp)

    while True:
        measure = measurements.next()
        if not measure:
            break

        result = problem.measure(measure)
        measure.set_result(result)

    estimate = Estimation(inp, temp, measurements)
    error_count = problem.sendEstimate(estimate)

    return Score(error_count, temp, measurements)


if True:
    error_cnt_sum = 0
    n_trial = 50
    for trial in range(n_trial):
        score = solve(TestProblem)
        error_cnt_sum += score.error_count
        print("[{:2d}] {}".format(trial, score.line()))
    print("error_count_mean:{}".format(error_cnt_sum / n_trial))
