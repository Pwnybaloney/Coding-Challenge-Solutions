# There are n people that are split into some unknown number of groups. 
# Each person is labeled with a unique ID from 0 to n - 1.

# Input
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. 
# For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

# Output
# Return a list of groups such that each person i is in a group of size groupSizes[i].

# Each person should appear in exactly one group, and every person must be in a group. 
# If there are multiple answers, return any of them. 
# It is guaranteed that there will be at least one valid solution for the given input.

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSizingIndices = {}
        finalReturnGroup = []
        #iterate through groupSizes
        for i in range(len(groupSizes)):
            #Where i is the unique ID of person i
            #check if the key size exists in the dictionary
            if groupSizes[i] not in groupSizingIndices:
                #if it does not exist, create an empty array
                groupSizingIndices[groupSizes[i]] = []

            #append the group member's ID to their respective group size
            groupSizingIndices[groupSizes[i]].append(i)
            
            #once the group capacity is filled, append it to the final group and
            #reset the dictionary entry
            if len(groupSizingIndices[groupSizes[i]]) == groupSizes[i]:
                finalReturnGroup.append(groupSizingIndices[groupSizes[i]])
                del groupSizingIndices[groupSizes[i]]
                
        return finalReturnGroup
                

