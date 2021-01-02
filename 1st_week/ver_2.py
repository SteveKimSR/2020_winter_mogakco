#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # 1. 퀸에서 제일 가까운 8 방면의 기물 찾기.

    top = None
    top_right = None
    right = None
    bottom_right = None
    bottom = None
    bottom_left = None
    left = None
    top_left = None

    for obs in obstacles:
        r = obs[0]
        c = obs[1]
        if c == c_q:  # 퀸의 세로 선 상에 있을 시
            if r > r_q:  # 퀸 위
                if top is None:
                    top = obs
                else:
                    r_t, c_t = top
                    if r < r_t:
                        top = obs
            else:  # 퀸 아래
                if bottom is None:
                    bottom = obs
                else:
                    r_b, c_b = bottom
                    if r > r_t:
                        bottom = obs
        elif r == r_q:  # 퀸의 가로 선 상에 있을 시
            if c > c_q:  # 퀸 오른쪽
                if right is None:
                    right = obs
                else:
                    r_r, c_r = right
                    if c < c_r:
                        right = obs
            else:  # 퀸 왼쪽
                if left is None:
                    left = obs
                else:
                    r_l, c_l = left
                    if c > c_l:
                        left = obs
        else:
            y = r - r_q
            x = c - c_q
            if abs(y) == abs(x):
                if y > 0:  # 퀸 위쪽
                    if x > 0:  # 퀸 오른쪽 위
                        if top_right is None:
                            top_right = obs
                        else:
                            r_t_r, c_t_r = top_right
                            if r < r_t_r:
                                top_right = obs
                    else:  # 퀸 왼쪽 위
                        if top_left is None:
                            top_left = obs
                        else:
                            r_t_l, c_t_l = top_left
                            if r < r_t_l:
                                top_left = obs
                else:  # 퀸 아래쪽
                    if x > 0:  # 퀸 아래 오른쪽
                        if bottom_right is None:
                            bottom_right = obs
                        else:
                            r_b_r, c_b_r = bottom_right
                            if r > r_b_r:
                                bottom_right = obs
                    else:  # 퀸 아래 왼쪽
                        if bottom_left is None:
                            bottom_left = obs
                        else:
                            r_b_l, c_b_l = bottom_left
                            if r > r_b_l:
                                bottom_left = obs

    # 2. 퀸부터 거리 계산하기.
    total = 0
    total += top[0] - r_q - 1 if top is not None else n - r_q  # 위
    total += right[1] - c_q - 1 if right is not None else n - c_q  # 오른쪽
    total += r_q - bottom[0] - 1 if bottom is not None else r_q - 1  # 아래
    total += c_q - left[1] - 1 if left is not None else c_q - 1  # 왼쪽

    total += top_right[0] - r_q - 1 if top_right is not None else min(n - r_q, n - c_q)  # 오른쪽 위
    total += bottom_right[1] - c_q - 1 if bottom_right is not None else min(r_q - 1, n - c_q)  # 오른쪽 아래
    total += c_q - bottom_left[1] - 1 if bottom_left is not None else min(r_q - 1, c_q - 1)  # 왼쪽 아래
    total += top_left[0] - r_q - 1 if top_left is not None else min(n - r_q, c_q - 1)  # 왼쪽 위

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
