# !/usr/bin/python3
# -*- coding: UTF8 -*-

# center(length_of_new_string, "character")

print("{}".format("=")*60)

print("\t \"center(new_str_len, charcter)\"\n")

name = "VIKAS NAGINENI"

print("center({}, \"{}\") for {} : {}".format(str(len(name)+8), "*", name, name.title().center(len(name)+8, "*")))

print("{}".format("=")*60)