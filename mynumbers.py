# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
import math

temp = 56.8926
temp2 = math.ceil(temp)
print(temp2)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89
temp = 56.8926
temp4 = round(temp, 2)
print(temp4)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926
temp5 = round(temp, 3)
print(temp5)

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926
temp=56.8926
temp6 = str(temp)
temp6 = temp6[3:]
temp6 = float(temp6)
temp6 = temp6 / 1000
print(temp6)
# fhfgg








