import math

def calculate_square_area(side):
  return side ** 2

def calculate_rectangle_area(length, width):
  return length * width

def calculate_triangle_area(base, height):
  return (base * height) / 2

def calculate_circle_area(radius):
  return math.pi * radius ** 2

def main():
  print("==================")
  print("Area Calculator 📐")
  print("==================")
  print("1) Triangle")
  print("2) Rectangle")
  print("3) Square")
  print("4) Circle")
  print("5) Quit")

  choice = input("Which shape: ")

  if choice == '1': # Triangle
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = calculate_triangle_area(base, height)
  elif choice == '2': # Rectangle
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = calculate_rectangle_area(length, width)
  elif choice == '3': # Square
    side = float(input("Side: "))
    area = calculate_square_area(side)
  elif choice == '4': # Circle
    radius = float(input("Radius: "))
    area = calculate_circle_area(radius)
  elif choice == '5': # Quit
    return
  else:
    print("Invalid choice.")
    return

  print(f"The area is {area}")

if __name__ == "__main__":
  main()
