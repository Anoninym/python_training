first_name = "    rONNIE  "
last_name = "    KIM"

# f
# first_name = first_name.strip()
# first_name = first_name.title()
# #print(first_name)
# last_name = last_name.lstrip()
# last_name = last_name.title()
# #print(last_name)
# full_name = first_name + " " + last_name
# print(full_name)
# (len(first_name)) == True

# email = 'ronnkim@gmail.com'
# print(email.count("@") == 1)
# st = "This is my book"
# print(type(st.split(" ")))
# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_one = "The Dog Breed is German Shepherd"
sentence_one = sentence_one[8:23]
print(sentence_one)
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
sentence_two = sentence_two[16:30]
print(sentence_two)
# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “C.” 
s = " The lazy dog; ran so fast; it hit the wall."
result = s.split(";")
print(result)
print("lenght is:", len(result))
# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="  Joh.n"  
last_name="   Do,e"
first_name = first_name.strip().capitalize().replace(".", "")
last_name = last_name.strip().capitalize().replace(",", "")
full_name = first_name + " " + last_name
print(full_name)
# Having the string r = '["E","W","C"]' Manipulate it to display EWC
r = '["E","W","C"]'
r_m = "".join(r.replace('[', "").replace(']', "").replace('"', "").split(",") )
print(r_m)
# t
name = "John Doe"
print(name[5:8])
# s
name = "John Doe"
print(name[::1])



