def average(array):
    distinct_heights = set()
    for i in range(0, len(array)):
        distinct_heights.add(array[i])

    sum_of_heights = sum(distinct_heights)
    count_of_heights = len(distinct_heights)
    average = (sum_of_heights/count_of_heights)
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
