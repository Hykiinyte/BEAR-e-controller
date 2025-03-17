import wpilib
import wpilib.drive
from subsystems.utilhandler import Elevator
from subsystems.utilhandler import CoralIntake
from subsystems.utilhandler import AlgaeIntake
from subsystems.utilhandler import DeepCage

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.XboxController(0) # nah actualy back to joystick
        self.drivetrain = drivetrain
        self.operator = wpilib.Joystick(1) # operator console

    def update(self):
        #variables
        self.elevator = Elevator(motor_id=11)
        self.coralintake = CoralIntake(motor_id=15)
        self.algaeintake = AlgaeIntake(motor_id=1)
        self.deepcage = DeepCage(motor_id=2)


        """driver controls"""
        y_speed = -self.controller.getLeftY()
        x_speed = self.controller.getLeftX()
        z_rotation = self.controller.getRightX()
        x_speed_inv = x_speed * -1
        z_rot_inv = z_rotation * -1

        self.a = self.controller.getRawButton(1)  # A
        self.b = self.controller.getRawButton(2)  # B
        self.x = self.controller.getRawButton(3)  # X
        self.y = self.controller.getRawButton(4)  # Y
        self.lb = self.controller.getRawButton(5)  # Left Bumper
        self.rb = self.controller.getRawButton(6)  # Right Bumper
        self.lt = self.controller.getRawButton(7)  # Left Trigger
        self.rt = self.controller.getRawButton(8)  # Right Trigger

        if self.a == True:
            print("Button A pressed")
        if self.b == True:
            print("Button B pressed")
        if self.x == True:
            print("Button X pressed")
        if self.y == True:
            print("Button Y pressed")
        if self.lb == True:
            print("Button LB pressed")
        if self.rb == True:
            print("Button RB pressed")
        if self.lt == True:
            print("Button LT pressed")
        if self.rt == True:
            print("Button RT pressed")

        

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
        self.lever4up = self.operator.getRawButton(19) # deep cage adjustment
        self.lever4down = self.operator.getRawButton(20) # deep cage adjustment

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
            print("Button 1 pressed")
        if self.cruise == True:
            print("Button 2 pressed")
        if self.flash == True:    
            self.elevator.setpos(3) #elevator level 3
            print("Button 3 pressed")
        if self.audio == True:
            self.elevator.setpos(4) #elevator level 4
            print("Button 4 pressed")
        if self.wipers == True:
            self.elevator.setpos(1) #elevator level 1
            print("Button 5 pressed")
        if self.map == True:
            self.elevator.setpos(2) #elevator level 2
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
        if self.lever1up:
            self.elevator.move(0.1)  # Move elevator up at
        elif self.lever1down:
            self.elevator.move(-0.1)  # Move elevator down
        else:
            self.elevator.stop()  # Stop the elevator if no lever button is pressed

        if self.lever2up:
            self.coralintake.move(0.5) # same stuff but for coral intake
        elif self.lever2down:
            self.coralintake.move(-0.5)
        else:
            self.coralintake.stop()

        if self.lever3up: # same stuff but for algae intake
            self.algaeintake.move(0.5)
        elif self.lever3down:
            self.algaeintake.move(-0.5)
        else:
            self.algaeintake.stop()

        if self.lever4up: #DEEEEEEEP CAAAAAAAGEEEE
            self.deepcage.move(0.5)
        elif self.lever4down:
            self.deepcage.move(-0.5)
        else:
            self.deepcage.stop()

        

        """combo controls"""
        y_total = y_speed + y_fine
        x_total = x_speed_inv + x_fine
        z_total = z_rot_inv + z_fine
        self.drivetrain.drive_cartesian(y_total, x_total, z_total)

print("teleop initiated")
