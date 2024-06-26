import curses
import re
import tuya_scripts
import tuya_windows


def mainWindow(openapi, BASE_URL, stdscr, status):
    # Initialise color attributes
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)

    # Define color constants
    WHITE_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    YELLOW_AND_BLACK = curses.color_pair(3)
    BLACK_AND_RED = curses.color_pair(4)

    # Define variables
    height, width = stdscr.getmaxyx()
    title = " Kogan Air Conditioner "
    activeLine = 0

    # Print the section titles:
    titles = [
        "Power:",
        "Temperature:",
        "Temp. Unit:",
        "Mode:",
        "Fan Speed:",
        "Oscilation:",
        "Sleep Mode:",
    ]

    # Set variables with user friendly values
    roomTemp = f"{status[7]}ºC" if status[5] == 1 else f"{status[9]}ºF"
    setTempValue = status[6] if status[5] == 1 else status[8]
    setTemp = f"{setTempValue}ºC" if status[5] == 1 else f"{setTempValue}ºF"
    tempUnit = "Celsius" if status[5] == 1 else "F/heit"

    # Rearrange status list to match the titles
    finalStatus = status.copy()
    for i in range(5):
        finalStatus.pop()

    finalStatus.insert(1, setTemp)
    finalStatus.insert(2, tempUnit)

    # Define cicle to update screen contents and capture keystrokes
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        # Add static items of the window
        stdscr.attron(GREEN_AND_BLACK)
        stdscr.border()
        stdscr.addstr(0, (width - len(title)) // 2, title)
        stdscr.attroff(GREEN_AND_BLACK)

        for index in range(len(titles)):
            color = WHITE_AND_BLACK
            if index == activeLine:
                color = YELLOW_AND_BLACK
            stdscr.addstr(3 + index, 3, titles[index], color)
            stdscr.addstr(
                3 + index,
                width - 10,
                (
                    str(finalStatus[index]).capitalize()
                    if re.search("^[a-zA-Z]", str(finalStatus[index]))
                    else str(finalStatus[index])
                ),
                color,
            )

        # Statusbar
        stdscr.addstr(
            height - 3, 2, " " * (width - 6), YELLOW_AND_BLACK | curses.A_REVERSE
        )
        stdscr.addstr(
            height - 3,
            2,
            "Room Temperature: ",
            YELLOW_AND_BLACK | curses.A_REVERSE | curses.A_BOLD,
        )
        stdscr.addstr(
            height - 3,
            width - 10,
            roomTemp,
            YELLOW_AND_BLACK | curses.A_REVERSE | curses.A_BOLD,
        )

        stdscr.refresh()
        curses.napms(100)

        # Controls of the main Window
        # Leave the program
        if key == chr(27):
            break

        # Scroll through the options
        if key == "KEY_DOWN":
            activeLine += 1
        if key == "KEY_UP":
            activeLine -= 1

        # Control the variable so that highlight will not disappear
        activeLine = min(max(0, activeLine), len(titles) - 1)

        if key == chr(10):
            if activeLine == 0:
                tuya_windows.switchOnOffWindow(openapi, BASE_URL, BLACK_AND_RED)
            elif activeLine == 1:
                tuya_windows.selectTempWindow(
                    openapi, BASE_URL, BLACK_AND_RED, setTempValue, status[5]
                )
            elif activeLine == 2:
                tuya_windows.selectTempUnitWindow(openapi, BASE_URL, BLACK_AND_RED)
            elif activeLine == 3:
                tuya_windows.selectModeWindow(openapi, BASE_URL, BLACK_AND_RED)
            elif activeLine == 4:
                tuya_windows.selectFanSpeedWindow(openapi, BASE_URL, BLACK_AND_RED)
            elif activeLine == 5:
                tuya_windows.selectOscilationWindow(openapi, BASE_URL, BLACK_AND_RED)
            else:
                tuya_windows.windowTest(BLACK_AND_RED)


def main(stdscr):
    # Define some curses properties
    stdscr.nodelay(True)

    # Start connection with the air conditioner
    openapi, BASE_URL = tuya_scripts.connectTuya()

    # Get all the status from the air conditioner
    fullStatus = tuya_scripts.getFullStatus(openapi, BASE_URL)

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
        value = tuya_scripts.getStatus(fullStatus, param)
        statusVal.append(value)

    # stdscr.addstr(5, (40 - len(curTempString)) // 2, "On" if curPowerState else "Off")
    # stdscr.addstr(5, (40 - len(curTempString)) // 2, curTempString)

    mainWindow(openapi, BASE_URL, stdscr, statusVal)


# if __name__ == "__main__":
curses.wrapper(main)
