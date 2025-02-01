# BEAR-e-controller
Pythons are a type of snake, that are especially prevalent in places such as Florida. Burmese Pythons are actually invasive to Florida, as they out compete or eat up most typical wildlife.

RobotPy Documentation: https://robotpy.readthedocs.io/en/stable/

Below are the instructions for Python, ROBOrio and deployment, and the to do list for the team.

----------------------------------------------------------------------------------------------------------------------

# Instructions
If RobotPy is not working on your computer or on this web, please open (the) Terminal and type the following:

pip install robotpy

pip install robotpy-rev

pip install robotpy-ctre

pip install robotpy-navx

pip install robotpy-pathplanner

----------------------------------------------------------------------------------------------------------------------

To deploy to ROBOrio, do the following:
- Install RobotPy on the ROBOrio
  
py -3 -m robotpy_installer download robotpy

py -3 -m robotpy_installer install robotpy

- Deploy the code
  
py -3 -m robotpy deploy

- Additionally, you can simulate

py -3 -m robotpy sim

- As well as add Telemetry data for debugging and output reading

wpilib.SmartDashboard.putNumber("Joystick Y", y_speed)

-------------------------------------------------------------------------------------------------------------------------

Recommended to do this on your client (computer) and run on an environment such as VS Code. Open codespaces on VS or Github to work together in real-time.

-------------------------------------------------------------------------------------------------------------------------

# To Do List

Create a basic drivetrain.
- Begin
- Drive (Autonoumous)
- Drive (TeleOperated)

Utilities
- Sensors/Camera if needed
- Objective Mechanism control

Refer to Dhillan for more instructions if not here.
