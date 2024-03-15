#1. copy array to another arry
# arr = [0,1,2,3,4,5,6]
# copyArry = [None]*len(arr)

# for i in range(0, len(arr)):
#     copyArry[i] = arr[i]

# print("Elements of the original array : ")
# for i in range(0,len(arr)):
#     print(arr[i], end=" ")
# print()

# print("Elements of the new array : ")
# for i in range(0,len(copyArry)):
#     print(copyArry[i],end=" ")




#2. Find Third and Second largest element
# arr = [25,11,7,75,56]
# arr2 = [1,2,5,6,3,2]

#function to get third largest
# def TL(arr,total):
#     for i in range(total):
#         for j in range(i+1,total):
#             if arr[i] > arr[j]:
#                 tmp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = tmp

#     return arr[total-3]

# def SL(arr,total):
#     for i in range(total):
#         for j in range(i+1,total):
#             if arr[i] > arr[j]:
#                 tmp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = tmp
#     return arr[total-2]



# print("The third largest element in arr is:", TL(arr, 5))
# print("The third largest element in arr2 is:", TL(arr2, 6))
# print("The Second largest element in arr is:", SL(arr, 5))
# print("The Second largest element in arr2 is:", SL(arr2, 6))




# 3.marge two arrays
# import array
# arr1 = array.array('i',[0,1,2,4,5,6,7,8,9,10])
# arr2 = array.array('i',[40,50,16,18,90])

# arra3 = array.array('i')
# arra3 = arr1 + arr2
# print("The new created array is : ", arra3)





#4 Print two common elements 
# import array
# arr1 = array.array('i',[0,1,2,4,5,16,7,18,90,10])
# arr2 = array.array('i',[40,50,16,18,90])

# print("The common elements are : ")
# for i in arr1:
#     for j in arr2:
#         if i in arr1 and i in arr2:
#             arr1.remove(i)
#             print(i, end=" ")





#5 print duplicate array
# arr = [1,2,4,5,5,3,2,1,5,6,8]
# print("Duplicate elements in giving array")
# for i in range(0,len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j]:
#             print(arr[j])





#Odd even position elemets
# arr = [1,2,3,4,5,6,7,8,9,10]
# print("Even Position")
# for i in range(1, len(arr), 2):
#     print(arr[i], end=" ")
# print()

# print("Odd position")
# for i in range(0, len(arr), 2):
#     print(arr[i],end=" ")




#sum of array
# arr = [1,5,1,2,3,45,60]
# sum = 0
# for i in range(0,len(arr)):
#     sum += arr[i]

# print("sum is : ",sum)




#reverse array without built-in function
# import array
# a1 = array.array('i',[0,1,2,3,4,5,6,7])
# print("Original array is : ", a1)
# print("Reverse array is : ",end=" ")
# for i in range(len(a1)-1,-1,-1):
    # print(i,end=" ")

#asseding or decending order array
# arr = [5, 2, 8, 7, 1]
# temp = 0
# print("Elements of original array: ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")

# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > arr[j]:
#             tmp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = tmp
# print()

# print("Elements of array sorted in ascending order: ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")


# arr = [5, 2, 8, 7, 1]
# temp = 0
# print("\nElements of original array: ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")

# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] < arr[j]:
#             tmp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = tmp
# print()

# print("Elements of array sorted in decending order: ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")





