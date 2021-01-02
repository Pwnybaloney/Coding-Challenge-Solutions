class Solution:
    def reverseParentheses(self, s: str) -> str:
        #initialize a stack to keep track of left bracket indexes
        leftBracketIndices = []
        
        #iterate through the string
        outputString = s
        index = 0
        
        while index < len(outputString):
            if outputString[index] == "(":
                leftBracketIndices.append(index)
                
            elif outputString[index] == ")":
                #print("right bracket found at index " + str(index))
                lastLeftBracketIndex = leftBracketIndices[len(leftBracketIndices)-1]
                
                toBeReplaced = outputString[lastLeftBracketIndex:index+1]
                reversedString = toBeReplaced[::-1]
                
                outputString = outputString.replace(toBeReplaced,reversedString[1:len(reversedString)-1])
                leftBracketIndices.pop()
                index = index-2
                
            index = index + 1
            
        return outputString
            
            
            
            
            
        
        
        
            