n = int(input())  # n개의 숫자를 입력받음
n_list = list(map(int, input().split()))  # n개의 숫자 리스트로 변환

# 홀수 번째 원소를 처리하기 위해 리스트를 순회하며, 매 홀수 번째 시점마다 중앙값을 출력
for i in range(1, n + 1, 2):  # 홀수 번째 원소에 대해 반복
    current_list = n_list[:i]  # 지금까지의 원소들 중 첫 i개의 원소를 잘라냄
    current_list.sort()  # 중앙값을 구하기 위해 정렬
    median = current_list[len(current_list) // 2]  # 중앙값 계산
    print(median, end=" ")  # 중앙값을 출력 (공백으로 구분)