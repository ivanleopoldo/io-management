def fcfs(track_size, initial, queue, seek_rate):
    path = [initial] + queue

    thm = sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))

    sk = thm * seek_rate

    print("\nFCFS:")
    for i, track in enumerate(path):
        if track < track_size:
            if i == 0:
                print(f"Start at {track}")
            else:
                print(f"Move to {track} (Distance: {abs(path[i] - path[i - 1])})")
        else:
            print("Track out of bounds")
            break

    print("\nSummary:")
    print(f"Total Head Movement (THM): {thm}")
    print(f"Seek Time (SK): {sk}")
