# 4-1. 상하좌우


n = int(input())

moves = input().split()


def solution(moves, n):
    x, y = 1, 1

    # L(eft), R(ight), U(p), D(own)
    directions = ["L", "R", "U", "D"]

    dx = [0, 0, -1, 1]  # x축 좌우 이동
    dy = [-1, 1, 0, 0]  # y축 상하 이동

    for move in moves:

        # 이동 방향 확인
        for i in range(0, 4):
            if move == directions[i]:

                # 이동 후, 공간 안에 있는지 확인

                if (x + dx[i] >= 1 and x + dx[i] <= n) and (y + dy[i] >= 1 and y + dy[i] <= n):
                    x = x + dx[i]
                    y = y + dy[i]


    print(x, y)


solution(moves, 5)
