# arr=[5,4,8,3]
# arr.sort() #배열의 내용 변경
# print(arr)

# arr1=[5,4,8,3]
# print(sorted(arr1)) #배열의 변경 없음
# print(arr1)

# arr2=['김철수','박효신','BTS','이문세']
# print(sorted(arr2))
# print(sorted(arr2,reverse=True))

arr3=['banana','apple','pinapple','pear','peach']
print(sorted(arr3,key=len))