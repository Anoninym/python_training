# Print KES
# 2. Print 560
# 3. Print Maths
# 4. In the dictionary with the key currency, add another key “amount” with value 90
# 5. 
 

my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
print(my_ds[3][2]["currency"])
print(my_ds[3][1])
my_ds[3][2]["amount"]=90
# print(my_ds)
# Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
# converting it to a string
reve=str(my_ds[4])
# reversing
reve=reve[::-1]
# converting it back to an integer
reve=int(reve)
# updating the dictionary
my_ds[4]=reve
# print(my_ds)
# 6. Change the name “John” to “Jane” .
y=list(my_ds[5])
y[1]="jane"
y=tuple(y)
my_ds[5]=y
print(my_ds)


