class Solution:
    def isPalindrome(self, s: str) -> bool:
       regex_alphaNumeric = re.sub(r'[^a-zA-Z0-9]','',s).lower()

       return regex_alphaNumeric == regex_alphaNumeric[::-1]