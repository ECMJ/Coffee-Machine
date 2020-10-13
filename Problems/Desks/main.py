#  Posted from EduTools plugin
# put your python code here
import math

class1 = int(input())
class2 = int(input())
class3 = int(input())

desk_group_1 = math.ceil(class1 / 2)
desk_group_2 = math.ceil(class2 / 2)
desk_group_3 = math.ceil(class3 / 2)

print(desk_group_1 + desk_group_2 + desk_group_3)
