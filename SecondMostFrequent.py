from collections import Counter


def second_most_frequent(numbers: []):
    freq = Counter(numbers)

    sorted_freq = sorted(set(freq.values()), reverse=True)

    if len(sorted_freq) < 2:
        return None

    second_highest = sorted_freq[1]

    for num, count in freq.items():
        if count == second_highest:
            return num
