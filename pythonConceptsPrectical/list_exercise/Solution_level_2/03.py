# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# -> Unpack the first three countries and the rest as scandic countries.

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

#method 1
tuple(countries)

(c1,c2,c3,*rest) = countries

print(c1)
print(c2)
print(c3)
print(rest)



#method 2
first_three_countries, *scandinavian_countries = countries[:3], countries[3:]

print("First three countries:", first_three_countries)
print("Scandinavian countries:", scandinavian_countries)
