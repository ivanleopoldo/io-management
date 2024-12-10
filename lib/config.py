import json


def openConfig(configPath="config.json"):
    with open(configPath, "r") as configFile:
        return json.load(configFile)


def saveConfig(config, configPath="config.json"):
    with open(configPath, "w") as configFile:
        json.dump(config, configFile, indent=4)
