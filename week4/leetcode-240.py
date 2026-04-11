class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        # 站在右上角，如果target比當前大，捨棄整列。
        # 如果target比當前小，捨棄整行。
        cr, cc = 0, len(mat[0])-1
        while cr < len(mat) and cc >= 0:
            if mat[cr][cc] > target:
                cc -= 1
            elif mat[cr][cc] < target:
                cr += 1
            else:
                return True
        return False
        # 只能解NxN，看錯題目了...
        """
        def binarySearch(TYPE: str, mat: List[List[int]], row: int, col: int, target) -> bool:
            if TYPE == "row":
                left, right = 0, row
                while left < right:
                    mid = (left+right)//2
                    if mid < 0 or mid >= row:
                        return False
                    elif target < mat[mid][col]:
                        right = mid
                    elif target > mat[mid][col]:
                        left = mid+1
                    else:
                        return True
            if TYPE == "col":
                left, right = 0, col
                while left < right:
                    mid = (left+right)//2
                    if mid < 0 or mid >= col:
                        return False
                    elif target < mat[row][mid]:
                        right = mid
                    elif target > mat[row][mid]:
                        left = mid+1
                    else:
                        return True
            return False
        # current row, current col
        cr, cc = 0, 0
        while(True):
            if target > mat[cr][cc]:
                cr, cc = cr+1, cc+1
            if target == mat[cr][cc]:
                return True
            if target < mat[cr][cc]:
                br = binarySearch("row", mat, cr, cc, target) # bool of row
                bc = binarySearch("col", mat, cr, cc, target) # bool of col
                return br or bc
        return False
        """