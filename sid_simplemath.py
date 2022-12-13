# This program will do simple math.



# Import the math module
import math

# Menu for the area calculator
def choose_area_shape():
    print("What shape would you like to calculate the area of?")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Parallelogram")
    print("6. Trapezium")
    print("7. Ellipse")
    print("8. Sector")
    print("9. Regular Polygon")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        circle_area()
    elif choice == "2":
        rectangle_area()
    elif choice == "3":
        triangle_area()
    elif choice == "4":
        square_area()
    elif choice == "5":
        parallelogram_area()
    elif choice == "6":
        trapezium_area()
    elif choice == "7":
        ellipse_area()
    elif choice == "8":
        sector_area()
    elif choice == "9":
        polygon_area()
    elif choice == "0":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice")
        choose_area_shape()


# Menu for the volume calculator
def choose_volume_shape():
    print("What shape would you like to calculate the volume of?")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Sphere")
    print("5. Cone")
    print("6. Pyramid")
    print("7. Regular Prism")
    print("8. Regular Pyramid")
    print("9. Regular Frustum")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        cube_volume()
    elif choice == "2":
        cuboid_volume()
    elif choice == "3":
        cylinder_volume()
    elif choice == "4":
        sphere_volume()
    elif choice == "5":
        cone_volume()
    elif choice == "6":
        pyramid_volume()
    elif choice == "7":
        prism_volume()
    elif choice == "8":
        pyramid_volume()
    elif choice == "9":
        frustum_volume()
    elif choice == "0":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice")
        choose_volume_shape()

# Area Functions
def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is: ", area)

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is: ", area)

def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is: ", area)

def square_area():
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    print("The area of the square is: ", area)

def parallelogram_area():
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    area = base * height
    print("The area of the parallelogram is: ", area)

def trapezium_area():
    base1 = float(input("Enter the first base of the trapezium: "))
    base2 = float(input("Enter the second base of the trapezium: "))
    height = float(input("Enter the height of the trapezium: "))
    area = 0.5 * (base1 + base2) * height
    print("The area of the trapezium is: ", area)

def ellipse_area():
    a = float(input("Enter the first semi-major axis of the ellipse: "))
    b = float(input("Enter the second semi-major axis of the ellipse: "))
    area = math.pi * a * b
    print("The area of the ellipse is: ", area)

def sector_area():
    radius = float(input("Enter the radius of the sector: "))
    angle = float(input("Enter the angle of the sector: "))
    area = 0.5 * radius ** 2 * angle
    print("The area of the sector is: ", area)

def polygon_area():
    n = float(input("Enter the number of sides of the polygon: "))
    s = float(input("Enter the length of each side of the polygon: "))
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    print("The area of the polygon is: ", area)

# Volume Functions
def cube_volume():
    side = float(input("Enter the side of the cube: "))
    volume = side ** 3
    print("The volume of the cube is: ", volume)

def cuboid_volume():
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    volume = length * width * height
    print("The volume of the cuboid is: ", volume)

def cylinder_volume():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = math.pi * radius ** 2 * height
    print("The volume of the cylinder is: ", volume)

def sphere_volume():
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4 / 3) * math.pi * radius ** 3
    print("The volume of the sphere is: ", volume)

def cone_volume():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    volume = (1 / 3) * math.pi * radius ** 2 * height
    print("The volume of the cone is: ", volume)

def pyramid_volume():
    base = float(input("Enter the base of the pyramid: "))
    height = float(input("Enter the height of the pyramid: "))
    volume = (1 / 3) * base * height
    print("The volume of the pyramid is: ", volume)

def prism_volume():
    base = float(input("Enter the base of the prism: "))
    height = float(input("Enter the height of the prism: "))
    volume = base * height
    print("The volume of the prism is: ", volume)

def frustum_volume():
    base1 = float(input("Enter the first base of the frustum: "))
    base2 = float(input("Enter the second base of the frustum: "))
    height = float(input("Enter the height of the frustum: "))
    volume = (1 / 3) * (base1 + base2) * height
    print("The volume of the frustum is: ", volume)


# This function will have a fancy splash screen with  ascii art.
# This function will also have a numerical menu with options to choose from.
# The user will also be able to choose an option by typing the name of the option as well as the number.
# The user will be able to exit the program by typing "exit" or "quit" or "0".

def main():
    # Splash screen with border
    print("=============================================")
    print("|   Welcome to the Geometry Calculator!     |")
    print("=============================================")
    print("Choose what you want to calculate:")
    print("1. Area")
    print("2. Volume")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        choose_area_shape()
    elif choice == "2":
        choose_volume_shape()
    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice")
        main()

main()