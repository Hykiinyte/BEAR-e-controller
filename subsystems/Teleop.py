import wpilib

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.Joystick(0)  #joystick from usb slot 0 (interchagable)
        self.drivetrain = drivetrain

    def update(self):
        """Called every cycle during teleop"""
        y_speed = -self.controller.getY()  # Forward/Backward
        x_speed = self.controller.getX()  # Strafe
        z_rotation = self.controller.getZ()  # Rotation
        self.drivetrain.drive_cartesian(y_speed, x_speed, z_rotation)
