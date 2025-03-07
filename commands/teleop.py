import wpilib
import wpilib.drive
from subsystems.utilhandler import Elevator
from subsystems.utilhandler import CoralIntake
from subsystems.utilhandler import AlgaeIntake

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

        

        """operator controls"""
        #buttons
        self.handle = self.operator.getRawButton(1)  # 180 (change to wrist)
        self.cruise = self.operator.getRawButton(2)  # P
        self.flash = self.operator.getRawButton(3)  # elevator level 3
        self.audio = self.operator.getRawButton(4)  # elevator level 4
        self.wipers = self.operator.getRawButton(5)  # elevator level 1
        self.map = self.operator.getRawButton(6) # elevator level 2
        self.light = self.operator.getRawButton(7) # coral on
        self.talk = self.operator.getRawButton(8) # algae on

        self.lever1up = self.operator.getRawButton(13) # elevator adjustment
        self.lever1down = self.operator.getRawButton(14) # elevator adjustment
        self.lever2up = self.operator.getRawButton(15) # coral intake adjustment
        self.lever2down = self.operator.getRawButton(16) # coral intake adjustment
        self.lever3up = self.operator.getRawButton(17) # algae intake adjustment
        self.lever3down = self.operator.getRawButton(18) # algae intake adjustment

        self.enginestart = self.operator.getRawButton(11) # idk
        self.emergencyoff = self.operator.getRawButton(12) # emergency off

        # (add more buttons as needed)

        # POV
        self.operator.getPOV()  # POV

        # Axis
        x_fine = self.operator.getX() * 0.1 # X axis
        y_fine = self.operator.getY() * 0.1 # Y axis
        z_fine = self.operator.getZ() * 0.1 # Z axis  

        #button library
        if self.handle == True:
            self.drivetrain.drive_cartesian(0, 0, 1)
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
        self.elevator = Elevator(motor_id=11)
        self.coralintake = CoralIntake(motor_id=15)
        self.algaeintake = AlgaeIntake(motor_id=1)

        if self.lever1up:
            self.elevator.move(0.5)  # Move elevator up at half speed
        elif self.lever1down:
            self.elevator.move(-0.5)  # Move elevator down
        else:
            self.elevator.stop()  # Stop the elevator if no lever button is pressed

        if self.lever2up:
            self.coralintake.move(0.5) # same stuff but for coral intake
        elif self.lever2down:
            self.coralintake.move(-0.5)
        else:
            self.coralintake.stop()

        if self.lever3up:
            self.algaeintake.move(0.5)
        elif self.lever3down:
            self.algaeintake.move(-0.5)
        else:
            self.algaeintake.stop()

        

        """combo controls"""
        y_total = y_speed + y_fine
        x_total = x_speed_inv + x_fine
        z_total = z_rot_inv + z_fine
        self.drivetrain.drive_cartesian(y_total, x_total, z_total)

print("teleop initiated")
