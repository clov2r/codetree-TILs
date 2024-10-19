n, m = map(int, input().split())
n_list = [0] * n  # 각 칸의 블록 개수를 저장하는 리스트

for i in range(m):
    x, y = map(int, input().split())
    # x번 칸부터 y번 칸까지 블록을 쌓아야 함
    for j in range(x-1, y):  # x-1부터 y-1까지 인덱스 범위에 블록을 추가
        n_list[j] += 1  # 블록을 덮어쓰지 않고 더해줌

# 최대 블록 수 출력
print(max(n_list))