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
    def __init__(self, motor_id):
        motor1.setInverted(False)  # Adjust inversion as needed

    def move(self, speed):
        """Sets the elevator motor speed (-1 to 1)."""
        motor1.set(speed)
        print(f"Elevator moving at {speed}")

    elevator_level = 0
    elevator_speed = 0.5
    base = 0
    low = 1
    mid = 2
    high = 3
    top = 4
    def setpos(self, level):
        if level == 0:
            if level == 0:
                self.elevator_level = self.base
                print("Elevator set to base")
            elif level == 1:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.low
            elif level == 2:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(2000)
                self.motor1.set(0)
                self.elevator_level = self.mid
            elif level == 3:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(3000)
                self.motor1.set(0)
                self.elevator_level = self.high
            elif level == 4:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(4000)
                self.motor1.set(0)
                self.elevator_level = self.top
        elif level == 1:
            if level == 0:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.base
            elif level == 1:
                self.elevator_level = self.low
                print("Elevator set to low")
            elif level == 2:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.mid
            elif level == 3:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(2000)
                self.motor1.set(0)
                self.elevator_level = self.high
            elif level == 4:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(3000)
                self.motor1.set(0)
                self.elevator_level = self.top
        elif level == 2:
            if level == 0:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(2000)
                self.motor1.set(0)
                self.elevator_level = self.base
            elif level == 1:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.low
            elif level == 2:
                self.elevator_level = self.mid
                print("Elevator set to mid")
            elif level == 3:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.high
            elif level == 4:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(2000)
                self.motor1.set(0)
                self.elevator_level = self.top
        elif level == 3:
            if level == 0:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(3000)
                self.motor1.set(0)
                self.elevator_level = self.base
            elif level == 1:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(2000)
                self.motor1.set(0)
                self.elevator_level = self.low
            elif level == 2:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.mid
            elif level == 3:
                self.elevator_level = self.high
                print("Elevator set to high")
            elif level == 4:
                self.motor1.set(self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.top
        elif level == 4:
            if level == 0:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(4000)
                self.motor1.set(0)
                self.elevator_level = self.base
            elif level == 1:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(3000)
                self.motor1.set(0) 
                self.elevator_level = self.low
            elif level == 2:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(2000)
                self.motor1.set(0)
                self.elevator_level = self.mid
            elif level == 3:
                self.motor1.set(-1 * self.elevator_speed)
                pygame.time.wait(1000)
                self.motor1.set(0)
                self.elevator_level = self.high
            elif level == 4:
                self.elevator_level = self.top
                print("Elevator set to top")

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
