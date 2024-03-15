# 1. The following is a list of 10 students ages:
#    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# -> Sort the list and find the min and max age
# -> Add the min age and the max age again to the list
# -> Find the median age (one middle item or two middle items divided by two)
# -> Find the average age (sum of all items divided by their number )
# -> Find the range of the ages (max minus min)
# -> Compare the value of (min - average) and (max - average), use abs() method


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

min_age = ages[0]
max_age = ages[-1]


ages.append(min_age)
ages.append(max_age)


length = len(ages)
middle = length // 2
if length % 2 == 0:
    median_age = (ages[middle - 1] + ages[middle]) / 2
else:
    median_age = ages[middle]
    
    

sum_ages = sum(ages)
average_age = sum_ages / length



range_ages = max_age - min_age



diff1 = abs(min_age - average_age)
diff2 = abs(max_age - average_age)
if diff1 > diff2:
    print("The max age is closer to the average")
else:
    print("The min age is closer to the average")