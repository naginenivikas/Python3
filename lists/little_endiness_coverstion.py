# !/usr/bin/python3
# -*- coding: UTF8 -*-
import re

def endiness_converter(value):
    return value.split(':')[::-1]

print(':'.join(endiness_converter("AA:BB:CC:DD:EE:FF")))
