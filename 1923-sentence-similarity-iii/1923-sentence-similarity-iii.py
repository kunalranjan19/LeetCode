class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        word1 = sentence1.split()
        word2 = sentence2.split()
        n1 = len(word1)
        n2 = len(word2)

        if n1 > n2:
            word1, word2 = word2, word1  

        i = 0
        while i < len(word1) and word1[i] == word2[i]:
            i += 1
        
        j = 0
        while j < len(word1) and word1[-1 - j] == word2[-1 - j]:
            j += 1
        if i + j >= len(word1):
            return True
        else:
            return False