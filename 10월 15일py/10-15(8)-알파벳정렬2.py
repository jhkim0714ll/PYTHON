arr=['t','b','c','k','u','w']

arr.sort()

print(arr[0],arr[len(arr) - 1]) # 자료 중 아스키 코드값이 가장 작은 알파벳 출력

arr.sort(reverse=True) # 역 방향 정렬
print(arr)