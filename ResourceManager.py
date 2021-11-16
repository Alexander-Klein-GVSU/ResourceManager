import Process
import Resource
import copy

#Function
def checker(p, r, rl):
    #Initializes internal values.
    prcCpy = copy.deepcopy(p)
    resCpy = copy.deepcopy(r)
    finishedPrcs = 0
    stuckPrcs = 0

    #Checks if every process is finished
    for prcs in prcCpy:
        if (prcs.isFinished()):
            finishedPrcs += 1
    if (finishedPrcs == processes):
        dl = False
    else:
        iterations = 0
        for prcs in prcCpy:
            iterations += 1
            #If the process is not finished.
            if (not(prcs.isFinished())):
                hasAll = 0
                #Counts if the process has all of its resources, releasing them if it does.
                for i in range(resources-1):
                    if (prcs.getRequests(i) == 0):
                        hasAll += 1
                if (hasAll == resources):
                    for i in range(resources-1):
                        resCpy[i].returnRes(prcs.getHas(i))
                        prcs.release(i, prcs.getHas(i))
                    finishedPrcs += 1
                    runOption[rl] = iterations
                    rl += 1
                    checker(prcCpy, resCpy, rl)
                #If the process doesnt have all of its processes.
                else:
                    for i in range(resources-1):
                        #Allocates the resources if they are available.
                        if (resCpy[i].provideRes(prcs.getRequests(i)) == 0):
                            prcs.take(i, prcs.getRequests(i))
                        else:
                            prcs.take(i, resource[i].getAvailable())
                            resCpy[i].provideRes(resource[i].getAvailable())
                hasAll = 0
                #Counts if the process has all of its resources, releasing them if it does.
                for i in range(resources-1):
                    if (prcs.getRequests(i) == 0):
                        hasAll += 1
                if (hasAll == resources):
                    checker(prcCpy, resCpy, rl)
                else:
                    stuckPrcs += 1
    if (not(finishedPrcs == processes) and (finishedPrcs + stuckPrcs == processes)):
        dl = True

#Opens the file.
file = open("upload.txt", "r")

#Gets the number of processes.
input = file.readline(0)
processes = int(input)

#Gets the number of Resources.
input = file.readline(1)
input = input.split(" ")
resources = input[0]

#Declares the processes and resources.
resource = []
process = []

#Generates the resources.
for i in range(1, resources):
    resource[i-1] = Resource(input[i])

#Generates the processes.
for i in range(processes-1):
    process[i] = Process(resources)

#Runs the main part of the program.
lineCt = len(file.readlines)
for i in range(2, lineCt-1):
    input = file.readline(i)
    input = input.split(" ")

    #If the current command is a request of resources.
    if (input[0] == "request"):
        #Checks if the amount of resources requested is possible to be allocated.
        if (resource[input[2]].getTotal() < input[3]):
            print("This amount of this resource will never be available.\n")
        else:
            #Requests the number of resources by the process.
            process[input[1]].request(input[2], input[3])
        #Allocates the resources if they are available.
        if (resource[input[2]].provideRes(input[3]) == 0):
            process[input[1]].take(input[2], input[3])
        else:
            process[input[1]].take(input[2], resource[input[2]].getAvailable())
            resource[input[2]].provideRes(resource[input[2]].getAvailable())
    #If the current command is a release of resources.
    elif (input[0] == "release"):
        if (process[input[1]].getHas(input[2]) < input[3]):
            print("You are attempting to release more resources than this process has.\n")
        else:
            process[input[1]].release(input[3])
            resource[input[2]].returnRes(input[3])
    #Invalid command.
    else:
        print("Error: Invalid Command\n")

    #Checks if the processes can all be completed.
    
    dl = False
    runOption = []
    runLocation = 0
    checker(process, resource, runLocation)
    if (dl):
        print("Processes are stuck in a deadlock.\n")
    else:
        print("All Processes can run correctly:\n")
        print(runOption)
        print("\n")

#Closes the file.
file.close()