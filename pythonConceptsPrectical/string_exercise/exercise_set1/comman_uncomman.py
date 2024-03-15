"""
Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : ['Learning', 'from']

Input : A = “apple banana mango” , B = “banana fruits mango”
Output : ['apple', 'fruits']

"""

txt = "Python is Programming Language"
txt1 = "java is Oops language"

c_list = []

alist = txt.lower().split()
blist = txt1.lower().split()

for i in range(len(alist)):
    if alist[i] in blist:
        c_list.append(alist[i])

print("Comman Elements is : ",c_list)


#method 2
# def find_common(A,B):
#     # convert string to list of words
#     aList = A.split()
#     bList = B.split()
#     # create an empty result list
#     commonWords = []
#     # iterate over the first list and add common word in both lists to the result list
#     for i in range(len(aList)):
#         if aList[i] in bList:
#             commonWords.append(aList[i])
#     return commonWords

# print(find_common(txt.lower(), txt1.lower()))