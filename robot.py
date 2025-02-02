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
        """Initialize robot subsystems"""
        print("robotInit")
        self.drivetrain = Drivetrain()
        self.auto = Autonomous(self.drivetrain)
        self.teleop = TeleopControl(self.drivetrain)
        self.util = Utilhandler()

    def autonomousInit(self):
        """Called once at the start of autonomous mode"""
        print("autonomousInit")
        self.auto.start()

    def autonomousPeriodic(self):
        """Runs periodically during autonomous"""
        print("autonomousPeriodic")
        self.auto.update()

    def teleopPeriodic(self):
        """Runs periodically during teleop"""
        self.teleop.update()

    def utilInit(self):
        """Starts the utility subsystem like arm or intake"""
        print("utilInit")
        self.util.update()

print("robot initiated")
