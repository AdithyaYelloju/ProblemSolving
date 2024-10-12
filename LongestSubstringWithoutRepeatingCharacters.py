'''longest substring without repeating characters.

Problem Statement: Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcbcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3

abcbda
4
'''


def solve(s):
    start = 0
    unique_elements = []
    max_count = 0


    for i in range(len(s)):
       
        if(s[i] in unique_elements):
            while(s[start] != s[i]):
                unique_elements.pop(0)
                start += 1


            unique_elements.pop(0)
            start += 1
       
        unique_elements.append(s[i])


        max_count = max(max_count, i-start+1)


        print(unique_elements, i-start+1)
       
    return max_count


s = "abcbcbb"
print(solve(s))
