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


def switchOnOffWindow(color):
    heightw, widthw = 10, 40
    start_y, start_x = (curses.LINES - heightw) // 2, (curses.COLS - widthw) // 2
    winTitle = " Turn On/Off Air Conditioner "

    statesList = ["On", "Off"]
    activeLine = 0

    win = curses.newwin(heightw, widthw, start_y, start_x)
    win.bkgd(" ", color)
    win.border()
    win.nodelay(True)

    # Title and message in the new window
    win.addstr(0, (widthw - len(winTitle)) // 2, winTitle, color | curses.A_BOLD)
    # Add window loop

    for index, state in enumerate(statesList):
        spaceCount = widthw - (len(state) + 4)
        win.addstr(2 + index, 2, state + spaceCount * " ", color)
        if index == activeLine:
            win.addstr(2 + index, 2, state + spaceCount * " ", color | curses.A_REVERSE)

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
