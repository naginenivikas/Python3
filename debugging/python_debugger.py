# !/usr/bin/python3
# -*- coding: UTF8 -*-

import pdb

# pdb is a module used for debugging

class Phone:
    def __init__(self, name, version, price):
        self.name = name
        self.version = version
        self._price = price
    
    def fullname(self):
        return f"{self.name} {self.version}"

class SmartPhone(Phone):
    def __init__(self, name, version, price, btry_cap, f_cam, r_cam, ram):
        Phone.__init__(name, version, price)
        self.battery = btry_cap
        self.front_cam = f_cam
        self.rear_cam = r_cam
        self.ram = ram
    
    def full_spec(self):
        #full_name = f"{self.name}_{self.version}"
        return f"Name\t: \n \
            Price\t: {self.price} \n \
                Battery\t: {self.battery} \n \
                    Camera\t: front {self.front_cam} rear {self.rear_cam}\n \
                        Ram\t: {self.ram}"

# pdb.set_trace()
# Obj = SmartPhone('Samsung', 'M30s', '250000', '6000 MAh', '12 MP', '64 MP', '8GB')
Obj = Phone('Samsung', 'M30S', "20000")
print(help(Obj.fullname))