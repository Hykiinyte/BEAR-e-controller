import wpilib
import rev
import time

class MotorController:
    def __init__(self, device_id, inverted=False):
        self.motor = rev.SparkMax(device_id, rev.SparkMax.MotorType.kBrushless)
        self.motor.setInverted(inverted)

    def set(self, speed):
        self.motor.set(speed)

    def stop(self):
        self.set(0)


class Elevator:
    # Assume 1 second per level change for this example.
    LEVEL_TIME = 1.0

    def __init__(self, motor1: MotorController, motor2: MotorController):
        self.motor1 = motor1
        self.motor2 = motor2
        self.current_level = 0  # Levels: 0 (base) to 4 (top)
        self.target_level = 0
        self.speed = 0.5
        self.moving = False
        self.move_start_time = None
        self.move_duration = 0

    def move_manual(self, speed):
        self.motor1.set(speed)
        self.motor2.set(-speed)
        self.moving = True

    def stop(self):
        self.motor1.stop()
        self.motor2.stop()
        self.moving = False
        self.move_start_time = None

    def set_position(self, target_level):
        # If already at target, do nothing.
        if target_level == self.current_level:
            return

        diff = target_level - self.current_level
        direction = 1 if diff > 0 else -1
        # Set the movement duration (assume LEVEL_TIME per level change)
        self.move_duration = abs(diff) * self.LEVEL_TIME
        self.move_start_time = time.time()
        self.target_level = target_level

        # Start moving both motors in opposite directions
        self.motor1.set(self.speed * direction)
        self.motor2.set(-self.speed * direction)
        self.moving = True

    def update(self):
        # This method should be called periodically (e.g., in teleop's update loop)
        if self.moving and self.move_start_time is not None:
            elapsed = time.time() - self.move_start_time
            if elapsed >= self.move_duration:
                self.stop()
                self.current_level = self.target_level
                print(f"Elevator set to level {self.current_level}")


class CoralIntake:
    def __init__(self, motor: MotorController):
        self.motor = motor

    def move(self, speed):
        self.motor.set(speed)

    def stop(self):
        self.motor.stop()


class AlgaeIntake:
    def __init__(self, motor: MotorController):
        self.motor = motor

    def move(self, speed):
        self.motor.set(speed)

    def stop(self):
        self.motor.stop()


class DeepCage:
    def __init__(self, motor: MotorController):
        self.motor = motor

    def move(self, speed):
        self.motor.set(speed)

    def stop(self):
        self.motor.stop()
