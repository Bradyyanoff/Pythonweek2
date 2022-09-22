courses_file = open("requiredCS (1).txt", 'r')
lines_from_file = courses_file.readlines()
for line in lines_from_file:
    print(line)