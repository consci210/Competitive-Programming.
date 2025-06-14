class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        firstNonZero = None
        firstNonNine = None

        # Find first digit not 0 and not 9
        for ch in s:
            if ch != '0' and firstNonZero is None:
                firstNonZero = ch
            if ch != '9' and firstNonNine is None:
                firstNonNine = ch
            if firstNonZero and firstNonNine:
                break

        # Create the small number (replace all firstNonZero with '0')
        small = ""
        for ch in s:
            if ch == firstNonZero:
                small += '0'
            else:
                small += ch

        # Create the large number (replace all firstNonNine with '9')
        large = ""
        for ch in s:
            if ch == firstNonNine:
                large += '9'
            else:
                large += ch

        return int(large) - int(small)
