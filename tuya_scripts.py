from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
import logging
import json


def importJson(file):
    f = open(file)
    return json.load(f)


def connectTuya():
    tuyaData = importJson("tuya.json")
    print(tuyaData)

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

    for item in response.get("result", []):
        if item.get("code") == "Power":
            power_state = item.get("value")
            break
    return {"commands": [{"code": "Power", "value": not power_state}]}


def setTempC(tempC):
    return {"commands": [{"code": "temp_set", "value": tempC}]}


def getPowerState(openapi, BASE_URL):
    response = openapi.get(f"{BASE_URL}/status")

    # Filter the response to obtain the current temp value
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
        if item.get("code") == "temp_c_f_set":
            temp_value = item.get("value")
    return temp_value


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
                curTemp = getTempUnit(openapi, BASE_URL)
                if curTemp == "c":
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
