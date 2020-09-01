# Assignment1


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tempS = sorted(s)
        tempT = sorted(t)
        if tempS == tempT:
            return True
        else:
            return False

# Assignment2


class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
        ans += d[s[-1]]
        return ans

# Assignment3


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] < 9:
                digits[-1] += 1
                return digits

        else:
            s = ""
            for i in digits:
                s += str(i)

            s = str(int(s) + 1)
            digits = [int(x) for x in s]

            return digits

