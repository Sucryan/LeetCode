class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        l = [1]
        while len(l) < n:
            # no pythontic
            """
            odd = []
            even = []
            tmp = []
            for num in l:
                odd.append(2*num-1)
                even.append(2*num)
            for num in odd:
                if num <= 2*len(l) and num <= n:
                    tmp.append(num)
            for num in even:
                if num <= 2*len(l) and num <= n:
                    tmp.append(num)
            l = tmp[:]
            """
            # pythontic way
            odd = [2*num-1 for num in l if 2*num-1 <= n]
            even = [2*num for num in l if 2*num <= n]
            l = odd+even
        return l
            
            