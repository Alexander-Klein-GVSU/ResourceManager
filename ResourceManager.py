import copy
import GUI

# Name: Alexander Klein
# Date: 11/15/21
# Assignment: Resource Manager

#Deadlock Checker Function
def checker(has, want, available):
    #Initializes internal values.
    availC = copy.deepcopy(available)
    finished = [False for i in range(len(has))]
    runnable = True
    rl = 0

    #While processes can be completed.
    while (runnable):
        runnable = False
        #Checks for an unfinished Process.
        for i in range(len(has)):
            if (finished[i] == False):
                #Checks if the resources are available to the process.
                canHaveAll = 0
                for j in range(len(has[i])):
                    if (availC[j] >= want[i][j]):
                        canHaveAll += 1
                #If they are, it releases all of the resources in it, 
                #sets the process as finished, and
                #adds the process to the runOrder.
                if (canHaveAll == len(has[i])):
                    for j in range(len(has[i])):
                        availC[j] += has[i][j]
                    finished[i] = True
                    runnable = True
                    runOption[rl] = i
                    rl += 1
    #If all processes can be finished, it returns no dl.
    totalF = 0
    for i in (range(len(finished))):
        if (finished[i] == True):
            totalF += 1
    if (totalF == len(finished)):
        return False
    else:
        return True

#Opens the file.
file = open("upload.txt", "r")
input = file.read()
input = input.split('\n')

i = 0
for l in input:
    input[i] = l.split(' ')
    i += 1

#Gets the number of processes.
processes = int(input[0][0])

#Gets the number of Resources.
resources = int(input[1][0])

#Declares the processes and resources.
availableR = [0 for i in range(resources)]
totalR = [0 for i in range(resources)]
wantP = [[0 for i in range(resources)] for j in range(processes)]
hasP = [[0 for i in range(resources)] for j in range(processes)]

#Generates the resources.
for i in range(1, resources+1):
    availableR[i-1] = (int(input[1][i]))
    totalR[i-1] = (int(input[1][i]))

#converts numerical input to integers.
for i in range(2, len(input)):
    for j in range(1, 4):
        input[i][j] = int(input[i][j])

#Runs the main part of the program.
for i in range(2, len(input)):
    #If the current command is a request of resources.
    if (input[i][0] == 'request'):
        #Checks if the amount of resources requested is possible to be allocated.
        if (totalR[input[i][2]] < input[i][3]):
            print("This amount of this resource will never be available.\n")
        else:
            #Requests the number of resources by the process.
            wantP[input[i][1]][input[i][2]] += input[i][3]
    
        #Allocates the resources if they are available.
        hasP[input[i][1]][input[i][2]] += min(input[i][3], availableR[input[i][2]])
        wantP[input[i][1]][input[i][2]] -= min(input[i][3], availableR[input[i][2]])
        availableR[input[i][2]] -= min(input[i][3], availableR[input[i][2]])
    #If the current command is a release of resources.
    elif (input[i][0] == 'release'):
        if (hasP[input[i][1]][input[i][2]] < input[i][3]):
            print("You are attempting to release more resources than this process has.\n")
        else:
            hasP[input[i][1]][input[i][2]] -= input[i][3]
            availableR[input[i][2]] += input[i][3]
        for k in range(processes):
            for l in range(resources):
                #Reallocates the resources if they are available.
                        hasP[k][l] += min(wantP[k][l], availableR[l])
                        wantP[k][l] -= min(wantP[k][l], availableR[l])
                        availableR[l] -= min(wantP[k][l], availableR[l])
    #Invalid command.
    else:
        print("Error: Invalid Command\n")

    #Checks if the processes can all be completed.
    runOption = [-1 for i in range(processes)]
    dl = checker(hasP, wantP, availableR)
    if (dl):
        print("Processes are stuck in a deadlock.\n")
    else:
        print("All Processes can run correctly:\n")
        print(runOption)
        print("\n")
    #Draws visual representation of processes and resources.
    GUI.draw(hasP, wantP, dl, runOption)

#Closes the file.
file.close()