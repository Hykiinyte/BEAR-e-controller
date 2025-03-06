import wpilib
import wpilib.drive
import rev  # For SPARK MAX

class Utilhandler:
    def __init__(self):
        """Initialize utilitrain motors"""
        global motor1
        global motor2
        self.motor1 = rev.SparkMax(11, rev.SparkMax.MotorType.kBrushless)
        self.motor2 = rev.SparkMax(15, rev.SparkMax.MotorType.kBrushless)

print("utils initiated")

class Elevator:
    def __init__(self, motor_id):
        self.motor.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the elevator motor speed (-1 to 1)."""
        self.motor.set(speed)
        print(f"Elevator moving at {speed}")

    def stop(self):
        self.motor.set(0)
        print("Elevator stopped")


#This is incomplete code. It is meant to be used as a reference for the user to have something to start with.
#Have fun coding!
