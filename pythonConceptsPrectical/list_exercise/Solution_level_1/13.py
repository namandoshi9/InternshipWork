# 13. Change one of the it_companies names to uppercase (IBM excluded!)


it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
print(it_companies)
        
        
