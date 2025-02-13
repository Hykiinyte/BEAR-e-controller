import wpilib
from wpilib import XboxController, GenericHID

class TeleopControl:
    def __init__(self, drivetrain):
        # Use a single controller; device 0 represents your gamepad.
        self.controller = XboxController(0)
        self.drivetrain = drivetrain

    def update(self):
        """Called every cycle during teleop"""
        # Use the left stick for translation (forward/backward and strafe).
        y_speed = -self.controller.getY(GenericHID.Hand.kLeft)
        x_speed = self.controller.getX(GenericHID.Hand.kLeft)
        x_speed_inv = x_speed * -1
        # Use the right stick horizontal axis for rotation.
        z_rotation = self.controller.getX(GenericHID.Hand.kRight)
        
        # Now pass these values to the drivetrain.
        self.drivetrain.drive_cartesian(y_speed, x_speed, z_rotation)
        
        # Optional: print debug info
        #print(f"Teleop: y={y_speed}, x={x_speed}, rotation={z_rotation}")

print("teleop initiated")

