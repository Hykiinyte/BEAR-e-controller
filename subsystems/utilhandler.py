import wpilib
import wpilib.drive
import rev  # For SPARK MAX

class Utilhandler:
    def __init__(self):
        """Initialize utilitrain motors"""
        global motor1
        global motor2
        global motor3
        motor1 = rev.SparkMax(11, rev.SparkMax.MotorType.kBrushless)
        motor2 = rev.SparkMax(15, rev.SparkMax.MotorType.kBrushless)
        motor3 = rev.SparkMax(1, rev.SparkMax.MotorType.kBrushless)

print("utils initiated")

class Elevator:
    def __init__(self, motor_id):
        motor1.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the elevator motor speed (-1 to 1)."""
        motor1.set(speed)
        print(f"Elevator moving at {speed}")

    def stop(self):
        motor1.set(0)
        print("Elevator stopped")

class CoralIntake:
    def __init__(self, motor_id):
        motor2.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the coral intake motor speed (-1 to 1)."""
        motor2.set(speed)
        print(f"Coral intake moving at {speed}")

    def stop(self):
        motor2.set(0)
        print("Coral intake stopped")

class AlgaeIntake:
    def __init__(self, motor_id):
        motor3.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the algae intake motor speed (-1 to 1)."""
        motor3.set(speed)
        print(f"Algae intake moving at {speed}")

    def stop(self):
        motor3.set(0)
        print("Algae intake stopped")


#This is incomplete code. It is meant to be used as a reference for the user to have something to start with.
#Have fun coding!
