# !/usr/local/bin/python3
# -*- coding: UTF8 -*-
 
# replace(searched, to_be_replaced, no of replacements)
print("{}".format("=")*60)

print("\t \"replace(to_be_srch, replaces_with, no_of_replacements)\"\n")

string = "PY is an interperter and PY is simple to learn. Today will be same day as next day."

# Replace all occurance of string
print("replace(\"{}\", \"{}\",  ) for String : {}".format("PY", "Python", string.replace("PY", "Python")))  

# Replace only one occurance of string 
print("replace(\"{}\", \"{}\", {}) for String : {}".format("PY", "Python", str(1), string.replace("PY", "Python", 1)))

# Replaces Today with bright day because of day occurance.
print("replace(\"{}\", \"{}\",  ) for String : {}".format("day", "bright day", string.replace("day", "bright day")))

print("{}".format("=")*60)
print("\t \"find(to_be_searched, srch_index_pos)\"\n")
print("{}".format("=")*60)

# find(to_be_searched, search_Index_start)

print("find(\"{}\",  ) for String : {}".format("PY", string.find("PY")))
print("find(\"{}\", {}) for String : {}".format("PY", str(5), string.find("PY", 5)))
print("{}".format("=")*60)