import wpilib

class Autonomous:
    def __init__(self, drivetrain):
        self.timer = wpilib.Timer()
        self.drivetrain = drivetrain

    def start(self):
        self.timer.reset()
        self.timer.start()

    def update(self):
        if self.timer.get() < 3.0:
            self.drivetrain.drive_cartesian(0.5, 0, 0)  #move forward a bit
        else:
            self.drivetrain.drive_cartesian(0, 0, 0)  #stop
        #this thing literally moves forward for 3 seconds as the auto setting
