class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        # Get max number by replacing the first non-9 digit with 9
        for ch in num_str:
            if ch != '9':
                max_str = num_str.replace(ch, '9')
                break
        else:
            max_str = num_str  # All digits are already 9

        # Get min number by replacing:
        # If first digit is not '1', replace it with '1' to avoid leading zero
        if num_str[0] != '1':
            min_str = num_str.replace(num_str[0], '1')
        else:
            # First digit is already '1', so replace next non-0, non-1 digit with '0'
            for ch in num_str[1:]:
                if ch != '0' and ch != '1':
                    min_str = num_str.replace(ch, '0')
                    break
            else:
                min_str = num_str  # No change needed if already minimal

        return int(max_str) - int(min_str)
