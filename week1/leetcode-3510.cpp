#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    using ll = long long;

    int minimumPairRemoval(vector<int>& nums) {
        int n = (int)nums.size();
        if (n <= 1) return 0;

        // arr[i] = 目前這個位置代表的值
        // merge 時，左邊留下來，右邊被刪掉
        vector<ll> arr(nums.begin(), nums.end());

        // removed[i] = 這個位置是否已經被刪掉
        vector<bool> removed(n, false);

        // min-heap，存 {pair_sum, left_index}
        // 代表目前有一組候選 pair 是 (left_index, next[left_index])
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;

        // sorted = 目前有幾條相鄰邊滿足 non-decreasing
        // 例如 a <= b，這條邊就算一條好邊
        int sorted = 0;

        // 初始化 heap 與 sorted
        for (int i = 1; i < n; i++) {
            pq.push(make_pair(arr[i - 1] + arr[i], i - 1));
            if (arr[i - 1] <= arr[i]) {
                sorted++;
            }
        }

        // 一開始就已經 sorted
        if (sorted == n - 1) return 0;

        // 用 prev / next 模擬 doubly linked list
        vector<int> prev(n), next(n);
        for (int i = 0; i < n; i++) {
            prev[i] = i - 1;
            next[i] = i + 1;
        }

        // rem = 目前還活著的元素數量
        int rem = n;

        while (rem > 1) {
            // 取目前 heap 最小的 pair
            pair<ll, int> topPair = pq.top();
            pq.pop();

            ll sum = topPair.first;
            int left = topPair.second;
            int right = next[left];

            // lazy deletion:
            // 如果這組 pair 已經失效，就跳過
            if (right >= n) continue; // 已經吃到最右邊了。
            if (removed[left] || removed[right]) continue; // 這組是已經deprecate的紀錄。
            if (arr[left] + arr[right] != sum) continue; // 如果不合也有問題

            // 局部四個角色：pre - left - right - nxt
            int pre = prev[left];
            int nxt = next[right];

            // ---- 先移除舊邊對 sorted 的貢獻 ---- (因為要merge起來)
            // 舊邊可能是：
            // 1. pre -> left （前一個node和本身）
            // 2. left -> right (本身和下一個node)
            // 3. right -> nxt（下一個Node和下下一個，因為自己要跟右邊merge成一個node）
            if (arr[left] <= arr[right]) {
                sorted--;
            }
            if (pre != -1 && arr[pre] <= arr[left]) {
                sorted--;
            }
            if (nxt != n && arr[right] <= arr[nxt]) {
                sorted--;
            }

            // ---- merge：左邊吃掉右邊 ----
            arr[left] += arr[right];
            removed[right] = true;
            rem--;

            // ---- 更新 linked list，讓 right 消失 ----
            // 如果這個left是最左邊的。
            if (pre == -1) {
                prev[left] = -1;
            } else {
                // merge 後會新形成 pre -> left 這條邊
                pq.push(make_pair(arr[pre] + arr[left], pre));
                if (arr[pre] <= arr[left]) {
                    sorted++;
                }
            }
            // 同理，如果他的right本來在最右邊。
            if (nxt == n) {
                next[left] = n;
            } else {
                prev[nxt] = left;
                next[left] = nxt;

                // merge 後會新形成 left -> nxt 這條邊
                pq.push(make_pair(arr[left] + arr[nxt], left));
                if (arr[left] <= arr[nxt]) {
                    sorted++;
                }
            }

            // 如果目前所有相鄰邊都正確，表示整串已經 sorted
            if (sorted == rem - 1) {
                return n - rem;
            }
        }

        return n;
    }
};