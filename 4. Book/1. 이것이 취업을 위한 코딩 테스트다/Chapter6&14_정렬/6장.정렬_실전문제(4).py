# p.182 두 배열의 원소 교체

# n=원소의 개수, k=변경할 횟수
n, k = map(int, input().split())

# a와 b 리스트 생성
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, B는 내림차순으로 정렬해 원소를 k번 변경
a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    # a원소와 b원소 비교
    if a[i] < b[i]:
        a[i] ,b[i] = b[i], a[i]
    else:
        break

print(sum(a))