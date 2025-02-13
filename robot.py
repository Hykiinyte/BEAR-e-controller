#P.S. If RobotPy is not working on your computer or on this web, please open Terminal and type the following:
#pip install robotpy
#pip install robotpy-rev
#pip install robotpy-ctre
#pip install robotpy-navx

import wpilib
import wpilib.drive
from subsystems.drivetrain import Drivetrain
from subsystems.utilhandler import Utilhandler
from commands.autonomous import Autonomous
from commands.teleop import TeleopControl

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        try:
            """Initialize robot subsystems"""
            self.drivetrain = Drivetrain()
            self.auto = Autonomous(self.drivetrain)
            self.teleop = TeleopControl(self.drivetrain)
            self.util = Utilhandler()
        except Exception as e:
            print(f"Something went wrong trying to Initiate Robot: {e}")

    def autonomousInit(self):
        try:
            """Called once at the start of autonomous mode"""
            self.auto.start()
        except Exception as e:
            print(f"Something went wrong trying to initiate Autonomous: {e}")

    def autonomousPeriodic(self):
        try:
            """Runs periodically during autonomous"""
            self.auto.update()
        except Exception as e:
            print(f"Something went wrong trying to run Autonomous: {e}")

    def teleopPeriodic(self):
        try:
            """Runs periodically during teleop"""
            self.teleop.update()
        except Exception as e:
            print(f"Something went wrong running TeleOperation: {e}")

    def utilInit(self):
        try:
            """Starts the utility subsystem like arms or intake"""
            self.util.update()
        except Exception as e:
            print(f"Something went wrong initiating Utilities: {e}")

print("robot initiated")
