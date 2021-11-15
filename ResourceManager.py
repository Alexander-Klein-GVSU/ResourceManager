import Process
import Resource

file = open("upload.txt", "r")

input = file.readline(0)
processes = int(input)

input = file.readline(1)
input = input.split(" ")
resources = input[0]

for i in range(1, resources):
    resource[i-1] = Resource(input[i])

for i in range(processes):
    process[i] = Process(resources)

lineCt = len(file.readlines)
for i in range(2, lineCt):
    input = file.readline(i)
    input = input.split(" ")
    if (input[0] == "request"):
        temp = i
    elif (input[0] == "release"):
        temp = i
    else:
        print("Error: Invalid Command")
        
file.close()