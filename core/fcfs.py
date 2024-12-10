def fcfs(track_size, initial, queue, seek_rate):
    path = [initial] + queue

    thm = sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))

    sk = thm * seek_rate

    print("\nFCFS:")
    for i, track in enumerate(path):
        if i == 0:
            print(f"Start at {track}")
        else:
            print(f"Move to {track} (Distance: {abs(path[i] - path[i - 1])})")

    print("\nSummary:")
    print(f"Total Head Movement (THM): {thm}")
    print(f"Seek Time (SK): {sk}")
