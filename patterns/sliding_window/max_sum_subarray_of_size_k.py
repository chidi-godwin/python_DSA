def max_sub_array_of_size_k(k, arr):
  _max = float("-inf")

  windowSum, windowStart = 0, 0

  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]

    if windowEnd >= k - 1:
      _max = max(_max, windowSum)
      windowSum -= arr[windowStart]
      windowStart += 1
  return _max
