class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 2:
            return [[1]]
        pascal_triangle = [[1],[1, 1]]

        for row in range(2, numRows):
         
            array = []
            array.append(1)
            for middle in range (1, row ):
              
                left = pascal_triangle[row-1][middle-1]
              
                right = pascal_triangle[row-1][middle]
               
                array.append(left+right)
            array.append(1)
            pascal_triangle.append(array)
        return pascal_triangle

