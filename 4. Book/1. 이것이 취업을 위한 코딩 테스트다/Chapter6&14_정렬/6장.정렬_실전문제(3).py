# p.180 성적이 낮은 순서로 학생 출력하기

n = int(input())

# 학생 정보를 입력받아 리스트에 저장(이름, 점수)
data = []
for i in range(n):
    tmp = input().split(' ')
    # 이름은 그대로, 점수는 정수형으로 변환하여 저장
    data.append((tmp[0], int(tmp[1])))

# 키(Key)를 이용하여 점수를 기준으로 정렬
data = sorted(data, key = lambda score: score[1])

for i in data:
    print(i[0], end=' ')