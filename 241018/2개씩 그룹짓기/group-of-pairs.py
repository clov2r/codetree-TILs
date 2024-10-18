n = int(input()) # 그룹의 수 N을 입력 받음
n_list = list(map(int, input().split())) # 2 * N개의 숫자를 입력받고, 이를 리스트로 변환
n_list2 = sorted(n_list)
x = []

# N개의 그룹을 만들기 위해 작은 숫자와 큰 숫자를 짝지어 그룹의 합을 구함
for i in range(n):
    # i번째 작은 숫자와 i번째 큰 숫자를 더한 값을 리스트 x에 추가
    x.append(n_list2[i] + n_list2[-(i+1)])

# 각 그룹의 합 중 최댓값을 출력
print(max(x))