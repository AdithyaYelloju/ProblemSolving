Changer letters based given list of numbers
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

 
Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"



def solve_brut(s1, shifts):
    s = list(s1)
    print(s)

    for i in range(len(shifts)):
        for j in range(i+1):
            s[j] = chr(ord(s[j]) + shifts[i])
        print(s)
    return ''.join(s)

# Time O(n)
def solve(s1, shifts):
    s = list(s1)
    print(s)

    total_shifts = sum(shifts)

    for i in range(len(s)):
        s[i] = chr(ord(s[i]) + total_shifts)
        total_shifts -= shifts[i]
        print(s)
    return ''.join(s)




s = "abc"
shifts = [3,5,9]
print(solve(s, shifts))
