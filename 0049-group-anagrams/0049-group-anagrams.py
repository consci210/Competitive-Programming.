class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        answer = []
        for word in strs:
            if ("".join(sorted(word))) in anagrams :
                anagrams["".join(sorted(word))].append(word)
            else :
                anagrams["".join(sorted(word))] = [word]
        for key in anagrams :
            answer.append(anagrams[key])
        return answer
            