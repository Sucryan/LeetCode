# https://leetcode.com/problems/course-schedule-iii/solutions/2185553/python3-heapq-faster-solution-with-expla-byvq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        A, curr = [], 0
        for dur, ld in courses:
            heapq.heappush(A,-dur)
            curr += dur
            if curr > ld: curr += heapq.heappop(A)
        return len(A)