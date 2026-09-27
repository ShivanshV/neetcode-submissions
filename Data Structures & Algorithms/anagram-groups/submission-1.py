class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dictionary = defaultdict(list)
        for word in strs:
            temp = defaultdict(int)
            for letter in word:
                temp[letter]+=1
                
            key = frozenset(temp.items())
            dictionary[key].append(word)
          
        
        return list(dictionary.values())

