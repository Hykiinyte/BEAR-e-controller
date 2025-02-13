import wpilib
import wpilib.drive
import rev  # For SPARK MAX

class Drivetrain:
    def __init__(self):
        """Initialize drivetrain motors"""
        try:
            self.front_left = rev.SparkMax(14, rev.SparkMax.MotorType.kBrushed)
            self.front_right = rev.SparkMax(12, rev.SparkMax.MotorType.kBrushed)
            self.rear_left = rev.SparkMax(16, rev.SparkMax.MotorType.kBrushed)
            self.rear_right = rev.SparkMax(13, rev.SparkMax.MotorType.kBrushed)

            # Set inversion (if needed)
            self.front_left.setInverted(False)
            self.rear_left.setInverted(False)
            self.front_right.setInverted(True)
            self.rear_right.setInverted(True) 

            # Create motor controllers wit mah SpeedControllerGroup
            # ideal config: (front_right, rear_right, front_left, rear_left)
            self.drive = wpilib.drive.MecanumDrive(
                self.front_right, self.rear_right, self.front_left, self.rear_left
            )

            print("Drivetrain initialized Vincent AND Nguyen")
        
        except Exception as e:
            print(f"Drivetrain initialization failed: {e}")

    def drive_cartesian(self, y_speed, x_speed, z_rotation):
        """Mecanum drive movement"""
        try:
            self.drive.driveCartesian(y_speed, x_speed, z_rotation)
        
        except Exception as e:
            print(f"Mecanum drivetrain configuration failed: {e}")
