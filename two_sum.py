def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}
    lenght = len(nums)

    for i in range(lenght):
        complement = target - nums[i]
        if complement in num_map and complement != nums[i]:
            return [num_map[complement], i]
        num_map[nums[i]] = i
    return []
