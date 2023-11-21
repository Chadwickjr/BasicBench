from datetime import datetime
import os
import time
import math
import turtle as t
from tkinter import *

calcResults = [5.007, 9.818]
cpsResults = [9985841.798, 5445951.357]
frameResults= [59.056, 252.607]


def gofromto(x, y, z, xx, yy, zz):
    global xposition, yposition, zposition, FOV, xrotation, yrotation, zrotation, t
    cosz = math.cos(zrotation)
    sinz = math.sin(zrotation)
    cosx = math.cos(xrotation)
    sinx = math.sin(xrotation)
    cosy = math.cos(yrotation)
    siny = math.sin(yrotation)
    x1 = x * cosz - y * sinx
    y1 = x * sinz + y * cosz
    y1 = y * cosx - z * sinx
    z1 = y * sinx + z * cosx
    x1 = x * cosy + z * siny
    z1 = -1 * x * siny + z * cosy
    x2 = xx * cosz - yy * sinz
    y2 = xx * sinz + yy * cosz
    y2 = yy * cosx - zz * sinx
    z2 = yy * sinx + zz * cosx
    x2 = xx * cosy + zz * siny
    z2 = -1 * xx * siny + zz * cosy
    t.penup()
    t.goto(FOV * ((x1 + xposition) / (z1 + zposition)), FOV * ((y1 + yposition) / (z1 + zposition)))
    t.pendown()
    t.goto(FOV * ((x2 + xposition) / (z2 + zposition)), FOV * ((y2 + yposition) / (z2 + zposition)))

def cube(x, y, z, size):
    gofromto(x - size, y - size, z + size, x - size, y + size, z + size)
    gofromto(x - size, y + size, z + size, x + size, y + size, z + size)
    gofromto(x + size, y + size, z + size, x + size, y - size, z + size)
    gofromto(x + size, y - size, z + size, x - size, y - size, z + size)
    gofromto(x - size, y - size, z - size, x - size, y + size, z - size)
    gofromto(x - size, y + size, z - size, x + size, y + size, z - size)
    gofromto(x + size, y + size, z - size, x + size, y - size, z - size)
    gofromto(x + size, y - size, z - size, x - size, y - size, z - size)
    gofromto(x + size, y - size, z - size, x + size, y + size, z - size)
    gofromto(x + size, y + size, z - size, x + size, y + size, z + size)
    gofromto(x + size, y + size, z + size, x + size, y - size, z + size)
    gofromto(x + size, y - size, z + size, x + size, y - size, z - size)
    gofromto(x - size, y - size, z - size, x - size, y + size, z - size)
    gofromto(x - size, y + size, z - size, x - size, y + size, z + size)
    gofromto(x - size, y + size, z + size, x - size, y - size, z + size)
    gofromto(x - size, y - size, z + size, x - size, y - size, z - size)
    gofromto(x - size, y - size, z + size, x + size, y - size, z + size)
    gofromto(x + size, y - size, z + size, x + size, y - size, z - size)
    gofromto(x + size, y - size, z - size, x - size, y - size, z - size)
    gofromto(x - size, y - size, z - size, x - size, y - size, z + size)
    gofromto(x - size, y + size, z + size, x + size, y + size, z + size)
    gofromto(x + size, y + size, z + size, x + size, y + size, z - size)
    gofromto(x + size, y + size, z - size, x - size, y + size, z - size)
    gofromto(x - size, y + size, z - size, x - size, y + size, z + size)


def benchCube():
    global xposition, yposition, zposition, FOV, xrotation, yrotation, zrotation, t, frames
    start = time.time()
    frames = 0
    t.title("Cube Test")
    t.bgcolor("black")
    t.color("white")
    t.hideturtle()
    t.speed(0)
    FOV = 750
    xposition = 0
    yposition = -30
    zposition = 200
    xrotation = 0
    yrotation = 0
    zrotation = 0
    while yrotation < 5:
        t.tracer(0, 0)
        t.clear()
        cube(0, 0, 0, 20)
        yrotation += 0.005
        t.update()
        frames += 1
    t.bye()
    end = time.time()
    return frames / (end - start)

def benchCalculate():
    start = time.time()
    sums = 0
    for num in range(1, 50000001):
        sums += num ** 0.5
    end = time.time()
    return end - start


