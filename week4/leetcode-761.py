class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # 關鍵點：反正題目想暗示我們的意思就是一定是1開頭0結尾 --> 可以想成樹狀結構。
        count = 0
        left = 0
        chunks = []
        
        # 遍歷整個字串，尋找「獨立的」 Special String 區塊
        for i, char in enumerate(s):
            count += 1 if char == '1' else -1
            
            # 當 count 歸零，代表我們精準切出了一個完整的 Special String (範圍是 left 到 i)
            if count == 0:
                # 【核心邏輯：掐頭去尾與遞迴】
                # s[left+1 : i] 就是去掉最外層的 '1' 和 '0' 後的「內部字串」
                # 把內部字串丟進遞迴，確保它內部也被排到最大
                inner_sorted = self.makeLargestSpecial(s[left+1:i])
                
                # 把排好的內部字串，重新套上最外圍的 '1' 和 '0'，存入 chunks
                # 細節：這題說1的數量在任何prefix一定不小於0，然後結束一定是special，所以一定頭是1，尾巴是0。
                chunks.append("1" + inner_sorted + "0")
                
                # 更新左指標，準備切下一個區塊
                left = i + 1
                
        # 迴圈結束後，我們擁有了一堆「內部已經最佳化」的合法區塊
        # 題目說可以無限次交換相鄰區塊，這就等同於我們可以對它們進行降序排序！
        chunks.sort(reverse=True)
        
        # 組合起來，就是當前層級的最大字典序字串
        return "".join(chunks)