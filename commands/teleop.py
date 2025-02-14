import wpilib
from wpilib import XboxController, GenericHID

class TeleopControl:
    def __init__(self, drivetrain):
        # Port 0 is the norm
        self.controller = XboxController(0)
        self.drivetrain = drivetrain

    def update(self):
        """Called every cycle during teleop"""
        # Use the left stick for vertical/strafing moves
        y_speed = -self.controller.getY(GenericHID.Hand.kLeft)
        x_speed = self.controller.getX(GenericHID.Hand.kLeft)
        x_speed_inv = x_speed * -1
        # Use the right stick horizontal axis for rotation
        z_rotation = self.controller.getX(GenericHID.Hand.kRight)
        
        # Drivetraining get it
        self.drivetrain.drive_cartesian(y_speed, x_speed, z_rotation)
        
        # Optional: print debug info
        #print(f"Teleop: y={y_speed}, x={x_speed}, rotation={z_rotation}")

print("teleop initiated")

