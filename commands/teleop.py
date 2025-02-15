import wpilib
import wpilib.drive

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.XboxController(0)  # nah actualy back to joystick
        self.drivetrain = drivetrain

    def update(self):
        y_speed = -self.controller.getLeftY()
        x_speed = self.controller.getLeftX()
        x_speed_inv = x_speed * -1
        z_rotation = self.controller.getRightX()
        self.drivetrain.drive_cartesian(y_speed, x_speed_inv, z_rotation)
        #print(f"Teleop: y={y_speed}, x={x_speed}, rotation={z_rotation}")

print("teleop initiated")

