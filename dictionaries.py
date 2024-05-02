
my_dict={
    "name":"kim",
    "gender":"male",
    "age":4,
    "address":["kajiado",254,"ngong"]
}
# accessing values using keys
print(my_dict["name"])
print(my_dict["gender"])
print(my_dict["age"])
# display 254
print(my_dict["address"][1])

# modifying values
my_dict["age"]=30
my_dict["name"]="Ronnie"

# adding key value to a dictionary
# id
my_dict["id"]=42436754
my_dict["other"]={"occupation":"software developer",
         "specification":["front end developer","graphic disigner"]}
print(my_dict.keys())