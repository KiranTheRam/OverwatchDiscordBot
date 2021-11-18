import json
import requests
if __name__ == '__main__':
    baseUrl = "http://owapi.io/profile/[PLATFORM]/[REGION]/[USERNAME]-[TAG]"

    # For user input
    # userPlatform = input("Enter platform: ")
    # userRegion = input("Enter region: ")
    # userUsername = input("Enter username: ")
    # userTag = input("Enter tag: ")

    # For testing
    userPlatform = "pc"
    userRegion = "us"
    userUsername = "GhostKiller"
    userTag = "11710"

    baseUrl = baseUrl.replace("[PLATFORM]", userPlatform)
    baseUrl = baseUrl.replace("[REGION]", userRegion)
    baseUrl = baseUrl.replace("[USERNAME]", userUsername)
    baseUrl = baseUrl.replace("[TAG]", userTag)

    response = requests.get(baseUrl)

    print(response.json())


