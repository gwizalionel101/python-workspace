import math
print("this program convert polar coordinate to cartesian")
radius=float(input("enter the distance between  origin (radius)--->>>>      "))
adeg=int(input("provide the positive angle from x--->>>>      "))
arad=math.radians(adeg)
x=radius*math.cos(adeg)
y=radius*math.sin(adeg)
print(f"the cartesian coordinates are:>>>    (f"{x:.3}")  and  {f"{y:.2}\n simply ==>>")