# Write
f = open("file.txt", "w")
f.write("Hello")
f.close()

# Read
f = open("file.txt", "r")
print(f.read())
f.close()

# Append
f = open("file.txt", "a")
f.write("\nNew Line")
f.close()
