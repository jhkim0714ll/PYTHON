import random

arr = list() #arr을 리스트로 선언
#arr = [] #arr을 리스트로 선언
print(arr)

for i in range(6):
    arr.append(random.randint(1,46))
print(arr)
arr.sort(reverse=True)
print(arr[1])