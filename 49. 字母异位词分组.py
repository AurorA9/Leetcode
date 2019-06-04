给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]




import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        # 自己做 暴力 超时
        def sameGroup(s1,s2):
            if len(s1) != len(s2):
                return False
            for i in s1:
                if i in s2:
                    index_ = s2.index(i)
                    s2 = s2[:index_] + s2[index_+1:] 
            return s2 == ''
        res = []
        now_having = []
        for i in range(len(strs)):
            temp = []
            if strs[i] in now_having:
                continue
            now_having.append(strs[i])
            for j in range(i,len(strs)):
                if sameGroup(strs[i],strs[j]):
                    temp.append(strs[j])
                    now_having.append(strs[j])
            res.append(temp)
        return res'''
        
        from collections import defaultdict
        lookup = defaultdict(list)
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())

            