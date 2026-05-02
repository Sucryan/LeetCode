class Solution:
    def jump(self, nums: List[int]) -> int:
        L = len(nums)
        if L <= 1: return 0
        
        hops = 0
        maxi = 0  # 觀察員：目前看過最強的潛力
        end = 0   # 目前這一跳的物理極限
        
        # 遍歷陣列（不用到最後一個，因為到達最後一個前接力就完成了）
        for idx in range(L - 1):
            # 隨時更新最強潛力
            maxi = max(maxi, idx + nums[idx])
            
            # 當走到「這一次跳躍」的盡頭時，才不得不跳下一跳
            if idx == end:
                hops += 1      # 發生接力
                end = maxi     # 更新下一跳的邊界
                
                # 如果已經看到終點，就不用再算了
                if end >= L - 1:
                    break
        return hops