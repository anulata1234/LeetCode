def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    curSubStr = ""
    curSubStrDict = {}
    maxSubStr = ""
    for ch in s :
        if ch in curSubStrDict :
            if len(maxSubStr) < len(curSubStr):
                maxSubStr = curSubStr
            curSubStrDict = {}
            curSubStrDict[ch] = ch
            curSubStr = ""+ch

        else :
            curSubStrDict[ch] = ch
            curSubStr += ch

    return len(curSubStr) if len(curSubStr) > len(maxSubStr) else len(maxSubStr)

x = lengthOfLongestSubstring("abbbba")
x = lengthOfLongestSubstring("xyzx")
print(x)
