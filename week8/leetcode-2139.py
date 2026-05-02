class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        tmp = target
        cnt = 0
        while tmp != 0:
            if tmp%2 == 0 and maxDoubles:
                tmp //= 2
                maxDoubles -= 1
                cnt += 1
            elif tmp%2 == 1 or not maxDoubles:
                tmp -= 1
                cnt += 1
                if not maxDoubles:
                    return cnt + tmp - 1
        return cnt-1