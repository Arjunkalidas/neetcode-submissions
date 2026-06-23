class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for s in strs:
            res.append(f'{len(s)}:{s}')

        return ''.join(res)


    def decode(self, s: str) -> List[str]:

        res = []

        i, j = 0, 0

        while j < len(s):
            
            if s[j] == ':':
                word_len = int(s[i:j])
                word = s[j+1:j+1+word_len]
                res.append(word)
                j += word_len + 1
                i = j
            else:
                j+=1

        return res


