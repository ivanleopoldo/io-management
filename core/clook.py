def clook(track_size, initial, queue, seek_rate, alpha):
    queue.sort()

    left = [track for track in queue if track < initial]
    right = [track for track in queue if track >= initial]

    thm = (max(right) - initial) + (max(left) - min(left)) + alpha

    sk = thm * seek_rate

    path = [initial] + right + left

    print("\nDisk Movement Visualization (C-LOOK):")
    for i, track in enumerate(path):
        if i == 0:
            print(f"Start at {track}")
        else:
            print(f"Move to {track} (Distance: {abs(path[i] - path[i - 1])})")

    print("\nSummary:")
    print(f"Total Head Movement (THM): {thm}")
    print(f"Seek Time (SK): {sk}")
