# BE@R-e Controller
Python is a genus of constricting snakes in the Pythonidae family native to the tropics and subtropics of the Eastern Hemisphere. The name python was proposed by François Marie Daudin in 1803 for non-venomous flecked snakes. Currently, 10 python species are recognized as valid taxa. Pythons are especially prevalent in places such as Florida, as well as anywhere both tropical and subtropical. Burmese Pythons in particular are actually invasive to Florida, as they out compete or eat up most typical wildlife.

!!! NOTICE !!!

Veteran teams recommend Java best, due to its simplicity (similar to Python) and its extensive support from FRC. Python is supported and has all the required libraries to make a working robot, however is more or so independently translated for support. If you know Java, I would like to recommend you make a exact copy of this WORKING code but translate it to Java in case. Though since we have a perfectly working code (so much so that Sanjoe actually let me chill instead of being like "FUCKING WORK BRO") priority should go to creating the required systems for making our robot's utilities and mechanisms. We also may refer to the Kitbot, however should we follow through with a kitbot, we should decide on starter wheels or keep our mecanum wheels. It's also a suggestion from veteran teams, and we should decide either, speed or versatlity, since going for both requires LOCKING IN and maybe a lot more money. Anyways, yeah you do you, you can refer to me for any questions concerns on the coding side, as well as some general robot stuff so yeah.

RobotPy Documentation: https://robotpy.readthedocs.io/en/stable/

Python Documentation: https://docs.python.org/3/

Cy-Bears Team 10402 Page: https://tinyurl.com/cybears-team10402

Below are the instructions for Python, ROBOrio and deployment, and the to do list for the team.

----------------------------------------------------------------------------------------------------------------------

# Instructions
The Github repository is structured where "robot.py" is the main handler, the LabVIEW equivalent of "Robot Main.vi". In "commands" there are files like "teleop.py" for TeleOperated mode and "auto.py" for autonomous mode. The "constants" folder is for constant values held and shared. Changing may break code or something. Folder "subsytems" contain the drivetrain and utilities such as a ball intake. Please organize accordingly, as my expierence with being a game developer- FILE ORGANIZATION HELPS MAN so yeah you do you just don't break shit.

If RobotPy is not working on your computer or on this web, please open (the) Terminal (cmd, powershell, bash, etc) and type the following:

- pip install robotpy
- pip install wpilib
- pip install robotpy-rev
- pip install robotpy-ctre
- pip install robotpy-navx
- pip install robotpy-pathplanner
- pip install rev

If still not working, you may need to import the WPI Library. Be sure to include this in your code:

- import wpilib
- import wpilib.drive (not always, but necessary)

----------------------------------------------------------------------------------------------------------------------

To deploy to ROBOrio, open the Terminal do the following:

Install RobotPy and REV on the ROBOrio
- py -3 -m robotpy installer download robotpy
- py -3 -m robotpy installer install robotpy
- py -3 -m robotpy installer install robotpy-rev
- py -3 -m robotpy installer install [any other libraries required]

Define the path to the module. This is typically a folder. Make sure "robot.py" and "pyproject.toml" exist inside the folder that is your robot module. Format; C:\Path1\Path2\Path3\Folder
- cd C:\path1\path2\path3\Folder

Deploy the code
- python -m robotpy deploy
- py -3 -m robotpy deploy (alternate)

Additionally, you can simulate the robot:
- python -m robotpy sim
- py -3 -m robotpy sim (alternate)

As well as add Telemetry data for debugging and output reading
- wpilib.SmartDashboard.putNumber("Joystick Y", y_speed)

When simulating/executing the module code onto your computer, it should run once unless pushing out the outputs at least once and finish. You should recieve any errors along with where they occur. When deployed to a ROBORio, the wpilib Framework should handle it, which means that we can omit some parts of what you'd think should be in there, such as output update loops. Or least that's what I've learned, find out for yourself or something.

Drive logic can be handled by the FRC Driver Station, which means you can use that to switch between modes, i.e., Autonomous and TeleOperated.

-------------------------------------------------------------------------------------------------------------------------

Recommended to do this on your client (computer) and run on an environment such as VS Code. Open codespaces on VS or Github to work together in real-time.

-------------------------------------------------------------------------------------------------------------------------

# To Do List

Create a basic drivetrain.
- Begin
- Autonomous Drive (refine this)
- TeleOperation Drive

Utilities
- Sensors/Camera if needed (mechanical team aint doing shi)
- Objective Mechanism control (like a ball groper)
- Driver Station Utilities (somebody gotta work on that UI i set up the framework with Tkinter)

Refer to Bhillah Salad for more instructions if not here.
![image](https://github.com/user-attachments/assets/9ce631a5-c3f3-4c19-8374-dab1f0feef71)

Remember to ask Sanjoe if there are snacks at the competition.
