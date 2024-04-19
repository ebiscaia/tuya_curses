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
    rectangle(stdscr, 0, 0, height - 2, width - 2)
    stdscr.addstr(0, (width - len(title)) // 2, title)
    stdscr.attroff(GREEN_AND_BLACK)

    # Print other screen elements
    subtitle = ["Room", "Temperature"]
    for index, word in enumerate(subtitle):
        stdscr.addstr(3 + index, (width - len(word)) // 2, word)


def airConStatus():
    openapi, BASE_URL = tuya_scripts.connectTuya()


def main(stdscr):
    # Start connection with the air conditioner
    openapi, BASE_URL = tuya_scripts.connectTuya()

    # Get the initial values from the air conditioner
    curPowerState = tuya_scripts.getStatus(openapi, BASE_URL, "Power")
    curMode = tuya_scripts.getStatus(openapi, BASE_URL, "mode")
    curFanMode = tuya_scripts.getStatus(openapi, BASE_URL, "windspeed")
    curOscilationState = tuya_scripts.getStatus(openapi, BASE_URL, "windshake")
    curSleepState = tuya_scripts.getStatus(openapi, BASE_URL, "Sleeping_mode")

    # Get unit in use and get values of variables that depende on the
    # temperature unit
    curTempUnit = tuya_scripts.getStatus(openapi, BASE_URL, "funcTag")
    curRoomTemp = tuya_scripts.getStatus(
        openapi, BASE_URL, "temp_current" if curTempUnit == 1 else "temp_current_f"
    )

    curTempString = f"{curRoomTemp}ºC" if curTempUnit == 1 else f"{curRoomTemp}ºF"

    stdscr.addstr(5, (40 - len(curTempString)) // 2, "On" if curPowerState else "Off")
    # stdscr.addstr(5, (40 - len(curTempString)) // 2, curTempString)

    stdscr.getkey()


# if __name__ == "__main__":
curses.wrapper(main)
