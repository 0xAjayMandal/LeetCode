from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create a counter for the target string
        target_counter = Counter(t)
        
        # Initialize variables for the sliding window
        left = 0
        min_window = float('inf')
        min_window_start = 0
        counter = len(t)
        
        # Iterate over the string using the sliding window
        for right in range(len(s)):
            # If the current character is in the target string, decrement the counter
            if s[right] in target_counter:
                target_counter[s[right]] -= 1
                if target_counter[s[right]] >= 0:
                    counter -= 1
            
            # If all characters in the target string are found, try to minimize the window
            while counter == 0:
                # Update the minimum window if necessary
                if right - left + 1 < min_window:
                    min_window = right - left + 1
                    min_window_start = left
                
                # Move the left pointer to the right to shrink the window
                if s[left] in target_counter:
                    target_counter[s[left]] += 1
                    if target_counter[s[left]] > 0:
                        counter += 1
                left += 1
        
        # Return the minimum window substring
        if min_window == float('inf'):
            return ""
        return s[min_window_start:min_window_start+min_window]