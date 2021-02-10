class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = ""
        s_len = len(s)

        cycle = 2*numRows-2

        for r_num in range(numRows):
            # Case of two characters
            if r_num == 0 or r_num == numRows-1:
                answer += s[r_num::(numRows-1)*2]
            
            # Otherwise they're cases of 3 characters
            else:
                for i in range(r_num, s_len, cycle):
                    answer += s[i]

                    next_i = i + (cycle - r_num * 2)
                    if next_i < s_len:
                        answer += s[next_i]

        return answer