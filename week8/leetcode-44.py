# https://leetcode.com/problems/wildcard-matching/solutions/7440992/greedy-with-backtracking-beats-100-o1-sp-qxhw
# https://chatgpt.com/share/69f9a9de-2d24-83a6-94e9-022adca410c3
# 遇到 '*' 時，先不要急著讓它吞字元。
# 我們先記住這個 '*' 的位置，並假設它目前只匹配「空字串」。
# 接著讓 pattern 往 '*' 後面走，先嘗試用最少的吞噬量完成比對。
# 如果後面比對失敗，才會回到這個 '*'，讓它多吞一個 s 的字元再重試。
# 也就是說：'*' 一開始吃 0 個，失敗時才逐步擴張成吃 1 個、2 個、3 個...
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si, pi, match, star = 0, 0, 0, -1
        sn, pn = len(s), len(p)
        while si < sn:
            if pi < pn and (p[pi] == '?' or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < pn and p[pi] == '*':
                star = pi
                match = si
                pi += 1
            elif star != -1:
                pi = star + 1
                match += 1
                si = match
            else:
                return False
        while pi < pn and p[pi] == '*':
            pi += 1
        return pi == pn