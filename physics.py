import numpy as np
r=float(input("provide your positon coordinate:"))
theta=float(input("provide the angle:"))
thetar=np.radians(theta)
x=r*np.cos(thetar)
y=r*np.sin(thetar)
print(f"Given r = {r} and theta = {theta} degrees\nThen Cartesian coordinates are ({x:.2f}, {y:.2f})")
