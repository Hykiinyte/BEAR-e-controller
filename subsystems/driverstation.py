import tkinter

import wpilib
from subsystems.drivetrain import Drivetrain
from subsystems.utilhandler import Utilhandler
from commands.autonomous import Autonomous
from commands.teleop import TeleopControl

#idk use Tkinter to create a window and design a GUI for our driver station
#while this is not necessary, it is a good utility to have, especially for debugging and reading sensor values in real time possibly
root = tkinter.Tk()
root.title("Cy-Bears Driver Station")
root.geometry("400x400")
root.configure(bg="black")
