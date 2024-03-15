#break:  to break out of a loop
#continue: to skip the rest of the code in the current iteration and move/continue on to the next iteration of a loop


for i in range(9):
    if i > 3:
        break
    print(i)

#the break keyword is used to break out a for loop, or a while loop

i = 1
while i < 9:
    print(i)
    if i == 3:
        break
    i += 1


#the continue is used to continues to the next iteration