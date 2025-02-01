#P.S. If RobotPy is not working on your computer or on this web, please open Terminal and type the following:
#pip install robotpy
#pip install robotpy-rev
#pip install robotpy-ctre
#pip install robotpy-navx
#pip install robotpy-pathplanner

import wpilib
from subsystems.drivetrain import Drivetrain  #Import drivetrain subsystem

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Runs once when the robot starts up."""
        self.drivetrain = Drivetrain()  #Initialize subsystems

    def autonomousInit(self):
        """Runs once when autonomous mode starts."""
        print("Autonomous mode starting!")

    def autonomousPeriodic(self):
        """Runs repeatedly during autonomous."""
        self.drivetrain.drive(0.5, 0, 0)  #Move forward half speed

    def teleopInit(self):
        """Runs once when teleop starts."""
        print("Teleop mode starting!")

    def teleopPeriodic(self):
        """Runs repeatedly during teleop."""
        x_speed = -self.controller.getY()
        y_speed = self.controller.getX()
        rotation = self.controller.getZ()
        self.drivetrain.drive(x_speed, y_speed, rotation)

if __name__ == "__main__":
    wpilib.run(MyRobot)
