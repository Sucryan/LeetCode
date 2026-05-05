# https://leetcode.com/problems/optimal-partition-of-string/solutions/3376720/image-explanation-set-is-all-you-need-in-a6w3
class Solution:
    """
    Time Complexity: O(n) where n is the length of string s
    - We iterate through the string once, performing constant time operations (set operations) at each step
    
    Space Complexity: O(k) where k is the size of the character set
    - In the worst case, our set could contain all unique characters from the input alphabet
    - For ASCII, this is bounded by O(128), which is effectively O(1)
    - For Unicode, this could be larger but still bounded by the alphabet size
    """
    def partitionString(self, s: str) -> int:
        subs = 1                      # Start with 1 substring
        char_set = set()              # Track characters in current substring
        
        for ch in s:
            if ch not in char_set:    # If character not seen in current substring
                char_set.add(ch)      # Add to current substring
                continue
            
            # If character already in set, we need to start a new substring
            subs += 1                 # Increment substring count
            char_set.clear()          # Clear the set for new substring
            char_set.add(ch)          # Add current character to new substring
        
        return subs  # Return the total number of substrings