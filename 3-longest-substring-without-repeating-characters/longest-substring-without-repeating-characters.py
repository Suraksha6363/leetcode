class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maior = 1
        atual = ""
        for i in s:
            if i in atual:
                if len(atual) > maior:
                    maior = len(atual)
                atual = atual[atual.find(i)+1:] + i
            else:
                atual = atual + i
        if len(atual) > maior:
            maior = len(atual)
        return maior