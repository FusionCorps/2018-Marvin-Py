
from wpilib import Joystick
from wpilib.buttons import Button, JoystickButton

import robotmap


def init():
    global joystick, A

    joystick = Joystick(robotmap.joystick)
    A = JoystickButton(joystick, 1)
    B = JoystickButton(joystick, 2)
    X = JoystickButton(joystick, 3)
    Y = JoystickButton(joystick, 4)
    bumper_L = JoystickButton(joystick, 5)
    bumper_R = JoystickButton(joystick, 6)
    back = JoystickButton(joystick, 7)
    start = JoystickButton(joystick, 8)
    stick_L = JoystickButton(joystick, 9)
    stick_R = JoystickButton(joystick, 10)