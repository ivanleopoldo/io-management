from core.fcfs import fcfs
from core.cscan import cscan
from core.clook import clook

if __name__ == "__main__":
    track_size = int(input("Enter track size: "))
    initial = int(input("Enter current position: "))
    queue = list(
        map(int, input("Enter request queue (separate using spaces): ").split(" "))
    )
    seek_rate = int(input("Enter seek rate: "))
    alpha = int(input("Enter alpha: "))

    fcfs(track_size, initial, queue, seek_rate)
    cscan(track_size, initial, queue, seek_rate, alpha)
    clook(track_size, initial, queue, seek_rate, alpha)
