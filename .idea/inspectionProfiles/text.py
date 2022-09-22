courses_file = open("requiredCS (1).txt", 'r')
lines_from_file = courses_file.readlines()
for line in lines_from_file:
    loud_line = line.upper()
    split = line.split(":")
#    loud_line = loud_line.strip()
    print(split[0])
    print(split[1])
print("those are thew classes you HAVE to take for the CS Major")