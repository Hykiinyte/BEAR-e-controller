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
        """Example auto routine: Drive forward for 3 seconds"""
        if self.timer.get() < 3.0:
            self.drivetrain.drive_cartesian(0.5, 0, 0)  #move forward half speed for 3 secs
        else:
            self.drivetrain.drive_cartesian(0, 0, 0)  #Stop
