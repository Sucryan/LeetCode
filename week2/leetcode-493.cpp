class Solution {
public:
    int mergeSort(vector<int>& nums, int l, int r) {
        // 如果是單元素，就return 0，因為不可能會有reverse pair
        if(l >= r) return 0;
        // 先看左邊右邊之前算好的結果。
        int mid = (l+r) / 2;
        int leftCount = mergeSort(nums, l, mid);
        int rightCount = mergeSort(nums, mid+1, r);
        // merge環節。
        // ===== 特別for這題的modification =====
        // 先算crossCount
        int crossCount = 0;
        int j = mid+1;
        // 思考: 
        /*
        左邊和右邊都分別是遞增，
        而j會monotonic遞增(也就是持續j++)的意義在於，
        隨著最大圈的loop遞增原本右邊會left[i] > 2*right[j]的在i++以後也必定會符合。
        */
        for(int i = l; i <= mid; i++) {
            while(j <= r && (long long)nums[i] > 2LL*nums[j]) {
                j++;
            }
            // 這個主要是我們沒有拆成兩個vector，直接用index下去算。
            crossCount += j -(mid+1);
        }
        // ===== 特別for這題的modification =====
        // for merge (就正常的merge sort)
        vector<int> tmp;
        int p1 = l, p2 = mid+1;
        while(p1 <= mid && p2 <= r) {
            if(nums[p1] <= nums[p2]) {
                tmp.push_back(nums[p1]);
                p1++;
            }
            else {
                tmp.push_back(nums[p2]);
                p2++;
            }
        }
        while(p1 <= mid) {
            tmp.push_back(nums[p1]);
            p1++;
        }
        while(p2 <= r) {
            tmp.push_back(nums[p2]);
            p2++;
        }
        // 寫回原本的nums
        for(int k = 0; k < tmp.size(); k++) {
            nums[l+k] = tmp[k];
        }

        return leftCount + rightCount + crossCount;
    }
    int reversePairs(vector<int>& nums) {
        return mergeSort(nums, 0, nums.size()-1);
    }
};