class Solution(object):
    def minimumSteps(self, s):
        ones_positions = [i for i, c in enumerate(s) if c == '1']
        k = len(ones_positions)
        min_steps = 0
        for i, pos in enumerate(ones_positions):
            target_pos = len(s) - k + i
            min_steps += abs(pos - target_pos)
        return min_steps
