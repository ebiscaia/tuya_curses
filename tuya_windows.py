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
    win.bkgd(" ", color)
    win.border()
    win.nodelay(True)
    win.keypad(True)

    # Add window loop

    while True:
        try:
            key = win.getkey()
        except:
            key = None

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
