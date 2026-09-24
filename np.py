import np as np

# arr=nump.array([
#     [[1,2,3],[2,3,4]],
#     [[6,9,8],[4,6,8]]
#     ])

# print(np.ndim(arr))


arr=np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2=np.array([[1],
              [2],
              [3],
              [4],
              [5],
              [6],
              [7],
              [8],
              [9],
              [10]
              ])
print(arr.shape)
print(arr2.shape)
print(arr*arr2)


# fliter  topic

import np as np

age=np.array([[12,34,56,78,45,43,65],
              [34,18,12,16,74,84,26]])
    
print(age)    
print()

    
adults=age[age>18]
print(adults)
print()

senior=age[age>60]
print(senior)
print()

teen=age[age>18]
print(teen)
              