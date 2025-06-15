class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        print(words)
        if not words:
            return "#"
        tag = "#" + words[0].lower()
        for i in range(1,len(words)):
            tag+=words[i][0].upper()
            tag+=words[i][1:].lower()
        return tag[:100]