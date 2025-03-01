import wpilib
import wpilib.drive

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.XboxController(0) # nah actualy back to joystick
        self.drivetrain = drivetrain

    def update(self):
        y_speed = -self.controller.getLeftY()
        x_speed = self.controller.getLeftX()
        z_rotation = self.controller.getRightX()

        x_speed_inv = x_speed * -1

        self.drivetrain.drive_cartesian(y_speed, x_speed_inv, z_rotation)

print("teleop initiated")
