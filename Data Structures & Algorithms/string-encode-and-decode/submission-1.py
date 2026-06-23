class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for word in strs:
            res.append(f"{len(word)}:{word}")

        return "".join(res)
            
    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        start_index = 0

        while i < len(s):
            if s[i] != ':':
                i += 1
            else:
                length = int(s[start_index:i])
                res.append(s[i+1:i+length+1])
                i += length + 1
                start_index = i

        return res
