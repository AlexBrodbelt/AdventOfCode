def longestPalindrome(s):
    longest_substr = ""
    for l in range(len(s),-1,-1):
        for i in range(len(s)-l):
            #print(s[i:i+l+1], s[i:i+l+1][::-1])
            if s[i:i+l+1] == s[i:i+l+1][::-1]:
                return s[i:i+l+1]

print(longestPalindrome("abacdskafjfjf"))


def reverse(s):
    string = str(s)
    if string[0] == "-":
              

    return str(s)

print(reverse(-231))
