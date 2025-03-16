import wpilib
import wpilib.drive
import pygame
import rev  # For SPARK MAX

class Utilhandler:
    def __init__(self):
        """Initialize utilitrain motors"""
        global motor1
        global motor2
        global motor3
        global motor4
        motor1 = rev.SparkMax(11, rev.SparkMax.MotorType.kBrushless)
        motor2 = rev.SparkMax(15, rev.SparkMax.MotorType.kBrushless)
        motor3 = rev.SparkMax(1, rev.SparkMax.MotorType.kBrushless)
        motor4 = rev.SparkMax(2, rev.SparkMax.MotorType.kBrushless)

print("utils initiated")

class Elevator:
    elevator_level = 1
    def __init__(self, motor_id):
        motor1.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the elevator motor speed (-1 to 1)."""
        motor1.set(speed)
        print(f"Elevator moving at {speed}")

    def setpos(self, level):
        if level == 0:
            motor1.set(0)
            self.elevator_level = 0
        elif level == 1:
            if self.elevator_level == 1:
                motor1.set(0.5)
                pygame.time.wait(1000)
                motor1.set(0)
            if self.elevator_level == 2:
                motor1.set(-0.5)
                pygame.time.wait(2000)
                motor1.set(0)
            if self.elevator_level == 3:
                motor1.set(-0.5)
                pygame.time.wait(3000)
                motor1.set(0)
            if self.elevator_level == 4:
                motor1.set(-0.5)
                pygame.time.wait(4000)
                motor1.set(0)
            self.elevator_level = level
        elif level == 2:
            if self.elevator_level == 1:
                motor1.set(0.5)
                pygame.time.wait(1000)
                motor1.set(0)
            if self.elevator_level == 2:
                motor1.set(0)
            if self.elevator_level == 3:
                motor1.set(-0.5)
                pygame.time.wait(1000)
                motor1.set(0)
            if self.elevator_level == 4:
                motor1.set(-0.5)
                pygame.time.wait(2000)
                motor1.set(0)
            self.elevator_level = level
        elif level == 3:
            if self.elevator_level == 1:
                motor1.set(0.5)
                pygame.time.wait(1000)
                motor1.set(0)
            if self.elevator_level == 2:
                motor1.set(0)
            if self.elevator_level == 3:
                motor1.set(0)
            if self.elevator_level == 4:
                motor1.set(-0.5)
                pygame.time.wait(1000)
                motor1.set(0)
            self.elevator_level = level
        elif level == 4:
            if self.elevator_level == 1:
                motor1.set(0.5)
                pygame.time.wait(1000)
                motor1.set(0)
            if self.elevator_level == 2:
                motor1.set(0)
            if self.elevator_level == 3:
                motor1.set(0)
            if self.elevator_level == 4:
                motor1.set(0)
            self.elevator_level = level
        print(f"Elevator set to level {level}")

    def stop(self):
        motor1.set(0)
        print("Elevator stopped")

class CoralIntake:
    def __init__(self, motor_id):
        motor2.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the coral intake motor speed (-1 to 1)."""
        motor2.set(speed)
        print(f"Coral intake moving at {speed}")

    def stop(self):
        motor2.set(0)
        print("Coral intake stopped")

class AlgaeIntake:
    def __init__(self, motor_id):
        motor3.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the algae intake motor speed (-1 to 1)."""
        motor3.set(speed)
        print(f"Algae intake moving at {speed}")

    def stop(self):
        motor3.set(0)
        print("Algae intake stopped")

class DeepCage:
    def __init__(self, motor_id):
        motor4.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the deep cage motor speed (-1 to 1)."""
        motor4.set(speed)
        print(f"Deep cage moving at {speed}")

    def stop(self):
        motor4.set(0)
        print("Deep cage stopped")


#This is incomplete code. It is meant to be used as a reference for the user to have something to start with.
#Have fun coding!
