from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
import logging
import json


def importJson(file):
    f = open(file)
    return json.load(f)


def connectTuya():
    tuyaData = importJson("tuya.json")

    ACCESS_ID = tuyaData["access_id"]
    ACCESS_KEY = tuyaData["access_key"]

    ENDPOINT = tuyaData["endpoint"]
    # TUYA_LOGGER.setLevel(logging.DEBUG)

    AIRCON_ID = tuyaData["aircon_id"]
    BASE_URL = f"/v1.0/iot-03/devices/{AIRCON_ID}"

    openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
    openapi.connect()
    return openapi, BASE_URL


# response = openapi.get(BASE_URL)

# functions = openapi.get(f"{BASE_URL}/functions")
# commands = {"commands": [{"code": "windshake", "value": "on"}]}
# result = openapi.post(f"{BASE_URL}/commands", commands)
# response = openapi.get(f"{BASE_URL}/status")

# Filter the response to obtain the current temp value
# for item in response.get("result", []):
#     if item.get("code") == "temp_current":
#         temp_value = item.get("value")
#         break
#
# print(f"Current temp: {temp_value}")

# Implement some pratical functionality
# Switch the air con


def switchOnOff(openapi, BASE_URL):
    openapi = openapi
    BASE_URL = BASE_URL

    power_state = getStatus(getFullStatus(openapi, BASE_URL), "Power")
    return {"commands": [{"code": "Power", "value": not power_state}]}


def switchOnOffSelector(openapi, BASE_URL, state):
    openapi = openapi
    BASE_URL = BASE_URL

    return {"commands": [{"code": "Power", "value": state}]}


def setTemp(tempUnit, tempValue):
    if tempUnit == 1:
        code = "temp_set"
    else:
        code = "temp_set_f"
    return {"commands": [{"code": code, "value": tempValue}]}


def setTempUnit(openapi, BASE_URL, unit):
    fullStatus = getFullStatus(openapi, BASE_URL)
    tempC = getStatus(fullStatus, "temp_set")
    tempF = getStatus(fullStatus, "temp_set_f")

    if unit == 1:
        return {"commands": [{"code": "temp_set", "value": tempC}]}
    else:
        return {"commands": [{"code": "temp_set_f", "value": tempF}]}


def getFullStatus(openapi, BASE_URL):
    return openapi.get(f"{BASE_URL}/status")


def getStatus(status, statusItem):
    for item in status.get("result", []):
        if item.get("code") == statusItem:
            statusValue = item.get("value")
    return statusValue


def getPowerState(openapi, BASE_URL):
    response = openapi.get(f"{BASE_URL}/status")

    # Filter the response to obtain the current power state
    for item in response.get("result", []):
        if item.get("code") == "Power":
            power = item.get("value")
    return power


def getCurrentTemp(openapi, BASE_URL):
    response = openapi.get(f"{BASE_URL}/status")

    # Filter the response to obtain the current temp value
    for item in response.get("result", []):
        if item.get("code") == "temp_current":
            temp_value = item.get("value")
    return temp_value


def getTempUnit(openapi, BASE_URL):
    response = openapi.get(f"{BASE_URL}/status")

    # Filter the response to obtain the current temp value
    for item in response.get("result", []):
        if item.get("code") == "funcTag":
            temp_value = item.get("value")
    return temp_value


def setFanSpeed(openapi, BASE_URL, state):
    return {"commands": [{"code": "windspeed", "value": state}]}


def setOscilation(openapi, BASE_URL, state):
    return {"commands": [{"code": "windshake", "value": state}]}


def setMode(openapi, BASE_URL, state):
    return {"commands": [{"code": "mode", "value": state}]}


def applyCommand(openapi, BASE_URL, command):
    openapi.post(f"{BASE_URL}/commands", command)


def main():
    openapi, BASE_URL = connectTuya()
    while True:
        print("1 - Switch on/off")
        print("2 - Set the temperature")
        print("3 - Get the current temperature")
        print("4 - Get the current temperature unit")
        print("5 - Set the temperature unit")
        print("6 - Select fan speed")
        print("7 - Select oscilation mode")
        print("8 - Select cooling mode")
        print("0 - Exit program")
        inputNumber = int(
            input("Which command would like to use to control the air conditioning: ")
        )
        if inputNumber not in range(5):
        if inputNumber not in range(7):
            print("Please use one of the options shown\n")
            continue
        if inputNumber == 0:
            print("Exiting program.")
            break

        while True:
            if inputNumber == 1:
                commands = switchOnOff(openapi, BASE_URL)
                break
            if inputNumber == 2:
                tempNumber = int(
                    input(
                        "Select the air conditioning temperature in Celsius (16-31): "
                    )
                )
                if tempNumber < 16:
                    print(
                        "Temperature below minimal limit of 16. Using 16 as desired temperature"
                    )
                    tempNumber = 16
                if tempNumber > 31:
                    print(
                        "Temperature above above limit of 31. Using 31 as desired temperature"
                    )
                    tempNumber = 31
                commands = setTempC(tempNumber)
                break
            if inputNumber == 3:
                temp = getCurrentTemp(openapi, BASE_URL)
                print(f"Room temperature: {temp}")
                break
            if inputNumber == 4:
                curTemp = getStatus(openapi, BASE_URL, "funcTag")
                if curTemp == 1:
                    curTemp = "Celsius"
                else:
                    curTemp = "Fahrenheit"
                print(f"Temperature Unit: {curTemp}")
            if inputNumber == 5:
                print("1 - Celsius")
                print("2 - Fahrenheit")
                print("0 - Return to previous menu")
                tempUnitOption = int(
                    input("\nSelect option to set the temperature unit: ")
                )
                if tempUnitOption not in range(3):
                    print("Please choose one of the option below")
                    continue
                if tempUnitOption == 0:
                    break
                else:
                    commands = setTempUnit(openapi, BASE_URL, tempUnitOption)

                break
            if inputNumber == 7:
                titles = ["On", "Off"]
                for index, text in enumerate(titles):
                    print(f"{index+1} - {text}")

                oscilationSelectionNumber = int(
                    input("\nSelect option to set the oscilation mode: ")
                )

                if oscilationSelectionNumber not in range(1, len(titles) + 1):
                    print("Please choose one of the option below")
                    continue

                oscilationSelection = titles[oscilationSelectionNumber - 1].lower()
                commands = setOscilation(openapi, BASE_URL, oscilationSelection)
                break
            print("\n")
            if inputNumber == 8:
                titles = ["Cool", "Dry", "Fan"]
                for index, text in enumerate(titles):
                    print(f"{index+1} - {text}")

                modeNumber = int(input("\nSelect option to set the cooling mode: "))

                if modeNumber not in range(1, len(titles) + 1):
                    print("Please choose one of the option below")
                    continue

                modeSelection = titles[modeNumber - 1].lower()
                if modeSelection == "cool":
                    modeSelection = "cold"
                if modeSelection == "dry":
                    modeSelection = "wet"
                if modeSelection == "fan":
                    modeSelection = "wind"
                commands = setMode(openapi, BASE_URL, modeSelection)
                break
            print("\n")

        if inputNumber in range(3) or inputNumber in range(5, 7):
            applyCommand(openapi, BASE_URL, commands)


if __name__ == "__main__":
    main()
