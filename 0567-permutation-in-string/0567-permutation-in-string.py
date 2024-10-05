class Solution(object):
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])

        for i in range(len2 - len1 + 1):
            if window_count == s1_count:
                return True

            if i + len1 < len2:
                left_char = s2[i]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]

                right_char = s2[i + len1]
                window_count[right_char] += 1

        return False
