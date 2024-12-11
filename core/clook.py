def clook(track_size, initial, queue, seek_rate, alpha):
    queue.sort()

    left = [track for track in queue if track < initial]
    right = [track for track in queue if track >= initial]

    thm = (max(right) - initial) + (max(left) - min(left)) + alpha

    sk = thm * seek_rate

    path = [initial] + right + left

    print("\nC-LOOK:")
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
