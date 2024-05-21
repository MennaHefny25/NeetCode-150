from typing import List

# Unstable test case 
class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""        
        return "$".join(strs)
    

    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]
        return s.split("$")



class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoding the list of strings into a single string
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "$" + s
        return encoded_string
    

    def decode(self, s: str) -> List[str]:
        # Decoding the single string back into the list of strings
        decoded_strings = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter
            j = s.find("$", i)
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string using the length found
            decoded_strings.append(s[j+1:j+1+length])
            # Move to the next part of the encoded string
            i = j + 1 + length
        return decoded_strings


"""
Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
"""
"""
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
"""

sol = Solution()
strs = [""]

enc = sol.encode(strs)
print("Input: ", strs)

dec = sol.decode(enc)
print("Output: ", dec)
