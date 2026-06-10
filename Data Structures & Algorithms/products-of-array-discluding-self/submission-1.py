class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_product = []

        for i in range(len(nums)):
            products = 1
            for j in range(len(nums)):
                if(j != i):
                    products *= nums[j]

            array_product.append(products)

        return array_product