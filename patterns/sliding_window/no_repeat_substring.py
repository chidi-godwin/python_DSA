def non_repeat_substring(str1):
    max_length = 0
    window_start = 0
    char_index_map = {}
    
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)

        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end-window_start+1)
    return max_length


print(non_repeat_substring('aabdcbb'))
