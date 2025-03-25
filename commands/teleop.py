import wpilib
from subsystems.utilhandler import Elevator
from subsystems.utilhandler import CoralIntake
from subsystems.utilhandler import CoralSpin
from subsystems.utilhandler import AlgaeIntake
from subsystems.utilhandler import DeepCage
from subsystems.utilhandler import MotorController

"""
10, 11, 12, 13 drivetrain (FL, RL, FR, RR)
14, 15, elevator
16, 17, coral (wrist, intake)
18, 19, algae (left, right)
20, deepcage
"""

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.XboxController(0)  # or a joystick, if preferred
        self.operator = wpilib.Joystick(1)  # Operator console
        self.drivetrain = drivetrain

        # Adjust motor IDs and inversion as needed
        self.elevator_motor1 = MotorController(14, inverted=False)
        self.elevator_motor2 = MotorController(15, inverted=True)
        self.coral_motor1 = MotorController(16, inverted=False)
        self.coral_motor2 = MotorController(17, inverted=False)
        self.algae_motor1 = MotorController(18, inverted=False)
        self.algae_motor2 = MotorController(19, inverted=False)
        self.deepcage_motor = MotorController(20, inverted=False)

        # Create subsystems
        self.elevator = Elevator(self.elevator_motor1, self.elevator_motor2)
        self.coral_intake = CoralIntake(self.coral_motor1)
        self.coral_spin = CoralSpin(self.coral_motor2)
        self.algae_intake = AlgaeIntake(self.algae_motor1, self.algae_motor2)
        self.deepcage = DeepCage(self.deepcage_motor)

    def update(self):
        # --- Driver Controls ---
        y_speed = -self.controller.getLeftY()
        x_speed = -self.controller.getLeftX()
        z_speed = -self.controller.getRightX()
        self.drivetrain.drive_cartesian(y_speed, x_speed, z_speed)

        # --- Operator Controls ---
        # Elevator position buttons:
        if self.operator.getRawButton(3):  # Example: Button 3 sets level 3
            self.elevator.set_position(3)
            print("Operator: Elevator set to level 3")
        elif self.operator.getRawButton(4):  # Button 4 sets level 4 (top)
            self.elevator.set_position(4)
            print("Operator: Elevator set to level 4")
        elif self.operator.getRawButton(5):  # Button 5 sets level 1 (low)
            self.elevator.set_position(1)
            print("Operator: Elevator set to level 1")
        elif self.operator.getRawButton(6):  # Button 6 sets level 2 (mid)
            self.elevator.set_position(2)
            print("Operator: Elevator set to level 2")
        elif self.operator.getRawButton(1):
            self.elevator.set_position(1)
            print("base")

        # Manual elevator control via levers
        #speed toggle
        turbovator = False
        if self.operator.getRawButton(12):
            if turbovator == False:
                turbovator = True
            elif turbovator == True:
                turbovator = False
            print("Operator toggled turbovator")
        #activate speed setting
        if turbovator == False:
            if self.operator.getRawButton(13):
                self.elevator.move_manual(0.15)  # manual up
            elif self.operator.getRawButton(14):
                self.elevator.move_manual(-0.15)  # manual down
            print("Operator set elevator speed to SLOW")
        elif turbovator == True:
            if self.operator.getRawButton(13):
                self.elevator.move_manual(0.65)  # manual up but fastr
            elif self.operator.getRawButton(14):
                self.elevator.move_manual(-0.65)  # manual down but faster
            print("Operator set elevator speed to FAST")
        else:
            # If no manual override, ensure motors are stopped.
            self.elevator.stop()

        # Intake controls for Coral, Algae, and Deep Cage:
        #Coral operates on two separate functions, wrist and intake.
        #Wrist
        if self.operator.getRawButton(15):
            self.coral_intake.move(0.2)
        elif self.operator.getRawButton(16):
            self.coral_intake.move(-0.2)
        else:
            self.coral_intake.stop()

        #Intake direction
        self.coral_spin.move(0.5)
        if self.operator.getRawButton(7):
            self.coral_spin.move(0.5)
        elif not self.operator.getRawButton(7):
            self.coral_spin.move(-0.5)
        else:
            self.coral_spin.stop()

        # Algae intake location partially based on elevator.
        # Both motors should move in tandem in one function.
        if self.operator.getRawButton(17):
            self.algae_intake.move(0.5)
            self.algae_spin.move(-0.5)
        elif self.operator.getRawButton(18):
            self.algae_intake.move(-0.5)
            self.algae_spin.move(0.5)
        else:
            self.algae_intake.stop()
            self.algae_spin.stop()

        #Deep cage is one function of one motor on a lever.
        if self.operator.getRawButton(19):
            self.deepcage.move(0.5)
        elif self.operator.getRawButton(20):
            self.deepcage.move(-0.5)
        else:
            self.deepcage.stop()

        # --- Periodic Updates ---
        # update elevator movement without blocking the main loop.
        self.elevator.update()

print("Teleop initiated")
