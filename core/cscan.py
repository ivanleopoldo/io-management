def cscan(track_size, initial, queue, seek_rate, alpha):
    queue.sort()

    right = [track for track in queue if track >= initial]
    left = [track for track in queue if track < initial]

    max_right = track_size - 1
    min_left = 0
    max_left = max(left)

    thm = ((track_size - 1) - initial) + (max_left - 0) + alpha

    sk = thm * seek_rate

    print("\nDisk Movement Visualization (C-SCAN):")
    print(f"Start at {initial}")
    print(f"Move to {max(right)} (Distance: {max(right)- initial})")
    print(f"Move from {max(right)} to {max_right} (Distance: {max_right - max(right)})")
    print(f"Jump back to 0 (Distance: 20)")
    print(f"Move from 0 to {min_left} (Distance: {min_left})")
    for track in left:
        if track != min_left:
            print(f"Move to {track}")

    print("\nSummary:")
    print(f"Total Head Movement (THM): {thm}")
    print(f"Seek Time (SK): {sk}")
