# Chapter 06. 정렬
: 연속된 데이터를 기준에 따라서 정렬하기 위한 알고리즘

- 정렬 알고리즘을 이용하여 데이터를 정렬한 후에, 이진 탐색(Binary Search)이 가능해짐
- 내림차순 정렬은 오름차순 정렬 후 리스트를 뒤집으면 됨!

### 선택 정렬(Selection Sort)

: 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸고, 그 다음으로 작은 데이터를 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 정렬

- 선택 정렬을 이용하는 경우가 잦기 때문에 형태에 익숙해질 필요 있음

```python
cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(cards)):
  min_index = i
  for j in range(i+1, len(cards)):
      if cards[min_index] > cards[j]:
          min_index = j
  cards[i], cards[min_index] = cards[min_index], cards[i]

print(cards) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 선택 정렬(Selection Sort)

: 특정 데이터를 적절한 위치에 ‘삽입’하는 과정을 통해 정렬

- 필요할 때만 위치를 바꾸기 때문에 데이터가 거의 정렬되어 있을 때 훨씬 효율적임
- 특정 데이터가 적절한 위치에 들어가기 전에, 그앞까지의 데이터는 이미 정렬되어 있다고 가정함
- 두 번째 데이터부터 정렬을 시작(첫 번째 데이터는 그 자체로 정렬되어 있다고 판단)

```python
cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(cards)):
	for j in range(i, 0, -1): #인덱스 i부터 1까지 감소하며 반복
    if cards[j] < cards[j-1]:
			cards[j], cards[j-1] = cards[j-1], cards[j]
		else:
			break # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
print(cards) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 퀵 정렬(Quick Sort)

: 특기준 데이터를 설정한 후 큰 수와 작은 수를 교환하여 리스트를 반으로 나누는 방식으로 정렬

- 언급된 정렬 알고리즘 중 가장 많이 사용되는 알고리즘
- 피벗(Pivot) = 큰 숫자와 작은 숫자를 교환할 때 사용하는 기준
- 일반적인 경우에서 평균적으로 빠르게 동작하므로 데이터의 특성을 파악하기 어렵다면 유리
- 데이터가 이미 정렬되어 있는 경우에는 매우 느리게 동작함 
→ 기본 정렬 라이브러리를 이용하면 
최악의 경우에도 시간 복잡도가 O(NlogN)이 되는 것을 보장할 수 있음

```python
cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end: # 원소가 1개인 경우 종료
		return
	pivot = start # 피벗은 첫번째 원소
	left = start+1
	right = end
	while left <= right:
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] <= array[pivot]:
				left += 1
		# 피벗보다 작은 데이터를 찾을 때까지 반복
		while right > start and array[right] >= array[pivot]:
				right -= 1
		if left > right: # 엇갈린다면 작은 데이터와 피벗을 교체
				array[right], array[pivot] = array[pivot], array[right]
		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
				array[left], array[pivot] = array[pivot], array[left]
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
	quick_sort(arrays, start, right - 1)
	quick_sort(array, right+1, end)

quick_sort(cards, 0, len(cards) - 1)
print(cards) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

파이썬의 장점을 살린 퀵 정렬 소스코드는 아래와 같음

```python
cards = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
	# 리스트가 하나 이하의 원소만을 담고 있다면 종료
	if len(array) <= 1:
		return array

	pivot = array[0] # 피벗은 첫번째 요소
	tail = array[1:] # 피벗을 제외한 나머지 리스트

	left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
	right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(cards)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 계수 정렬(Count Sort)

: 최댓값과 입력 배열의 원소 값 개수를 누적합으로 구성한 배열로 정렬을 수행

- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용할 수 있음
- 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적
- 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합함

```python
cards = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값을 0으로 초기화)
count = [0] * (max(cards) + 1)

# 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(cards):
	count[cards[i]] += 1

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
	for j in range(count[i]):
		print(i end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
		# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```

### 파이썬의 정렬 라이브러리 - sorted()
: 퀵 정렬과 유사한 ‘병합 정렬’을 기반으로 만들어짐 - 최악의 경우에도 시간 복잡도 O(NlogN) 보장

- 리스트 또는 딕셔너리 자료형 등을 입력 받아서 정렬된 결과를 출력함
