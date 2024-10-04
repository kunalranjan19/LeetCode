class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        skill.sort()
        target = skill[0] + skill[-1]

        left = 0
        right = n - 1
        out = 0

        while left < right:
            summ= skill[left] + skill[right]
            if summ!= target:
                return -1
            out+= skill[left] * skill[right]

            left += 1
            right -= 1
        return out
