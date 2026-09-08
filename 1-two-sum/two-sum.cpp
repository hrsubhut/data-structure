class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j, n = nums.size(), q = 0;
        
        for (i = 0; i < n; i++) {
            q = target - nums[i];
            
            for (j = i + 1; j < n; j++) {
                // Check against nums[j], not nums[i]
                if (q == nums[j]) {
                    return {i, j};
                }
            }
        }
        
        return {}; // Fallback return to satisfy the compiler
    }
};