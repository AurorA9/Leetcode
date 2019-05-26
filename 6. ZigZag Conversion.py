将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) == 0:
            return ''
        if numRows == 1:
            return s
        row = 0
        col = 0
        maxRows = numRows - 1
        index_now = 0
        cols = len(s)//(numRows + numRows -2) + 1
        cols = cols * (numRows + numRows -2)//2
        matrix = [[' ' for j in range(cols) ] for i in range(numRows) ]
        cuizhi = True
        while index_now < len(s):
            # 如果是第一行 则向下遍历
            if row == 0 :
                matrix[row][col] = s[index_now]
                row +=1
                cuizhi =True
            # 最后一行 则右上角遍历
            elif row == maxRows:
                matrix[row][col] = s[index_now]
                row -=1
                col +=1
                cuizhi = False
            # 斜着走
            elif cuizhi == False:
                matrix[row][col] = s[index_now]
                row -=1
                col +=1
            # 垂直走
            else:
                matrix[row][col] = s[index_now]
                row += 1
            index_now +=1
        slist = []
        for i in range(numRows):
            for j in range(cols):
                if matrix[i][j] != ' ':
                    slist.append(matrix[i][j])
        return ''.join(slist)
            
        