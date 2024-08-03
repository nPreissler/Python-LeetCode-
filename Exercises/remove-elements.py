class Solution(object):
    def removeElement(self, nums, val):
      
        for a in nums[::-1]:     
            if a == val:
                nums.remove(val)     
                
#Difficulty : Easy