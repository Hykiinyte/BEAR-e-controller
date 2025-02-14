import wpilib

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.Joystick(0)  # back to joystick baby
        self.drivetrain = drivetrain

    def update(self):
        #ok should be axes 0 and 1 are the left stick and axes 3 and 4 are the right stick.
        y_speed = -self.controller.getRawAxis(1)
        x_speed = self.controller.getRawAxis(0)
        x_speed_inv = x_speed * -1
        z_rotation = self.controller.getRawAxis(4)  # Adjust the index as needed.
        self.drivetrain.drive_cartesian(y_speed, x_speed_inv, z_rotation)
        print(f"Teleop: y={y_speed}, x={x_speed}, rotation={z_rotation}")

print("teleop initiated")

