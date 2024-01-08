class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int

        Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        Output: 2
        """
        def isDifferByOne(str1, str2):
            return sum([1 for i in range(len(str1)) if str1[i]!=str2[i]]) == 1

        Q = [(startGene, 0)]
        seen = []
        while Q:
            curGene, step = Q.pop(0)
            if curGene == endGene:
                return step
            for gene in bank:
                if isDifferByOne(curGene, gene) and gene not in seen:
                    seen.append(gene)
                    Q.append([gene, step + 1])
        return -1
                    
