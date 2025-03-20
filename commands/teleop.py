import wpilib
from subsystems.utilhandler import (
    Elevator,
    CoralIntake,
    AlgaeIntake,
    DeepCage,
    MotorController
)

class TeleopControl:
    def __init__(self, drivetrain):
        self.controller = wpilib.XboxController(0)  # or a joystick, if preferred
        self.operator = wpilib.Joystick(1)  # Operator console
        self.drivetrain = drivetrain

        # Initialize motor controllers with new remapping.
        # Adjust motor IDs and inversion as needed.
        self.elevator_motor1 = MotorController(11, inverted=False)
        self.elevator_motor2 = MotorController(15, inverted=True)
        self.coral_motor = MotorController(1, inverted=False)
        self.algae_motor = MotorController(2, inverted=False)
        self.deepcage_motor = MotorController(3, inverted=False)

        # Create subsystems
        self.elevator = Elevator(self.elevator_motor1, self.elevator_motor2)
        self.coral_intake = CoralIntake(self.coral_motor)
        self.algae_intake = AlgaeIntake(self.algae_motor)
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

        # Manual elevator control via levers
        if self.operator.getRawButton(13):
            self.elevator.move_manual(0.1)  # manual up
        elif self.operator.getRawButton(14):
            self.elevator.move_manual(-0.1)  # manual down
        else:
            # If no manual override, ensure motors are stopped.
            self.elevator.stop()

        # Intake controls for Coral, Algae, and Deep Cage:
        if self.operator.getRawButton(17):
            self.coral_intake.move(0.5)
        elif self.operator.getRawButton(18):
            self.coral_intake.move(-0.5)
        else:
            self.coral_intake.stop()

        if self.operator.getRawButton(19):
            self.algae_intake.move(0.5)
        elif self.operator.getRawButton(20):
            self.algae_intake.move(-0.5)
        else:
            self.algae_intake.stop()

        if self.operator.getRawButton(21):
            self.deepcage.move(0.5)
        elif self.operator.getRawButton(22):
            self.deepcage.move(-0.5)
        else:
            self.deepcage.stop()

        # --- Periodic Updates ---
        # update elevator movement without blocking the main loop.
        self.elevator.update()

print("Teleop initiated")
