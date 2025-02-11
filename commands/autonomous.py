import wpilib
import wpilib.drive

class Autonomous:
    def __init__(self, drivetrain):
        self.timer = wpilib.Timer()
        self.drivetrain = drivetrain

    def start(self):
        self.timer.reset()
        self.timer.start()

    def update(self):
        """Temporary auto routine; leave starting area, plus movement"""
        if self.timer.get() < 1.0:
            self.drivetrain.drive_cartesian(0.65, 0, 0)  #move forward 65% speed for 3 secs
        else:
            self.drivetrain.drive_cartesian(0, 0, 0)  #Stop

        if self.timer.get() > 3.0 and self.timer.get < 6.0:
            self.drivetrain.drive_cartesian(0, 0.25, 0)  #strafe at 1/4 speed for 3 secs
        elif self.timer.get() > 6.0 and self.timer.get() < 12.0:
            self.drivetrain.drive_cartesian(0, -0.25, 0)  #strafe at 1/4 other speed for 6 secs
        elif self.timer.get() > 12.0 and self.timer.get() < 15.0:
            self.drivetrain.drive_cartesian(0, 0.25, 0)  #recenter at origin
            
print("autonomous initiated")
