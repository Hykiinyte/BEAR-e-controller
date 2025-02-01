#P.S. If RobotPy is not working on your computer or on this web, please open Terminal and type the following:
#pip install robotpy
#pip install robotpy-rev
#pip install robotpy-ctre
#pip install robotpy-navx
#pip install robotpy-pathplanner

import wpilib
from wpilib.drive import MecanumDrive
import rev  #for REV's SPARK MAX controllers(CAN)

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize Joystick
        self.controller = wpilib.Joystick(0)

        # Initialize Motors (Using CAN IDs)
        self.front_left = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)
        self.front_right = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        self.rear_left = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        self.rear_right = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushless)

        # Configure Motor Directions (if necessary)
        self.front_right.setInverted(True)
        self.rear_right.setInverted(True)

        # Setup Mecanum Drive
        self.drive = MecanumDrive(
            self.front_left, self.rear_left, self.front_right, self.rear_right
        )

    def teleopPeriodic(self):
        # Read joystick values
        y_speed = -self.controller.getY()  # Forward/Backward
        x_speed = self.controller.getX()   # Strafe Left/Right
        z_rotation = self.controller.getZ()  # Rotation

        # Drive robot using Mecanum Cartesian control
        self.drive.driveCartesian(y_speed, x_speed, z_rotation)

if __name__ == "__main__":
    wpilib.run(MyRobot)
