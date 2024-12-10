def cscan(track_size, initial, queue, seek_rate, alpha):
    queue.sort()

    right = [track for track in queue if track >= initial]
    left = [track for track in queue if track < initial]

    max_right = track_size - 1
    min_left = 0
    max_left = max(left)

    thm = ((track_size - 1) - initial) + (max_left - 0) + alpha

    sk = thm * seek_rate

    print("\nC-SCAN:")
    print(f"Start at {initial}")
    for track in right:
        if track != initial:
            print(f"Move to {track} (Distance: {track - initial})")
    print(f"Move to {max_right} (Distance: {max_right - max(right)})")
    print(
        f"Move from {max_right} to {min_left} (Distance: {max_right - min_left}, Alpha: {alpha})"
    )
    for track in left:
        if track != min_left:
            print(f"Move to {track}")

    print("\nSummary:")
    print(f"Total Head Movement (THM): {thm}")
    print(f"Seek Time (SK): {sk}")
