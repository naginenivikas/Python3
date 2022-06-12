# !/usr/bin/Python3
# -*- coding: UTF8 -*-

#=======================================================================
#
#         def function_name(positional_args, KwArgs)
# 
#         def f(info, name='vikas nagineni', age=26, Position="Senior Software Engineer")
# 
#=======================================================================

def emp(info, name="vikas nagineni", age=26, Position="Senior Soft Engineer"):
    print("\"Employee details\"\n===================================================================\n\
            \tName\t\t: {}\n\
            \tAge\t\t: {}\n\
            \tPosition\t: {}\n\
            \tInformation\t: {}\n".format(name, age, Position, info))

def new_emp(name, *info, **bio):
    print("\"Employee Details\":\n=====================================================================\n\
        \tName\t\t: {}\n\
        \tInfo\t\t: {}\n\
        \tbio\t\t: {}\n".format(name.title(), info, bio))

emp("I am Engineer working at Capgemini Software LTD")
emp(name="Theja Nagineni",info = "I am Engineer working at Infosys Software LTD", age=24, Position="Junior Soft Engineer")
emp(name="Yeshu Nagineni",info = "I am Engineer working at Infosys Software LTD", age=24)

# emp(name="Prakruth", age=2) # -> required positional argument.

#=======================================================================
#
#         def function_name(positional_args, *tuple, **dictionary)

#         def fun(arg, names=(), dict={})
# 
#         def f(name, *info, **bio")
# 
#=======================================================================

new_emp("ViKaS nAGiNenI", "I completed my btech from SVNE", 
",From IT departement", 
Age=24, Gender="Male", experience="2'Yrs as Embeeded Engineer")

# new_emp(only positional argunment)  -> new_emp(name=vikas) reads as keyword argunmnet