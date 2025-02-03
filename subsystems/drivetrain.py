import wpilib
import wpilib.drive
import rev  # For SPARK MAX

class Drivetrain:
    try:
        def __init__(self):
            """Initialize drivetrain motors"""
            self.front_left = rev.SparkMax(14, rev.SparkMax.MotorType.kBrushless)
            self.front_right = rev.SparkMax(12, rev.SparkMax.MotorType.kBrushless)
            self.rear_left = rev.SparkMax(16, rev.SparkMax.MotorType.kBrushless)
            self.rear_right = rev.SparkMax(13, rev.SparkMax.MotorType.kBrushless)

            self.front_left.setInverted(False)
            self.rear_left.setInverted(False)
            self.front_right.setInverted(False)
            self.rear_right.setInverted(False)

            self.drive = wpilib.drive.MecanumDrive(
                self.front_left, self.rear_left, self.front_right, self.rear_right
            )
    except:
        print("Drivetrain failed.")

    try:
        def drive_cartesian(self, y_speed, x_speed, z_rotation):
            """Handles mecanum drive logic"""
            self.drive.driveCartesian(y_speed, x_speed, z_rotation)
    except:
        print("Mechanum drivetrain configuration failed.")

print("drivetrain initiated")
