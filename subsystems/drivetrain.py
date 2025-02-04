import wpilib
import wpilib.drive
import rev  # For SPARK MAX

class Drivetrain:
    def __init__(self):
        """Initialize drivetrain motors"""
        try:
            self.front_left = rev.SparkMax(14, rev.SparkMax.MotorType.kBrushless)
            self.front_right = rev.SparkMax(12, rev.SparkMax.MotorType.kBrushless)
            self.rear_left = rev.SparkMax(16, rev.SparkMax.MotorType.kBrushless)
            self.rear_right = rev.SparkMax(13, rev.SparkMax.MotorType.kBrushless)

            # Set inversion (if needed)
            self.front_left.setInverted(False)
            self.rear_left.setInverted(False)
            self.front_right.setInverted(True)
            self.rear_right.setInverted(True) 

            # Create motor controllers wit mah SpeedControllerGroup
            self.drive = wpilib.drive.MecanumDrive(
                self.front_left, self.rear_left, self.front_right, self.rear_right
            )

            print("Drivetrain initialized successfully.")
        
        except Exception as e:
            print(f"Drivetrain initialization failed: {e}")

    def drive_cartesian(self, y_speed, x_speed, z_rotation):
        """Mecanum drive movement"""
        try:
            print(f"Driving with: y_speed={y_speed}, x_speed={x_speed}, z_rotation={z_rotation}")
            self.drive.driveCartesian(y_speed, x_speed, z_rotation)
        
        except Exception as e:
            print(f"Mecanum drivetrain configuration failed: {e}")