def main():

    datetime_obj = datetime.now()
    print(f"datetime_obj = {datetime_obj}")
    print(f"datetime_obj type = {type(datetime_obj)}")

    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")

    print("Finish!")
    time.sleep(0.5)


    window = Tk()
    window.geometry("800x700")
    window.configure(bg = "black")
    window.title("BasicBench v2.2.3")

    space = Label(window, bg = "black", text = 
                  "", font = ("Times 10"))
    space.grid(row = 0, column = 0, columnspan = 4, sticky = "w")

    mainHeader = Label(window, bg = "black", fg = "white", text = "BasicBench v2.2.3", font = ("Times 25"))
    mainHeader.grid(row = 2, column = 0, columnspan = 4, sticky = "w", padx = 10)

    subHeader = Label(window, bg = "black", fg = "white", text = 
                      "Please note that this is a simple benchmark and may not be completely acurate", font = ("Times 13"))
    subHeader.grid(row = 3, column = 0, columnspan = 4, sticky = "w", padx = 10)

    cpuHeader = Label(window, bg = "black", fg = "white", text = "\nCPU Test:", font = ("Times 20"))
    cpuHeader.grid(row = 4, column = 0, columnspan = 4, sticky = "w", padx = 10)

    cpuSubHeader = Label(window, bg = "black", fg = "white", text = "Runs through several calculations that rely more on CPU and RAM speed\n", font = ("Times 13"))
    cpuSubHeader.grid(row = 5, column = 0, columnspan = 4, sticky = "w", padx = 10)

    lastCalcResult = Label(window, bg = "black", fg = "white", text = "Speed of test: ", font = ("Times 17"))
    lastCalcResult.grid(row = 6, column = 0, columnspan = 4, sticky = "w", padx = 10)

    avgCalcResult = Label(window, bg = "black", fg = "white", text = "Calculations per second: ", font = ("Times 17"))
    avgCalcResult.grid(row = 7, column = 0, columnspan = 4, sticky = "w", padx = 10)

    calcReport = Label(window, bg = "black", fg = "white", text = " ", font = ("Times 13"))
    calcReport.grid(row = 8, column = 0, columnspan = 4, sticky = "w", padx = 10)

    calcReport2 = Label(window, bg = "black", fg = "white", text = " ", font = ("Times 12"))
    calcReport2.grid(row = 9, column = 0, columnspan = 4, sticky = "w", padx = 10)


    def runCPU():
        lastCalcResult.config(text = "Speed of last result: Running...")
        avgCalcResult.config(text = "Calculations per second: Running...")
        time.sleep(0.2)

        calcTime = benchCalculate()

        if calcTime // 60 > 0:
            lastCalcResult.config(text = f"Speed of test: {calcTime // 60} minuites, {round(calcTime % 60, 3)} seconds")
        else:
            lastCalcResult.config(text = f"Speed of test: {round(calcTime % 60, 3)} seconds")
        avgCalcResult.config(text =  f"Calculations per second: {round((50000000 / calcTime), 3)}")
        
        output = ""

        avgCalcTime = 0
        for num in calcResults:
            avgCalcTime += num
        avgCalcTime /= len(calcResults)

        if calcTime <= avgCalcTime:
            output += f"\nYour computer was {round(avgCalcTime - calcTime, 3)} seconds faster than the average time of {round(avgCalcTime, 3)}"
        else:
            output += f"\nYour computer was {round(calcTime - avgCalcTime, 3)} seconds slower than the average time of {round(avgCalcTime, 3)}"

        CPS = 50000000 / calcTime
        avgCPS = 0
        for num in cpsResults:
            avgCPS += num
        avgCPS /= len(cpsResults)

        calcReport.config(text = output)

        if CPS >= avgCPS:
            output = f"Your computer performed {round(CPS - avgCPS, 3)} more calculations per second than the average amount of {round(avgCPS, 3)}"
        else:
            output = f"Your computer performed {round(avgCPS - CPS, 3)} fewer calculations per second than the average amount of {round(avgCPS, 3)}"

        calcReport2.config(text = output)


    runCalcs = Button(window, bg = "black", fg = "white", text = "Run CPU Test", font = ("Times 20"), command = runCPU)
    runCalcs.grid(row = 6, padx = 600)



    gpuHeader = Label(window, bg = "black", fg = "white", text = "\nGPU Test:", font = ("Times 20"))
    gpuHeader.grid(row = 10, column = 0, columnspan = 4, sticky = "w", padx = 10)

    gpuSubHeader = Label(window, bg = "black", fg = "white", text = "Briefly renders a cube and tests frames per second, relies more on GPU\n", font = ("Times 13"))
    gpuSubHeader.grid(row = 11, column = 0, columnspan = 4, sticky = "w", padx = 10)

    avgCubeResult = Label(window, bg = "black", fg = "white", text = "Frames per second: ", font = ("Times 17"))
    avgCubeResult.grid(row = 12, column = 0, columnspan = 4, sticky = "w", padx = 10)

    cubeReport = Label(window, bg = "black", fg = "white", text = " ", font = ("Times 13"))
    cubeReport.grid(row = 13, column = 0, columnspan = 4, sticky = "w", padx = 10)


    def runGPU():
        avgCubeResult.config(text = "Frames per second: Running...")
        time.sleep(0.2)


        FPS = benchCube()
        avgCubeResult.config(text = f"Frames per second: {round(FPS, 3)}")
        
        avgFPS = 0
        for num in frameResults:
            avgFPS += num
        avgFPS /= len(frameResults)

        if avgFPS <= FPS:
            output = f"\nYour computer did {round(FPS - avgFPS, 3)} more frames per second than the average amount of {round(avgFPS, 3)}"
        else:
            output = f"\nYour computer did {round(avgFPS - FPS, 3)} fewer frames per second than the average amount of {round(avgFPS, 3)}"

        cubeReport.config(text = output)


    runCube = Button(window, bg = "black", fg = "white", text = "Run GPU Test", font = ("Times 20"), command = runGPU)
    runCube.grid(row = 12, padx = 600)



    end = Label(window, bg = "black", fg = "white", text = "\n\n\nOnly press run button once, application may freeze / become unresponsive for a moment while running tests", font = ("Times 13"))
    end.grid(row = 20, column = 0, columnspan = 4, sticky = "w", padx = 10)

    window.mainloop()



if __name__ == "__main__":
    main()