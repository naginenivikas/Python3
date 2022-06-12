# !/usr/bin/python3
# -*- coding: UTF8 -*-

# =========================================================================
#         
#   def fun(pos_args, /, combined_args, *, keyword_args)
#  
#   def fun(username, password, /, email, name="blank", age=24, *, experience="Fresher", Gender="Male")
# 
# ========================================================================

details = {}
bio = {}
def fun(username, password, /, email, name='blank', age=24, *, experience="Fresher", Gender="Male"):
    bio = {}
    if username not in details.keys():
        bio = {'pwd': password, "mail": email, "name": name, "age": age, "exp": experience, "gen": Gender}
        details[username] = bio
        print("\n\"{}\" User Added Successfully to data base\n".format(username))
        return True
    if details[username]['pwd'] == password:
        print("\nUser \"{}\" exists in data base\n=======================================================\nYour details :\n \
                \tName\t\t: {}\n\
                \temail\t\t: {}\n\
                \tAge\t\t: {}\n\
                \tGender\t\t: {}\n\
                \tExperience\t: {}\n".format(username, 
                                        details[username]['name'], details[username]['mail'], 
                                        details[username]['age'], details[username]['exp'], details[username]['gen']))
    else:
        print("\n\"{}\" date entry found in data base,\n\tPlease provide correct password to see your details\n".format(username))

fun("vikasnagineni", "demo@123", "vikas.nagineni@gmail.com", name="Vikas", age=26)
# fun("Vikas Nagineni", "demo@123", "vikas.nagineni@gmail.com", name="Vikas", age=26)
for iteration in range(5):
    username, password, email, nm, age, exp, gen = input("Enter User-Name, Password, bio details with comma seperated: ").strip().split(',')
    fun(username, password, email, name=nm, age=age, experience=exp, Gender=gen)