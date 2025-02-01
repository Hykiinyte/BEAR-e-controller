import wpilib
import rev  # For SPARK MAX

class Drivetrain:
    def __init__(self):
        """Initialize drivetrain motors"""
        self.front_left = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)
        self.front_right = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        self.rear_left = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        self.rear_right = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushless)

        self.drive = wpilib.drive.MecanumDrive(
            self.front_left, self.rear_left, self.front_right, self.rear_right
        )

    def drive_cartesian(self, y_speed, x_speed, z_rotation):
        """Handles mecanum drive logic"""
        self.drive.driveCartesian(y_speed, x_speed, z_rotation)
