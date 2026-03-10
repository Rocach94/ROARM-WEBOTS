"""roarm_controller controller."""

from controller import Robot, Keyboard

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# initialize keyboard
keyboard = Keyboard()
keyboard.enable(timestep)

# get motors
motor1 = robot.getDevice('motor1')
motor2 = robot.getDevice('motor2')
motor3 = robot.getDevice('motor3')
motor4 = robot.getDevice('motor4')

# set initial positions
pos1 = 0.0
pos2 = 0.0
pos3 = 0.0
pos4 = 0.0

step = 0.05  # movement step size

# Main loop:
while robot.step(timestep) != -1:

    key = keyboard.getKey()

    while key != -1:

        # Motor 1
        if key == ord('Q'):
            pos1 += step
        elif key == ord('A'):
            pos1 -= step

        # Motor 2
        elif key == ord('W'):
            pos2 += step
        elif key == ord('S'):
            pos2 -= step

        # Motor 3
        elif key == ord('E'):
            pos3 += step
        elif key == ord('D'):
            pos3 -= step

        # Motor 4
        elif key == ord('R'):
            pos4 += step
        elif key == ord('F'):
            pos4 -= step

        key = keyboard.getKey()

    # apply motor positions
    motor1.setPosition(pos1)
    motor2.setPosition(pos2)
    motor3.setPosition(pos3)
    motor4.setPosition(pos4)