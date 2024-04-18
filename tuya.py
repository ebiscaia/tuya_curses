import curses
import time
import tuya_scripts
from curses.textpad import rectangle


def mainWindow(stdscr):
    # Initialise color attributes
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Define color constants
    WHITE_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    # Define variables
    height, width = stdscr.getmaxyx()
    title = " Kogan Air Conditioner "
    # Add static items of the window
    stdscr.attron(GREEN_AND_BLACK)
    rectangle(stdscr, 0, 0, height, width)
    stdscr.addstr(0, (width - len(title)) // 2, title)
    stdscr.attroff(GREEN_AND_BLACK)

    # Print other screen elements
    subtitle = ["Room", "Temperature"]
    for index, word in enumerate(subtitle):
        stdscr.addstr(3 + index, (width - len(word)) // 2, word)

    win = curses.newwin(10, 38, 15, 1)
    win.addstr(0, 0, "This is a test")
    rectangle(win, 2, 2, 4, 30)
    win.refresh()

    stdscr.refresh()

    time.sleep(1)
    print("Hi")


# if __name__ == "__main__":
curses.wrapper(main)
