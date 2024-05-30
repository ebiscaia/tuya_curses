import curses
import tuya_scripts


def windowTest(color):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Curses Window "

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.bkgd(" ", color)
    win.border()

    # Title and message in the new window
    win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)
    win.addstr(2, 1, "You pressed ", color)
    win.addstr(
        heightw - 1,
        2,
        " Press any key to leave the window ",
        color,
    )
    win.refresh()

    # Wait for another key press to close the window
    win.getch()
    del win


def switchOnOffWindow(openapi, BASE_URL, color):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Turn On/Off Air Conditioner "

    statesList = ["On", "Off"]
    activeLine = 0

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.nodelay(True)
    win.keypad(True)

    # Add window loop

    while True:
        try:
            key = win.getkey()
        except:
            key = None

        # Start Window
        win.clear()
        win.bkgd(" ", color)
        win.border()

        # Title and message in the new window
        win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)

        for index, state in enumerate(statesList):
            spaceCount = widthw - (len(state) + 4)
            win.addstr(2 + index, 2, state + spaceCount * " ", color)
            if index == activeLine:
                win.addstr(
                    2 + index, 2, state + spaceCount * " ", color | curses.A_REVERSE
                )

        win.addstr(
            heightw - 1,
            2,
            " Press any key to leave the window ",
            color,
        )
        win.refresh()
        curses.napms(100)

        if key == chr(10):
            command = tuya_scripts.switchOnOffSelector(
                openapi, BASE_URL, not bool(activeLine)
            )
            tuya_scripts.applyCommand(openapi, BASE_URL, command)
            key = chr(27)

        # Wait for another key press to close the window
        if key == chr(27):
            del win
            break

        # Scroll through the options
        if key == "KEY_DOWN":
            activeLine += 1
        if key == "KEY_UP":
            activeLine -= 1

        # Control the variable so that highlight will not disappear
        activeLine %= 2


def selectFanSpeedWindow(openapi, BASE_URL, color):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Select Fan Speeed "

    statesList = ["High", "Low"]
    activeLine = 0

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.nodelay(True)
    win.keypad(True)

    # Add window loop

    while True:
        try:
            key = win.getkey()
        except:
            key = None

        # Start Window
        win.clear()
        win.bkgd(" ", color)
        win.border()

        # Title and message in the new window
        win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)

        for index, state in enumerate(statesList):
            spaceCount = widthw - (len(state) + 4)
            win.addstr(2 + index, 2, state + spaceCount * " ", color)
            if index == activeLine:
                win.addstr(
                    2 + index, 2, state + spaceCount * " ", color | curses.A_REVERSE
                )

        win.addstr(
            heightw - 1,
            2,
            " Press any key to leave the window ",
            color,
        )
        win.refresh()
        curses.napms(100)

        if key == chr(10):
            selector = statesList[activeLine].lower()
            command = tuya_scripts.setFanSpeed(openapi, BASE_URL, selector)
            tuya_scripts.applyCommand(openapi, BASE_URL, command)
            key = chr(27)

        # Wait for another key press to close the window
        if key == chr(27):
            del win
            break

        # Scroll through the options
        if key == "KEY_DOWN":
            activeLine += 1
        if key == "KEY_UP":
            activeLine -= 1

        # Control the variable so that highlight will not disappear
        activeLine %= 2


def selectOscilationWindow(openapi, BASE_URL, color):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Select Oscilation Mode "

    statesList = ["On", "Off"]
    activeLine = 0

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.nodelay(True)
    win.keypad(True)

    # Add window loop

    while True:
        try:
            key = win.getkey()
        except:
            key = None

        # Start Window
        win.clear()
        win.bkgd(" ", color)
        win.border()

        # Title and message in the new window
        win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)

        for index, state in enumerate(statesList):
            spaceCount = widthw - (len(state) + 4)
            win.addstr(2 + index, 2, state + spaceCount * " ", color)
            if index == activeLine:
                win.addstr(
                    2 + index, 2, state + spaceCount * " ", color | curses.A_REVERSE
                )

        win.addstr(
            heightw - 1,
            2,
            " Press any key to leave the window ",
            color,
        )
        win.refresh()
        curses.napms(100)

        if key == chr(10):
            selector = statesList[activeLine].lower()
            command = tuya_scripts.setOscilation(openapi, BASE_URL, selector)
            tuya_scripts.applyCommand(openapi, BASE_URL, command)
            key = chr(27)

        # Wait for another key press to close the window
        if key == chr(27):
            del win
            break

        # Scroll through the options
        if key == "KEY_DOWN":
            activeLine += 1
        if key == "KEY_UP":
            activeLine -= 1

        # Control the variable so that highlight will not disappear
        activeLine %= 2


