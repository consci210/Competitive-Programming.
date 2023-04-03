class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = []   
        high_score = sorted(score)
        hashmap = defaultdict(int)
        for i in range(len(score)-1 , -1 , -1) :
            hashmap [high_score[i]] =  len(score) - i 

        for rank in score :
            if hashmap[rank] == 1 :
                answer.append("Gold Medal")
            elif hashmap[rank] == 2 :
                answer.append("Silver Medal")
            elif hashmap[rank] == 3 :
                answer.append("Bronze Medal")
            else :
                position = str(hashmap[rank])
                answer.append(position)
        return answer
                    
            