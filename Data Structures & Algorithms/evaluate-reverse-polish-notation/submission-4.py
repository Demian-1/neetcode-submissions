class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = [] 
        ops = {"+", "-", "*", "/"}
        for t in tokens: 
            if t in ops: 
                a = myStack.pop()
                b = myStack.pop()
                if t == "+":
                    myStack.append(b + a)
                elif t == "-": 
                    myStack.append(b - a)
                elif t == "*": 
                    myStack.append(b * a)
                else:
                    myStack.append(int(b / a))
            else:
                myStack.append(int(t))
        return myStack[-1]
        """
        "10","6","9","3","+","-11","*","/","*","17","+","5","+"
        -198
        """