def selectModeWindow(openapi, BASE_URL, color):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Select Oscilation Mode "

    statesList = ["Cool", "Dry", "Fan"]
    activeLine = 0

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.nodelay(True)
    win.keypad(True)

    # Add window loop

    while True:
        try:
            key = win.getkey()
        except:
            key = None

        # Start Window
        win.clear()
        win.bkgd(" ", color)
        win.border()

        # Title and message in the new window
        win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)

        for index, state in enumerate(statesList):
            spaceCount = widthw - (len(state) + 4)
            win.addstr(2 + index, 2, state + spaceCount * " ", color)
            if index == activeLine:
                win.addstr(
                    2 + index, 2, state + spaceCount * " ", color | curses.A_REVERSE
                )

        win.addstr(
            heightw - 1,
            2,
            " Press any key to leave the window ",
            color,
        )
        win.refresh()
        curses.napms(100)

        if key == chr(10):
            selector = statesList[activeLine].lower()
            if selector == "cool":
                selector = "cold"
            if selector == "dry":
                selector = "wet"
            if selector == "fan":
                selector = "wind"
            command = tuya_scripts.setMode(openapi, BASE_URL, selector)
            tuya_scripts.applyCommand(openapi, BASE_URL, command)
            key = chr(27)

        # Wait for another key press to close the window
        if key == chr(27):
            del win
            break

        # Scroll through the options
        if key == "KEY_DOWN":
            activeLine += 1
        if key == "KEY_UP":
            activeLine -= 1

        # Control the variable so that highlight will not disappear
        activeLine %= len(statesList)


def selectTempUnitWindow(openapi, BASE_URL, color):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Select Oscilation Mode "

    statesList = ["Celsius", "Fahrenheit"]
    activeLine = 0

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.nodelay(True)
    win.keypad(True)

    # Add window loop

    while True:
        try:
            key = win.getkey()
        except:
            key = None

        # Start Window
        win.clear()
        win.bkgd(" ", color)
        win.border()

        # Title and message in the new window
        win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)

        for index, state in enumerate(statesList):
            spaceCount = widthw - (len(state) + 4)
            win.addstr(2 + index, 2, state + spaceCount * " ", color)
            if index == activeLine:
                win.addstr(
                    2 + index, 2, state + spaceCount * " ", color | curses.A_REVERSE
                )

        win.addstr(
            heightw - 1,
            2,
            " Press any key to leave the window ",
            color,
        )
        win.refresh()
        curses.napms(100)

        if key == chr(10):
            command = tuya_scripts.setTempUnit(openapi, BASE_URL, activeLine + 1)
            tuya_scripts.applyCommand(openapi, BASE_URL, command)
            key = chr(27)

        # Wait for another key press to close the window
        if key == chr(27):
            del win
            break

        # Scroll through the options
        if key == "KEY_DOWN":
            activeLine += 1
        if key == "KEY_UP":
            activeLine -= 1

        # Control the variable so that highlight will not disappear
        activeLine %= len(statesList)


def selectTempWindow(openapi, BASE_URL, color, tempValue, tempUnit):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Select air conditioner temperature "

    tempCRange = [16, 31]
    tempFRange = [61, 88]
    tempRange = tempCRange if tempUnit == 1 else tempFRange
    tempTag = "C" if tempUnit == 1 else "F"
    tempPrev = tempValue

    sliderSize = 5
    slider = f"<{"-"*sliderSize}>"

    keyCount = 0

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.nodelay(True)
    win.keypad(True)

    # Add window loop

    while True:
        try:
            key = win.getkey()
            keyCount = 0
        except:
            key = None
            keyCount += 1

        # Start Window
        win.clear()
        win.bkgd(" ", color)
        win.border()

        # Title and message in the new window
        tempText = f"{tempValue}º{tempTag}"
        win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)
        win.addstr(heightw // 2 - 1, (widthw - len(tempText)) // 2, tempText, color)
        win.addstr(heightw // 2, (widthw - len(slider)) // 2, slider, color)

        knobPos = (widthw - len(slider)) // 2 + 1
        knobPos += round(
            (tempValue - tempRange[0])
            / (tempRange[1] - tempRange[0])
            * (sliderSize - 1)
        )
        win.addstr(heightw // 2, knobPos, "*", color)

        win.addstr(
            heightw - 1,
            2,
            " Press any key to leave the window ",
            color,
        )

        if keyCount > 15 and tempPrev != tempValue:
            text = "Changing air conditioner temperature"
            win.addstr(
                heightw // 2 + 2,
                (widthw - len(text)) // 2,
                text,
                color | curses.A_REVERSE,
            )
            command = tuya_scripts.setTemp(tempUnit, tempValue)
            tuya_scripts.applyCommand(openapi, BASE_URL, command)
            tempPrev = tempValue
            keyCount = 0
            win.refresh()
            curses.napms(500)

        if key == chr(10):
            command = tuya_scripts.setTemp(tempUnit, tempValue)
            tuya_scripts.applyCommand(openapi, BASE_URL, command)
            key = chr(27)

        # Wait for another key press to close the window
        if key == chr(27):
            del win
            break

        # Scroll through the options
        if key == "KEY_RIGHT":
            tempValue += 1
        if key == "KEY_LEFT":
            tempValue -= 1

        # Control the variable so that temperatures out of the range will not be
        # chosen
        tempValue = min(tempRange[1], max(tempValue, tempRange[0]))

        win.refresh()
        curses.napms(100)
