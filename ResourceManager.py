import copy

# Name: Alexander Klein
# Date: 11/15/21
# Assignment: Resource Manager

#Function
def checker(has, want, available, total, finished, rl):
    #Initializes internal values.
    hasC = copy.deepcopy(has)
    wantC = copy.deepcopy(want)
    availC = copy.deepcopy(available)
    totalC = copy.deepcopy(total)
    finishC = copy.deepcopy(finished)
    finishedPrcs = 0
    stuckPrcs = 0

    #Checks if every process is finished
    for i in range(processes):
        if (finishC[i]):
            finishedPrcs += 1
    if (finishedPrcs == processes):
        dl = False
    else:
        finishedPrcs = 0
        stuckPrcs = 0
        iterations = -1
        for i in range(processes):
            iterations += 1
            #If the process is not finished.
            if (not(finishC[i])):
                hasAll = 0
                #Counts if the process has all of its resources, releasing them if it does.
                for j in range(resources):
                    if (wantC[i][j] == 0):
                        hasAll += 1
                if (hasAll == resources):
                    for j in range(resources):
                        availC[j] += hasC[i][j]
                        hasC[i][j] = 0
                        finishC[i] = True
                    finishedPrcs += 1
                    if (iterations not in runOption):
                        runOption[rl] = iterations
                        rl += 1
                    checker(hasC, wantC, availC, totalC, finishC, rl)
                #If the process doesnt have all of its processes.
                else:
                    for j in range(resources):
                        #Allocates the resources if they are available.
                        hasC[i][j] += min(wantC[i][j], availC[j])
                        wantC[i][j] -= min(wantC[i][j], availC[j])
                        availC[j] -= min(wantC[i][j], availC[j])
                hasAll = 0
                #Counts if the process has all of its resources.
                for j in range(resources):
                    if (wantC[i][j] == 0):
                        hasAll += 1
                if (hasAll == resources):
                    checker(hasC, wantC, availC, totalC, finishC, rl)
                else:
                    stuckPrcs += 1
            else:
                finishedPrcs += 1
    if (not(finishedPrcs == processes) and (finishedPrcs + stuckPrcs == processes)):
        dl = True

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
pFinished = [False for i in range(processes)]

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
            pFinished[input[i][1]] = False
    
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
    
    dl = False
    runOption = [-1 for i in range(processes)]
    runLocation = 0
    checker(hasP, wantP, availableR, totalR, pFinished, runLocation)
    for val in runOption:
        if (val < 0):
            dl = True
            break
    if (dl):
        print("Processes are stuck in a deadlock.\n")
    else:
        print("All Processes can run correctly:\n")
        print(runOption)
        print("\n")

#Closes the file.
file.close()