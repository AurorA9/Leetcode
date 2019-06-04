给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j, i+j+1]
        例: 123 * 45,  123的第1位 2 和45的第0位 4 乘积 08 存放在结果的第[1, 2]位中
          index:    0 1 2 3 4  
              
                        1 2 3
                    *     4 5
                    ---------
                          1 5
                        1 0
                      0 5
                    ---------
                      0 6 1 5
                        1 2
                      0 8
                    0 4
                    ---------
                    0 5 5 3 5
        这样我们就可以单独都对每一位进行相乘计算把结果存入相应的index中  
        '''
        len1 = len(num1) - 1
        len2 = len(num2) - 1
        
        if len1 < 0 or len2 < 0:
            return ""
        if len1 == 0 or len2 == 0:
            return str(int(num1) * int(num2))
        mul = [0 for _ in range(len1 + len2 + 2)]
        
        for i in range(len1,-1,-1):
            for j in range(len2,-1,-1):
                bitmul = int(num1[i]) * int(num2[j])
                bitmul += mul[i+j+1] #先加低位 判断是否有新的进位
                mul[i+j] += bitmul // 10   #注意有个加号
                mul[i+j+1] = bitmul % 10
        res = []
    
        flag = False
        for i in range(len(mul)):
            if mul[i] == 0 and not flag:
                continue
            else:
                flag = True
                res.append(str(mul[i]))
        
        return ''.join(res)
        
        
        
        
        
        