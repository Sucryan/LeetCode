from collections import deque
# https://gemini.google.com/share/f53f5bcb1dcb
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()  # 裡面存放 tuple: (y - x, x)
        maxi = float('-inf')
        
        for x, y in points:
            # 1. 把過期的點踢掉 (x_j - x_i > k)
            while q and x - q[0][1] > k:
                q.popleft()
            
            # 2. 如果隊列有東西，隊首就是最大的 (y_i - x_i)，直接計算並更新答案
            if q:
                # 方程式：(y_i - x_i) + (y_j + x_j)
                maxi = max(maxi, q[0][0] + y + x)
            
            # 3. 維護單調遞減隊列：把未來絕對用不到的點從隊尾踢掉
            # 如果新來的點其 (y - x) 比隊尾大，隊尾的點就沒有利用價值了
            while q and q[-1][0] <= y - x:
                q.pop()
                
            # 4. 把當前的點加進去，成為未來的候選人
            q.append((y - x, x))
            
        return maxi