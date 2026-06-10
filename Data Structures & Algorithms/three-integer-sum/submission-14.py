class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        checkDupli = {}
        result = []
        n = len(nums)
        if n < 3: return []
   
    
        #find first postive number
    
        for i in range(n-1, -1,-1):
            if nums[i] < 0:
                return result
            if i < n -1 and nums[i] == nums[i+1]:
                continue
            pTarget = i
            pPlus = i -1
            pMinus = 0
            
            
            while pMinus < pPlus:
                
                sumT = nums[pTarget] + nums[pPlus] + nums[pMinus]
                if sumT < 0:
                    pMinus += 1
                elif sumT > 0:
                    pPlus -= 1
                else:
                    result.append([nums[pTarget], nums[pPlus], nums[pMinus]])
                    ## so instead of breaking and restarting at the same orginated value 

                    pMinus += 1
            

                    while pMinus < pPlus and nums[pMinus] == nums[pMinus-1]:
                        pMinus += 1
                    
                    pPlus -= 1
                    while pMinus < pPlus and nums[pPlus] == nums[pPlus+1]:
                        pPlus -=1 
        
        return result
                

        







        
            