import wpilib
import wpilib.drive
import rev  # For SPARK MAX

class Utilhandler:
    def __init__(self):
        """Initialize utilitrain motors"""
        self.motor1 = rev.SparkMax(1, rev.SparkMax.MotorType.kBrushless)
        self.motor2 = rev.SparkMax(2 ,rev.SparkMax.MotorType.kBrushless)

print("utils initiated")

#This is incomplete code. It is meant to be used as a reference for the user to have something to start with.
#Have fun coding!
