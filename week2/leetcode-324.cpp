class Solution {
public:
    // 會有相同值問題，左半要從左側拿，右半要從右側拿。
    void wiggleSort(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> res;
        int mid = (nums.size()+1) / 2;
        int left = mid-1, right = nums.size()-1;
        while(left >= 0 || right < nums.size()) {
            if(left >= 0) res.push_back(nums[left]);
            if(right < nums.size()) res.push_back(nums[right]);
            left--;
            right--;
        }
        for(int i = 0; i < nums.size(); i++) {
            nums[i] = res[i];
        }
    }
};