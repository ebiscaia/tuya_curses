import curses
import time
import tuya_scripts
from curses.textpad import rectangle


def mainWindow(stdscr, status):
    # Initialise color attributes
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Define color constants
    WHITE_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    YELLOW_AND_BLACK = curses.color_pair(3)

    # Define variables
    height, width = stdscr.getmaxyx()
    title = " Kogan Air Conditioner "
    activeLine = 1

    # Add static items of the window
    stdscr.attron(GREEN_AND_BLACK)
    rectangle(stdscr, 0, 0, height - 2, width - 2)
    stdscr.addstr(0, (width - len(title)) // 2, title)
    stdscr.attroff(GREEN_AND_BLACK)

    # Print the section titles:
    titles = [
        "Power:",
        "Temperature:",
        "Mode",
        "Fan Speed:",
        "Oscilation:",
        "Sleep Mode:",
    ]
    mockData = ["On", "13C", "Cool", "Low", "Off", "On"]

    # Rearrange status list to match the titles
    roomTemp = f"{status[7]}ºC" if status[5] == 1 else f"{status[9]}ºF"
    setTemp = f"{status[6]}ºC" if status[5] == 1 else f"{status[8]}ºF"

    for index in range(len(titles)):
        stdscr.addstr(3 + index, 3, titles[index])
        stdscr.addstr(3 + index, width - 4 - len(mockData[index]), mockData[index])

    # Statusbar
    stdscr.addstr(height - 3, 2, " " * (width - 6), curses.A_REVERSE)
    stdscr.addstr(height - 3, 2, "Room Temperature: ", curses.A_REVERSE)
    stdscr.addstr(height - 3, width - 4 - len("15C"), "15C", curses.A_REVERSE)


def main(stdscr):
    # Start connection with the air conditioner
    openapi, BASE_URL = tuya_scripts.connectTuya()

    # Get the initial values from the air conditioner
    statusPar = [
        "Power",
        "mode",
        "windspeed",
        "windshake",
        "Sleeping_mode",
        "funcTag",
        "temp_set",
        "temp_current",
        "temp_set_f",
        "temp_current_f",
    ]

    statusVal = []
    for param in statusPar:
        value = tuya_scripts.getStatus(openapi, BASE_URL, param)
        statusVal.append(value)

    # stdscr.addstr(5, (40 - len(curTempString)) // 2, "On" if curPowerState else "Off")
    # stdscr.addstr(5, (40 - len(curTempString)) // 2, curTempString)

    mainWindow(stdscr, statusVal)
    stdscr.getkey()


# if __name__ == "__main__":
curses.wrapper(main)
