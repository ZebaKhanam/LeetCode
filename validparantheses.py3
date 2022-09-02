class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map1 = {
            '(' : 1 , 
            ')' : 2 ,  
            '{' : 3, 
            '}' : 4, 
            '[' : 5 ,
            ']':6 
        }
        for i in s:
            if(not stack) and (map1[i] % 2 == 0):
                return False
            if(map1[i]%2 == 1):
                stack.append(i)
            else:
                if(map1[stack[-1]] == map1[i] - 1):
                    stack.pop()
                else:
                    return False
        if(not stack):
            return True
                
            
                
        
