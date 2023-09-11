def square_num(n):
    return n*n
nums=[5,6,8,2,4]
print("original list:",nums)
result = map(square_num,nums)
print("square the elements of list using map():")
print(list(result))