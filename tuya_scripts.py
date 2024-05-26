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
    response = openapi.get(f"{BASE_URL}/status")

    power_state = getStatus(getFullStatus(openapi, BASE_URL), "Power")
    return {"commands": [{"code": "Power", "value": not power_state}]}


def switchOnOffSelector(openapi, BASE_URL, state):
    openapi = openapi
    BASE_URL = BASE_URL

    return {"commands": [{"code": "Power", "value": state}]}


def setTempC(tempC):
    return {"commands": [{"code": "temp_set", "value": tempC}]}


def setTempUnit(unit):
    return {"commands": [{"code": "temp_c_f_set", "value": unit}]}

    # Filter the response to obtain the current temp value
    for item in response.get("result", []):

def getFullStatus(openapi, BASE_URL):
    return openapi.get(f"{BASE_URL}/status")


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


def applyCommand(openapi, BASE_URL, command):
    openapi.post(f"{BASE_URL}/commands", command)


def main():
    openapi, BASE_URL = connectTuya()
    while True:
        print("1 - Switch on/off")
        print("2 - Set the temperature")
        print("3 - Get the current temperature")
        print("4 - Get the current temperature unit")
        print("0 - Exit program")
        inputNumber = int(
            input("Which command would like to use to control the air conditioning: ")
        )
        if inputNumber not in range(5):
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
                break
            print("\n")

        if inputNumber in range(3):
            openapi.post(f"{BASE_URL}/commands", commands)


if __name__ == "__main__":
    main()
