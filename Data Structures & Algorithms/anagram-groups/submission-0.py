class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dictionary = defaultdict(list)
        for word in strs:
            
            temp = "".join(sorted(word))
            if temp in dictionary:
                dictionary[temp].append(word)
            else:
                dictionary[temp] = [word]
        
        return list(dictionary.values())

