import wpilib
import wpilib.drive

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.Joystick(0)  # Joystick on port 0
        self.drivetrain = drivetrain

    def update(self):
        """Called every cycle during teleop"""
        y_speed = -self.controller.getY()  # Forward/Backward
        x_speed = self.controller.getX()  # Strafe
        z_rotation = self.controller.getZ()  # Rotation
        x_speed_inv = x_speed * -1
        self.drivetrain.drive_cartesian(y_speed, x_speed_inv, z_rotation)
        #print(f"Teleop: y={y_speed}, x={x_speed}, z={z_rotation}") # Uncomment to see joystick values
         
print("teleop initiated")
