class Solution:
    def romanToInt(self, s: str) -> int:
        mapped = {'M': 1000, 'D': 500, 'C': 100,
                  'L': 50, 'X': 10, 'V': 5, 'I': 1}

        total = 0
        i = 0

        while i < len(s):
            val = mapped[s[i]]

            if i+1 < len(s) and val < mapped[s[i+1]]:
                total += mapped[s[i+1]] - val
                i += 2
            else:
                total += val
                i += 1

        return total
