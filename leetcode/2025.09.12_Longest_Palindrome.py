#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int: 
        # 이게 가장 빠른 베스트 way
        length = 0
        char = set()

        for i in s:
            if i in char:
                char.remove(i)
                length += 2
            else: 
                char.add(i)
        if len(char) > 0:
            length += 1

        return length 

    # 내가 작성한 반복문 + if문
    # char = Counter(s)
    # length = 0
    # odd = False
    # for i in char:
    #   length = (i//2) * 2
    #   if i % 2 == 0:
    #       odd = True
    # if odd:
    #   length += 1
    # return length
        


# 그니까 문자가 주어지는데 소문자와 대문자가 포함 근데 그 둘은 다른거임
# 앞으로 읽어도 뒤로 읽어도 같게 나오고 그 길이가 가장 긴거
# 즉 주어진 문장에서 문장에 양끝이 같게 하면서 길이를 갱신 그중에 제일 긴거를 비교를 통해 찾으면됨


# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.