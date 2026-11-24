class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sortWord = "".join(sorted(word))
            anagrams[sortWord].append(word)
        
        return list(anagrams.values())
            

