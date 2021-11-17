from graphics import *

# Name: Alexander Klein
# Date: 11/17/21
# Assignment: Resource Manager GUI

#Draws a visual representation of processes and 
#which resources they want/have.
def draw(h, w, dead, run, step):
    #Creates the Window
    win = GraphWin(title=str("Step " + str(step-1) + ":"), width=1000, height=500)

    process = []
    resource = []
    pMsg = []
    rMsg = []

    #Creates the Processes
    for i in range(len(h)):
        process.append(Circle(Point(40, 50*(i+1)), 20))
        process[i].setFill('pink')
        process[i].draw(win)
        pMsg.append(Text(Point(40, 50*(i+1)), str("P"+str(i))))
        pMsg[i].draw(win)

    #Creates the Resources
    for i in range(len(h[0])):
        resource.append(Rectangle(Point(980, (50*(i+1)-20)), Point(940, (50*(i+1)+20))))
        resource[i].setFill('lightblue')
        resource[i].draw(win)
        rMsg.append(Text(Point(960, 50*(i+1)), str("R"+str(i))))
        rMsg[i].draw(win)

    haveline = [[[0 for k in range(h[i][j])] for j in range(len(h[i]))] for i in range(len(h))]
    wantline = [[[0 for k in range(w[i][j])] for j in range(len(w[i]))] for i in range(len(w))]

    #Generates the Lines
    for i in range(len(h)):
        for j in range(len(h[i])):
            if (h[i][j] != 0):
                for k in range(h[i][j]):
                    haveline[i][j][k] = Line(Point(60, 50*(i+1)-20+k*4), Point(940, 50*(j+1)-20+k*4))
                    haveline[i][j][k].draw(win)
            if (w[i][j] != 0):
                for k in range(w[i][j]):
                    wantline[i][j][k] = Line(Point(60, 50*(i+1)+20-k*4), Point(940, 50*(j+1)+20-k*4))
                    wantline[i][j][k].setFill("red")
                    wantline[i][j][k].draw(win)

    #Outputs Bottom Text.
    if dead:
        stTxt = "Processes are stuck in a deadlock."
    else:
        stTxt = str("Processes can run using the order: " + str(run))
    legend = Text(Point(500, 470), "Red means want, Black means has. Click me to continue.")
    legend.draw(win)
    status = Text(Point(500, 490), stTxt)
    status.draw(win)

    #Closes the window.
    win.getMouse()
    win.close()
