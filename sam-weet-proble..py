def max_sweets(n, A, B, m, C):
    sweets = list(zip(A, B))  # Combine the time and sweetness levels for each sweet
    sweets.sort(key=lambda x: x[1], reverse=True)  # Sort sweets in descending order of sweetness

    total_sweets = 0
    total_sweetness = 0

    for i in range(n):
        sweet_time, sweet_sweetness = sweets[i]

        # Find the day with maximum available time that can be used to make the current sweet
        max_time_day = -1
        max_time_available = 0
        for j in range(m):
            if C[j] >= sweet_time and C[j] > max_time_available:
                max_time_available = C[j]
                max_time_day = j

        # If a suitable day is found, make the sweet and update the totals
        if max_time_day != -1:
            total_sweets += 1
            total_sweetness += sweet_sweetness
            C[max_time_day] = 0  # Mark the day as used

    return total_sweets, total_sweetness


# Example usage
n = 3
A = [10, 2, 5]
B = [40, 90, 20]
m = 3
C = [3, 4, 5]

max_sweets_count, max_total_sweetness = max_sweets(n, A, B, m, C)
print(list(max_sweets(n, A, B, m, C)))
