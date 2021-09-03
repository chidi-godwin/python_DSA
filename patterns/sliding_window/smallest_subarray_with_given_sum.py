def smallest_subarray_with_given_sum(s, arr):
  min_length = float("inf")
  length = 0
  windowStart, windowSum = 0, 0

  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]
    length += 1

    while windowSum >= s:
      min_length = min(min_length, length)
      windowSum -= arr[windowStart]
      length -= 1
      windowStart += 1
      
  return min_length
