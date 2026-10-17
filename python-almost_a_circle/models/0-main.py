#!/usr/bin/python3
from models.base import Base

b1 = Base()
print(b1.id)   # 1
b2 = Base(12)
print(b2.id)   # 12
b3 = Base()
print(b3.id)   # 2
