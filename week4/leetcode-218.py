import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 測資很煩，他會跑到int_max的大小，故意把array撐爆。
        event = []
        for L, R, H in buildings:
            event.append((L, -H, R)) # 把建築物塞進去。
            event.append((R, 0, 0))  # 細節：因為建築物結束了，所以要額外塞一個右邊，然後這邊開始高度為0，表示結束。 
        # 雖然L有排序，但建築物可能右邊很長，因為我們額外塞了R進去，所以要排序。
        event.sort()
        res = []
        # 先塞入一個代表地平線的（高度為0，R是無限大）
        heap = [(0, float('inf'))] # 左邊是高度，右邊是右邊界
        for x, neg_h, R in event:
            # 只要有高度就塞進去。
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, R))
            # Lazy Deletion: 如果這個右值比當前x小，則代表他是之前的事情。
            # Issue: 可是x只會被左邊觸發 -- 所以要在event加入右邊界結束aka(R, 0, 0)這個事件，象徵結束。
            while heap[0][1] <= x:
                heapq.heappop(heap)
            # 紀錄當前最大高度
            cur_max_h = -heap[0][0]
            # 思考點：如果當前的高度是維持剛剛的建築的高度（因為會有lazy deletion，所以不可能會有depricate的值在裡面），所以如果高度變化了話，代表要麻我們本來的值depricate，或者有更高的頂掉了我們的值。
            if not res or cur_max_h != res[-1][1]:
                res.append([x, cur_max_h])
        return res
        # 範測會過，但會MLE
        """
        # 整個array至少需要的長度
        LEN = buildings[-1][1]
        # 建立地平線
        l = [0 for i in range(LEN)]
        # 畫出skyline
        for b in buildings:
            for i in range(b[0], b[1]):
                l[i] = max(l[i], b[2])
        # 塞最右下角的點進去
        l.append(0)
        res = []
        # 取出點
        for i in range(LEN+1):
            if i == 0:
                if l[0] != 0:
                    res.append([0, l[i]])
            else:
                if l[i] != l[i-1]:
                    res.append([i, l[i]])
        return res
        """