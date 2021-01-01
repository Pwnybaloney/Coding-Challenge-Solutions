class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        
        def arithmetic(array):
            sortednums = sorted(array)
            diff = sortednums[1] - sortednums[0]
            for i in range(1,len(sortednums)-1):
                if sortednums[i+1] - sortednums[i] != diff:
                    return False
            return True
        
        for i in range(len(l)):
            output.append(arithmetic(nums[l[i]:r[i]+1]))
        return output