# https://leetcode.com/problems/course-schedule-iii/solutions/2185553/python3-heapq-faster-solution-with-expla-byvq
# https://chatgpt.com/share/69f9bc07-ddd8-83a5-8a7c-c9783dfa3dfb
# 先照 lastDay 由小到大排序，代表我們一路優先處理「越早截止、越沒彈性」的課。
# 對每門課先貪心地假裝修下去，並把 duration 放進 max heap，curr 記錄目前總耗時。
# 如果 curr 超過目前這門課的 lastDay，表示目前選的課集合在這個 deadline 前塞不下；
# 既然一定要丟一門，最佳選擇就是丟掉 duration 最長的課，因為這樣能釋放最多時間，
# 讓剩下的課集合總耗時最短，也保留最多空間給後面的課。
# 最後 heap 裡剩下幾門課，就是最多可以修幾門。
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        A, curr = [], 0
        for dur, ld in courses:
            heapq.heappush(A,-dur)
            curr += dur
            if curr > ld: curr += heapq.heappop(A)
        return len(A)