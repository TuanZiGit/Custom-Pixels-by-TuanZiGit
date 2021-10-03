import turtle as t
screen = t.Screen()
pixels=16
pen = t.Turtle()
pen.shape("square")
pen.color("black")
pen.speed("fastest")
pen.turtlesize(1)
pen.up()
def draw(color="black",shape="square",x=0,y=0):
    x-=pixels/2
    y-=pixels/2
    if pixels==8:
        x*=41
        y*=-41
    if pixels==16:
        x*=21
        y*=-21
    if pixels==32:
        x*=11
        y*=-11
    pen.goto(x,y)
    pen.color(color)
    pen.shape(shape)
    pen.stamp()
def creeper():
    global pixels
    px=pixels
    pixels=16
    pen.turtlesize(1)
    for j in range(2):
        for i in range(16):
            draw("green",x=i,y=j)
    for j in range(2,6):
        for i in range(2):
            draw("green",x=i,y=j)
        for i in range(2,6):
            draw(x=i,y=j)
        for i in range(6,10):
            draw("green",x=i,y=j)
        for i in range(10,14):
            draw(x=i,y=j)
        for i in range(14,16):
            draw("green",x=i,y=j)
    for j in range(6,8):
        for i in range(0,6):
            draw("green",x=i,y=j)
        for i in range(6,10):
            draw(x=i,y=j)
        for i in range(10,16):
            draw("green",x=i,y=j)
    for j in range(8,12):
        for i in range(0,4):
            draw("green",x=i,y=j)
        for i in range(4,12):
            draw(x=i,y=j)
        for i in range(12,16):
            draw("green",x=i,y=j)
    for j in range(12,14):
        for i in range(0,4):
            draw("green",x=i,y=j)
        for i in range(4,6):
            draw(x=i,y=j)
        for i in range(6,10):
            draw("green",x=i,y=j)
        for i in range(10,12):
            draw(x=i,y=j)
        for i in range(12,16):
            draw("green",x=i,y=j)
    for j in range(14,16):
        for i in range(16):
            draw("green",x=i,y=j)
    pixels=px
    if px==8:
        pen.turtlesize(2)
    elif px==16:
        pen.turtlesize(1)
    elif px==32:
        pen.turtlesize(0.5)
def cmdMain():
    global pixels
    while True:
        cmd=input("{}x Pixel> ".format(pixels))
        cmd=cmd.split(" ")
        if cmd[0]=="cpixel":
            if cmd[1]=="0":
                pixels=8
                pen.turtlesize(2)
            elif cmd[1]=="1":
                pixels=16
                pen.turtlesize(1)
            elif cmd[1]=="2":
                pixels=32
                pen.turtlesize(0.5)
            else:
                print("cpixel: Invalid argument {}.".format(cmd[1]))
        elif cmd[0]=="setpixel":
            if len(cmd)>=5:
                try:
                    draw(cmd[1],cmd[2],int(cmd[3]),int(cmd[4]))
                except ValueError:
                    print("setpixel: Invalid argument for target.")
                except t.TurtleGraphicsError:
                    print("setpixel: Invalid argument for color or shape.")
        elif cmd[0]=="clear":
            screen.clear()
        elif cmd[0]=="reset":
            screen.reset()
            pixels=16
            pen.turtlesize(1)
        elif cmd[0]=="creeper":
            print("Aww man! ---<<Revenge>> CaptainSparklez")
            creeper()
        elif cmd[0]=="update":
            pen.turtlesize(pen.turtlesize()[0])
        elif cmd[0]=="help":
            print("Custom Pixels V1 by TuanZiGit")
            print("Github here: https://github.com/TuanZiGit/Custom-Pixels-by-TuanZiGit")
            print("I'm happy to see someone opened issue or talk on Dicussions.")
            print("So now see how to use this program.")
            print("cpixel - Change the size of the pixels")
            print("help - Show this page")
            print("creeper - A demo. See this --> https://www.youtube.com/watch?v=cPJUBQd-PNM")
            print("setpixel - Set a pixel on the target(x,y).")
            print("clear - Clear screen")
            print("reset - Reset client")
            print("update - Update screen")
cmdMain()
