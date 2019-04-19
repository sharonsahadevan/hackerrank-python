# Author : Sharon Sahadevan
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_numbers = sorted(arr, reverse=True)
    unique_numbers = sorted(set(sorted_numbers), reverse=True)
    print(unique_numbers[1])
