import wpilib
import wpilib.drive

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.XboxController(0) # nah actualy back to joystick
        self.drivetrain = drivetrain
        self.operator = wpilib.Joystick(1) # operator console

    def update(self):
        """driver controls"""
        y_speed = -self.controller.getLeftY()
        x_speed = self.controller.getLeftX()
        z_rotation = self.controller.getRightX()
        x_speed_inv = x_speed * -1
        z_rot_inv = z_rotation * -1

        self.drivetrain.drive_cartesian(y_speed, x_speed_inv, z_rot_inv)

        """operator controls"""
        #buttons
        self.b1 = self.operator.getRawButton(1)  # button 1
        self.b2 = self.operator.getRawButton(2)  # button 2
        self.b3 = self.operator.getRawButton(3)  # button 3
        self.b4 = self.operator.getRawButton(4)  # button 4
        self.b5 = self.operator.getRawButton(5)  # button 5
        # (add more buttons as needed)

        # POV
        self.operator.getPOV()  # POV

        # Axis
        self.operator.getX()  # X axis
        self.operator.getY()  # Y axis
        self.operator.getZ()  # Z axis  

        #test print statement with button presses
        if self.b1 == True:
            print("Button 1 pressed")
        if self.b2 == True:
            print("Button 2 pressed")
        if self.b3 == True:    
            print("Button 3 pressed")
        if self.b4 == True:
            print("Button 4 pressed")
        if self.b5 == True:
            print("Button 5 pressed")

print("teleop initiated")
