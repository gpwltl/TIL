```python
def quick_sort(array, start, end):
  if start>=end:	#원소가 1개면 종료
    return 
  pivot=start		#피벗은 첫번째 원소
  left=start+1
  right=end

  while(left<=right):	#엇갈리지 않는 상황에서 while문 진행..
    while(left<=end and array[left]<=array[pivot]):	#피벗보다 큰 데이터 찾을 때까지 반복(왼쪽부터)
      left += 1
    while(right>start and array[right]>=array[pivot]):	#피벗보다 작은 데이터 찾을 때까지 반복(오른쪽부터)
      right -= 1
    if(left > right):	#엇갈렸다면, 작은 데이터와 피벗 교체
      array[right], array[pivot] = array[right], array[right]
    else: 	#엇갈리지 않았다면, 작은 데이터와 큰 데이터 교체
      array[left], array[pivot] = array[right], array[left]

  #분할 후 왼쪽, 오른쪽 각각 정렬 수행(재귀함수)
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
```

