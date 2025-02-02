import wpilib
import wpilib.drive
import rev  # For SPARK MAX

class Utilhandler:
    def __init__(self):
        """Initialize utilitrain motors"""
        self.motor1 = rev.SparkMax(1, rev.SparkMax.MotorType.kBrushless)
        self.motor2 = rev.SparkMax(2 ,rev.SparkMax.MotorType.kBrushless)

    def handle_utils():
        """Handles tools like a ball intake or a shooter"""

print("utils initiated")
