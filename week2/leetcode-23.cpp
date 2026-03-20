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
    ListNode* mergeTwo(ListNode* l1, ListNode* l2) {
        ListNode* p1 = l1;
        ListNode* p2 = l2;
        ListNode dummy(-1);
        ListNode* tail = &dummy;
        while(p1 != nullptr && p2 != nullptr) {
            if(p1->val > p2->val) {
                tail->next = p2;
                p2 = p2->next;
            }
            else {
                tail->next = p1;
                p1 = p1->next;
            }
            tail = tail->next;
        }
        // 因為是pointer，所以直接把沒算完的屁股貼上去就好了。
        if(p1 != nullptr) tail->next = p1;
        if(p2 != nullptr) tail->next = p2;
        // 把dummy head去掉。
        return dummy.next;
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<ListNode*> cur = lists;
        // Special Case;
        if (lists.size() == 0) return nullptr;
        // 只要cur還有東西，也就代表沒有全部merge完。
        while(cur.size() > 1) {
            vector<ListNode*> next;
            // it一方面可以看當前是不是至少大於兩個。
            // 另一方面可以幫我們一路往後跑抓兩個ListNode*來merge。
            int it = 0;
            // 之所以兩兩merge是因為如果一路越漲越大那種merge法，複雜度會太高。
            while(it+1 < cur.size()) {
                ListNode* merged = mergeTwo(cur[it], cur[it+1]);
                next.push_back(merged);
                it += 2;
            }
            // 如果還有多一個，塞進去next。
            if(it < cur.size()) next.push_back(cur[it]);
            // 都跑完了，所以把cur更新為next
            cur = next;
        }
        // 反正最後一定會merge完，因為while loop是跑到一為止。
        return cur[0];
    }
};