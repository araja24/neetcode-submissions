class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = {};

        for (const num of nums) {
            if (!(num in seen)) {
                seen[num] = 1;
            } else {
                return true;
                } 
            }
        return false;
        }
}

