#!/usr/bin/env python3
# Author: Arash Zarif

def find_pairs_with_sum(arr, target):
    result_indices = []
    seen_numbers = set()

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen_numbers:
            result_indices.append(arr.index(complement) + i)
        seen_numbers.add(num)

    return result_indices


def main():
    lst = [int(x) for x in input().strip().split()]
    target = int(input())

    result_indices = find_pairs_with_sum(lst, target)

    if not result_indices:
        print("Not Found!")
    else:
        result_indices = sorted(result_indices)
        for i in result_indices:
            print(i)


if __name__ == "__main__":
    main()
