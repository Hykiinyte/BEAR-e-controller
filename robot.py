#P.S. If RobotPy is not working on your computer or on this web, please open Terminal and type the following:
#pip install robotpy
#pip install robotpy-rev
#pip install robotpy-ctre
#pip install robotpy-navx

import wpilib
import wpilib.drive
from subsystems.drivetrain import Drivetrain
from subsystems.utilhandler import Utilhandler
from subsystems.camerascript import Camera
from commands.autonomous import Autonomous
from commands.teleop import TeleopControl
from pathlib import Path

class MyRobot(wpilib.TimedRobot):

    #----------Robot Initiation----------

    def robotInit(self):
        try:
            """Initialize robot subsystems"""
            self.drivetrain = Drivetrain()
            self.auto = Autonomous(self.drivetrain)
            self.teleop = TeleopControl(self.drivetrain)
            self.util = Utilhandler()
            self.camera = Camera()
        except Exception as e:
            print(f"Something went wrong trying to Initiate Robot: {e}")
    
    #----------Robot Functions----------

    def autonomousInit(self):
        try:
            """Called once at the start of autonomous mode"""
            self.auto.start()
        except Exception as e:
            print(f"Something went wrong trying to initiate Autonomous: {e}")

    def autonomousPeriodic(self):
        try:
            """Runs periodically during autonomous"""
            self.auto.update()
        except Exception as e:
            print(f"Something went wrong trying to run Autonomous: {e}")

    def teleopPeriodic(self):
        try:
            """Runs periodically during teleop"""
            self.teleop.update()
        except Exception as e:
            print(f"Something went wrong running TeleOperation: {e}")
    #missing "practice", "test", and disabled functions, however, they are not necessary for the robot to function

    #----------Utility Functions----------

    def utilInit(self):
        try:
            """Starts the utility subsystem like arms or intake"""
            self.util.update()
        except Exception as e:
            print(f"Something went wrong initiating Utilities: {e}")

    def cameraInit(self):
        try:
            """Starts the camera"""
            self.camera.cameraInit()
            wpilib.CameraServer.launch('camerascript.py:main')
        except Exception as e:
            print(f"Something went wrong initiating Camera: {e}")

    #----------Verification----------

    def keyinit():
        try:
            keyfile_path = Path("constants") / "keyfile.jpg"
            if keyfile_path.exists():
                print("Keyfile found")
            else:
                raise FileNotFoundError("Keyfile not found")   
        except Exception as e:
            print(f"Something went wrong trying to find the keyfile: {e}")

print("robot initiated")
