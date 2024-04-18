import curses
import time
import tuya_scripts
from curses.textpad import rectangle


def mainWindow(stdscr):
    # Initialise color attributes
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


def main(stdscr):
    # Initialise color attributes
    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    #
    # # Define color constants
    # BLUE_AND_BLACK = curses.color_pair(1)
    #
    # # Define variables
    # width = 40
    # height = 20
    # title = " Kogan Air Conditioner "
    # # Add static items of the window
    # stdscr.attron(BLUE_AND_BLACK)
    # rectangle(stdscr, 0, 0, height, width)
    # stdscr.addstr(0, (width - len(title)) // 2, title)
    # stdscr.attroff(BLUE_AND_BLACK)
    #
    # # Print other screen elements
    # subtitle = ["Room", "Temperature"]
    # for index, word in enumerate(subtitle):
    #     stdscr.addstr(3 + index, (width - len(word)) // 2, word)
    # openapi, BASE_URL = tuya_scripts.connectTuya()
    # mainWindow(stdscr)

    # Get the current temperature and current temperature unit
    # curTemperature = tuya_scripts.getCurrentTemp(openapi, BASE_URL)
    # curTempUnit = tuya_scripts.getTempUnit(openapi, BASE_URL).capitalize()
    # curTempString = f"{curTemperature}º{curTempUnit}"
    # stdscr.addstr(5, (40 - len(curTempString)) // 2, curTempString)

    win = curses.newwin(10, 38, 15, 1)
    win.addstr(0, 0, "This is a test")
    rectangle(win, 2, 2, 4, 30)
    win.refresh()

    stdscr.refresh()

    time.sleep(1)
    print("Hi")


# if __name__ == "__main__":
curses.wrapper(main)
