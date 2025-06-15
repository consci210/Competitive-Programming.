class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"
        tag = "#" + words[0].lower()
        for word in words[1:]:
            tag += word[0].upper() + word[1:].lower()
        return tag[:100]
