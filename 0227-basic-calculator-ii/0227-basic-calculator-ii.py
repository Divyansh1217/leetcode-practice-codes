class Solution:
    def calculate(self, s: str) -> int:
        curr_res = 0
        res = 0
        num = 0
        op = "+" 
        for ch in s + "+":
            if ch.isdigit():
                num = 10 * num + int(ch)

      
            if ch in ("+", "-", "*", "/"):
                if op == "+":
                    curr_res += num
                elif op == "-":
                    curr_res -= num
                elif op == "*":
                    curr_res *= num
                elif op == "/":
                    
                    curr_res = int(curr_res / num)
                
            
                if ch in ("+", "-"):
                    res += curr_res
                    curr_res = 0
                
                op = ch
                num = 0
        
        return res