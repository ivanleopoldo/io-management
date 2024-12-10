from core.fcfs import fcfs
from core.cscan import cscan
from core.clook import clook
from InquirerPy import prompt
from lib.config import openConfig, saveConfig

if __name__ == "__main__":
    config = openConfig()
    questions = [
        {
            "type": "number",
            "name": "track_size",
            "message": "Enter track size:",
            "default": int(config["track_size"]),
        },
        {
            "type": "number",
            "name": "initial",
            "message": "Enter current position:",
            "default": int(config["initial"]),
        },
        {
            "type": "input",
            "name": "queue",
            "message": "Enter request queue (separate using spaces):",
            "default": str(config["queue"]),
        },
        {
            "type": "number",
            "name": "seek_rate",
            "message": "Enter seek rate:",
            "default": int(config["seek_rate"]),
        },
        {
            "type": "number",
            "name": "alpha",
            "message": "Enter alpha:",
            "default": int(config["alpha"]),
        },
    ]

    answers = prompt(questions)
    saveConfig(
        {
            "track_size": int(answers["track_size"]),
            "initial": int(answers["initial"]),
            "queue": str(answers["queue"]),
            "seek_rate": int(answers["seek_rate"]),
            "alpha": int(answers["alpha"]),
        }
    )

    queue = list(map(int, answers["queue"].split(" ")))

    fcfs(config["track_size"], config["initial"], queue, config["seek_rate"])
    print("-" * 50)
    cscan(
        config["track_size"],
        config["initial"],
        queue,
        config["seek_rate"],
        config["alpha"],
    )
    print("-" * 50)
    clook(
        config["track_size"],
        config["initial"],
        queue,
        config["seek_rate"],
        config["alpha"],
    )
