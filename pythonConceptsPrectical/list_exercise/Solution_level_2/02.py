# 2. Find the middle country(ies) in the countries list
# countries = [
#     'Afghanistan','Albania','Algeria','Andorra', 'Angola', 'Antigua and Barbuda','Argentina','Armenia','Australia','Austria',
#     'Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina',
#     'Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada', 'Cape Verde','Central African Republic',
#     'Chad','Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba', 'Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic'
# ];
# -> Divide the countries list into two equal lists if it is even if not one more country for the first half.


countries = [
    'Afghanistan','Albania','Algeria','Andorra', 'Angola', 'Antigua and Barbuda','Argentina','Armenia','Australia','Austria',
    'Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina',
    'Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada', 'Cape Verde','Central African Republic',
    'Chad','Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba', 'Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic'
];

total_countries = len(countries)

x = total_countries // 2

print(countries[x])

first_half = countries[:x + total_countries % 2]
second_half = countries[x + total_countries % 2:]

print("First Half:", first_half)
print("Second Half:", second_half)
