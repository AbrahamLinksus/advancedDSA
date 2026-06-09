mainString = "abababc"
subString = "ababc"

def stringMatch(mainString, subString):
    n = len(subString)
    length = len(mainString)
    i = 0
    while n <= length:
        if mainString[i:n] == subString:
            print("Found in index", i)
            return True
        i += 1
        n += 1
    return False


def rabinKarp(mainString, subString):
      base = 10
      char_map = {chr(ord('a') + i): i + 1 for i in range(26)}
      m, n = len(subString), len(mainString)

      if m > n:
        return False

      def hashString(s):
          h = 1
          for ch in s:
            h = h * base + char_map[ch]
          return h

      high_power = base ** (m - 1)
      sub_hash = hashString(subString)
      window_hash = hashString(mainString[:m])

      for i in range(n - m + 1):
        if window_hash == sub_hash and mainString[i:i+m] == subString:
            print(i)
            return True
        if i < n - m:
            window_hash = (window_hash - char_map[mainString[i]] * high_power) * base + char_map[mainString[i + m]]

      return False

#KMP intution
# LPS -> Longest Prefix of a string that is also a suffix, excluding the current character if 1 is only present and so on

def KMP(mainString, subString):
    def lps(string):
        if string == "": return 0
        lps = [0] * len(string)
        prevLPS, i = 0, 1
        while i < len(string):
            if string[i] == string[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]
        return lps
    lpsArr = lps(subString)
    

    return lps(subString)

print(KMP(mainString, subString))




print(rabinKarp(mainString, subString))
print(stringMatch(mainString, subString))