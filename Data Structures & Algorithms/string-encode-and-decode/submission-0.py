class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""

        result = []

        for s in strs:
            result.append(f"{len(s)}:{s}")

        return ''.join(result)

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        result_list = []
        i = 0
        start_index = 0

        while i < len(s):
            if s[i] != ':':
                i += 1
            else:
                length = int(s[start_index:i])
                result_list.append(s[i + 1:i + length + 1])
                i += length + 1
                start_index = i

        return result_list

        
