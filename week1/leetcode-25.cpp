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