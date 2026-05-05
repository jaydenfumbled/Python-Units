try:
    name = input("Enter filename: ")
    f = open(name, "r")
    print(f.read())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")
