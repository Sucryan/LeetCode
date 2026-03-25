/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // 一個left, 一個right pointer, right會先走k次，放入vector中。
    // 確定可以的話，先把vector reverse，left再走k次把reverse後的結果塞進去。
    // 細節: 把vector init宣告在ptr != nullptr 也就是對於left pointer的大loop下，這樣每次走k次後都會重新init
        // 並且right pointer在走k次的時候如果發現走到null會直接return 當前的head，因為她說後面不滿足k的不用reverse；
        // 這樣也可以避免left走到null的可能性
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* ptr = head;
        while(ptr != nullptr) {
            int count = 0;
            vector<int> v;
            ListNode* tmp = ptr;
            for(int i = 0; i < k; i++) {
                if(tmp == nullptr) return head;
                v.push_back(tmp->val);
                tmp = tmp->next;
            }
            reverse(v.begin(), v.end());
            for(int i = 0; i < k; i++) {
                ptr->val = v[i];
                ptr = ptr->next;
            }
        }
        return head;
    }
};
