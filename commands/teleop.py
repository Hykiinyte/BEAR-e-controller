import wpilib
import wpilib.drive
from subsystems.utilhandler import Utilhandler

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
        self.handle = self.operator.getRawButton(1)  # button 1
        self.cruise = self.operator.getRawButton(2)  # button 2
        self.flash = self.operator.getRawButton(3)  # button 3
        self.audio = self.operator.getRawButton(4)  # button 4
        self.wipers = self.operator.getRawButton(5)  # button 5
        self.map = self.operator.getRawButton(6) # button 6
        self.light = self.operator.getRawButton(7)
        self.talk = self.operator.getRawButton(8)

        self.lever1up = self.operator.getRawButton(13)
        self.lever1down = self.operator.getRawButton(14)

        self.enginestart = self.operator.getRawButton(11)
        self.emergencyoff = self.operator.getRawButton(12)

        # (add more buttons as needed)

        # POV
        self.operator.getPOV()  # POV

        # Axis
        x_fine = self.operator.getX() * 0.1 # X axis
        y_fine = self.operator.getY() * 0.1 # Y axis
        z_fine = self.operator.getZ() * 0.1 # Z axis  

        #button library
        if self.handle == True:
            print("Button 1 pressed")
        if self.cruise == True:
            print("Button 2 pressed")
        if self.flash == True:    
            print("Button 3 pressed")
        if self.audio == True:
            print("Button 4 pressed")
        if self.wipers == True:
            print("Button 5 pressed")
        if self.map == True:
            print("Button 6 pressed")
        if self.light == True:
            print("button 7")
        if self.light == True:
            print("button 8")

        if self.enginestart == True:
            print("engine start")
        if self.emergencyoff == True:
            print("emergency off")

        # levers
        if self.lever1up == True: #elevator lever 1
            print("lever 1 up")
        if self.lever1down == True:
            print("lever 1 down")

        # fine control
        self.drivetrain.drive_cartesian(y_fine, x_fine, z_fine)

print("teleop initiated")
