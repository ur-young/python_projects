# p.178 위에서 아래로
# 수열을 내림차 순으로 정렬 하는 프로그램

number = int(input())

list = []
for i in range(number):
    list.append(int(input()))

list = reversed(sorted(list))
# list = sorted(array, reverse=True)

for i in list:
    print(i, end=' ')