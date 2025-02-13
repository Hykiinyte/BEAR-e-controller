import tkinter
import wpilib

#idk use Tkinter to create a window and design a GUI for our driver station
#while this is not necessary, it is a good utility to have, especially for debugging and reading sensor values in real time possibly
root = tkinter.Tk()
root.title("Cy-Bears Driver Station")
root.geometry("400x400")
root.configure(bg="blue")

#create a label for the title
title = tkinter.Label(root, text="Cy-Bears Driver Station", font=("Open Sans", 24), bg="black", fg="white")
title.pack()

#create a label for the drivetrain
drivetrain = tkinter.Label(root, text="Drivetrain", font=("Open Sans", 18), bg="black", fg="white")
drivetrain.pack()

#create a label for the utiliiy state
util = tkinter.Label(root, text="Utility", font=("Open Sans", 18), bg="black", fg="white")
util.pack()

#create a label for the sensor values
sensor = tkinter.Label(root, text="Sensor", font=("Open Sans", 18), bg="black", fg="white")
sensor.pack()

#you get the memo
example = tkinter.Label(root, text="just add more stuff here", font=("Open Sans", 18), bg="black", fg="white")
example.pack()

#execute the GUI
root.mainloop()
