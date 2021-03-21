def cud():
    print("AREA OF CUBOID")
    length = int(input('Please Enter the Length of a Cuboid: '))
    width = int(input('Please Enter the Width of a Cuboid: '))
    height = int(input('Please Enter the Height of a Cuboid: '))
    SA = 2 * (length * width + length * height + width * height)
    Volume = length * width * height
    print("\n The Surface Area of a Cuboid = %.2f " %SA)
    print(" The Volume of a Cuboid = %.2f" %Volume)
