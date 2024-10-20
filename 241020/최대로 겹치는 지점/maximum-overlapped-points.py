n = int(input())
x_list = [0] * 100
for i in range(n):
    x, y = map(int, input().split())
    # 선분의 끝점 x2는 포함하지 않으므로 x부터 y-1까지만 처리
    for j in range(x-1, y):  # 인덱스를 100 더해 양수로 변환
        x_list[j] += 1

# 가장 많이 겹치는 구간에서의 겹치는 선분 수 출력
print(max(x_list))