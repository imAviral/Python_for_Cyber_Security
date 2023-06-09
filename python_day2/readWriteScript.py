read_file = open(fileName, "r")
write_file = open(fileName, "a")
# read a file
print(read_file.read())

# read a file line
readLine = read_file.readlines()
print(readLine[1])

# write in file
write_file.write(data)
write_file.close()