import curses


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
