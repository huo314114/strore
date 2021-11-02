# a = [1,2,3,4,5,6,7,8,9]
# def reverse_list(n:list)->list:
#     d =dict(zip([i for i in range(len(n))],n))
#     return [d[k] for k in sorted(d,reverse=True)]
# print(reverse_list(a))

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b1, b2 = 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, ]
while b1 < 9:
    b2[b1] = b[-b1 - 1]
    b1 += 1
print(b2)
b2 = list(reversed(b))
print(b2)