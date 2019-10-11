def lengthOfLongestSubstring(s):
        if s == "":
            return 0
        MaxLength = 0
        TempString = ""
        for i in s:
            if i not in TempString:
                TempString += i
                if len(TempString) > MaxLength:
                    MaxLength = len(TempString)
            else:
                TempString = TempString[TempString.index(i)+1:] + i
        return MaxLength
