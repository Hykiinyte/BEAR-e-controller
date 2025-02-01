#P.S. If RobotPy is not working on your computer or on this web, please open Terminal and type the following:
#pip install robotpy
#pip install robotpy-rev
#pip install robotpy-ctre
#pip install robotpy-navx
#pip install robotpy-pathplanner

import wpilib
from subsystems.drivetrain import Drivetrain
from commands.autonomous import Autonomous
from commands.teleop import TeleopControl

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Initialize robot subsystems"""
        self.drivetrain = Drivetrain()
        self.auto = Autonomous(self.drivetrain)
        self.teleop = TeleopControl(self.drivetrain)

    def autonomousInit(self):
        """Called once at the start of autonomous mode"""
        self.auto.start()

    def autonomousPeriodic(self):
        """Runs periodically during autonomous"""
        self.auto.update()

    def teleopPeriodic(self):
        """Runs periodically during teleop"""
        self.teleop.update()

if __name__ == "__main__":
    wpilib.run(MyRobot)
