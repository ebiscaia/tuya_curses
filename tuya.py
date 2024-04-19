import curses
import re
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

    # Rearrange status list to match the titles
    roomTemp = f"{status[7]}ºC" if status[5] == 1 else f"{status[9]}ºF"
    setTemp = f"{status[6]}ºC" if status[5] == 1 else f"{status[8]}ºF"

    finalStatus = status.copy()
    for i in range(5):
        finalStatus.pop()

    finalStatus.insert(1, setTemp)

    # Define cicle to update screen contents and capture keystrokes
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        # Leave the program
        if key == chr(27):
            break

        for index in range(len(titles)):
            color = WHITE_AND_BLACK
            if index == activeLine:
                color = YELLOW_AND_BLACK
            stdscr.addstr(3 + index, 3, titles[index], color)
            stdscr.addstr(
                3 + index,
                width - 4 - len(str(finalStatus[index])),
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
            width - 4 - len(roomTemp),
            roomTemp,
            YELLOW_AND_BLACK | curses.A_REVERSE | curses.A_BOLD,
        )



def main(stdscr):
    # Define some curses properties
    stdscr.nodelay(True)

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


# if __name__ == "__main__":
curses.wrapper(main)
