class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0  # indices of longest palindrome found
        
        def expandAroundCenter(left: int, right: int) -> (int, int):
            # Expand while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the indices of the palindrome substring
            return left + 1, right - 1
        
        for i in range(len(s)):
            # Odd length palindrome (center at i)
            l1, r1 = expandAroundCenter(i, i)
            # Even length palindrome (center between i and i+1)
            l2, r2 = expandAroundCenter(i, i + 1)
            
            # Update longest palindrome if found longer
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end + 1]
