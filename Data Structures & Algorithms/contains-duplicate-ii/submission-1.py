class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distances = {}
        for i in range(len(nums)):
            if distances.get(nums[i]) is None:
                distances[nums[i]] = i
                continue
            if i - distances.get(nums[i]) <= k:
                return True
            else:
                distances[nums[i]] = i
        return False
