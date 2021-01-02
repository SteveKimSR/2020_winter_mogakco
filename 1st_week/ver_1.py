#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    total_count = 2 * n - 2

    temp_r = r_q
    temp_c = c_q

    while temp_r <= n and temp_c <= n:
        temp_r += 1
        temp_c += 1
        if temp_r <= n and temp_c <= n:
            total_count += 1

    temp_r = r_q
    temp_c = c_q

    while temp_r > 0 and temp_c <= n:
        temp_r -= 1
        temp_c += 1
        if temp_r > 0 and temp_c <= n:
            total_count += 1

    temp_r = r_q
    temp_c = c_q

    while temp_r <= n and temp_c > 0:
        temp_r += 1
        temp_c -= 1
        if temp_r <= n and temp_c > 0:
            total_count += 1

    temp_r = r_q
    temp_c = c_q

    while temp_r > 0 and temp_c > 0:
        temp_r -= 1
        temp_c -= 1
        if temp_r > 0 and temp_c > 0:
            total_count += 1

    # obstacles2 = [[r_q, c_q], [r_q, c_q], [r_q, c_q], [r_q, c_q], [r_q, c_q], [r_q, c_q], [r_q, c_q], [r_q, c_q]]
    obstacles2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for obstacle in obstacles:
        r = obstacle[0]
        c = obstacle[1]
        if c_q == c:
            if r - r_q > 0:
                obs = obstacles2[0]
                if obs == [0, 0] or obs[0] > r:
                    obstacles2[0] = obstacle
            else:
                obs = obstacles2[4]
                if obs == [0, 0] or obs[0] < r:
                    obstacles2[0] = obstacle
        elif r_q == r:
            if c - c_q > 0:
                obs = obstacles2[2]
                if obs == [0, 0] or obs[1] > c:
                    obstacles2[2] = obstacle
            else:
                obs = obstacles2[6]
                if obs == [0, 0] or obs[1] < c:
                    obstacles2[2] = obstacle
        else:
            x = r - r_q
            y = c - c_q

            if abs(x) == abs(y):
                if x > 0:
                    if y > 0:
                        obs = obstacles2[1]
                        if obs == [0, 0] or x < obs[0] - r_q:
                            obstacles2[1] = obstacle
                    else:
                        obs = obstacles2[7]
                        if obs == [0, 0] or x < obs[0] - r_q:
                            obstacles2[7] = obstacle
                else:
                    if y > 0:
                        obs = obstacles2[3]
                        if obs == [0, 0] or x < obs[0] - r_q:
                            obstacles2[3] = obstacle
                    else:
                        obs = obstacles2[5]
                        if obs == [0, 0] or x < obs[0] - r_q:
                            obstacles2[5] = obstacle

    for obstacle in obstacles2:
        r = obstacle[0]
        c = obstacle[1]
        if r == r_q:
            if c_q > c:
                total_count -= c
            else:
                total_count -= (n - c + 1)
        elif c == c_q:
            if r_q > r:
                total_count -= r
            else:
                total_count -= (n - r + 1)
        else:
            x = r - r_q
            y = c - c_q

            if abs(x) == abs(y):
                if x > 0:
                    if y > 0:
                        if r > c:
                            total_count -= n - r + 1
                        else:
                            total_count -= n - c + 1
                    else:
                        if r > c:
                            total_count -= n - r + 1
                        else:
                            total_count -= n - c + 1
                else:
                    if y > 0:
                        if r > c:
                            total_count -= n - c + 1
                        else:
                            total_count -= n - c + 1
                    else:
                        if r > c:
                            total_count -= c
                        else:
                            total_count -= r
    # print(total_count)
    return total_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    n = 100

    k = 100

    # r_qC_q = input().split()

    r_q = 48

    c_q = 81

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    # fptr.write(str(result) + '\n')

    # fptr.close()
