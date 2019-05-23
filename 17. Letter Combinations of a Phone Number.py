class Solution:
    dic = {'2' : 'abc', '3':'def','4':'ghi','5':'jkl','6':'mno',
              '7':'pqrs','8':'tuv','9':'wxyz', '0':' ', '1':'*'}
    def letterCombinations(self, digits: str) -> List[str]:
        li = []
        lia = []
        if digits:
            self.f(digits, 0,li,lia)
        return li
        
    def f(self,digits,i,li,lia):
        if i == len(digits):
            li.append("".join(lia))
            return 
        for j in range(len(self.dic.get(digits[i],""))):
            
            lia.append(self.dic[digits[i]][j])
            self.f(digits,i+1,li,lia)
            lia.pop()