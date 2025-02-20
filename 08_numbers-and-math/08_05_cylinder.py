# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

PI = 3.1415925
radius = 3.14
height = 5

volume = PI * radius**2 * height
surface_area = 2 * PI * radius * (height + radius)

print("Volume =", volume)
print("Surface Area =", surface_area)
