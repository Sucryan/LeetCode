/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if (!root) return true;
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        while(!q.empty()) {
            // 先抓好，因為在for裡面會額外插入下面的child。
            int size = q.size();
            int prev_val = (level % 2 == 0) ? INT_MIN : INT_MAX;
            // 這層有多少個人
            for(int i = 0; i < size; i++) {
                auto node = q.front();
                q.pop();
                if(level % 2 == 0) {
                    if(node->val % 2 == 0 || node->val <= prev_val) return false;
                }
                else {
                    if(node->val % 2 == 1 || node->val >= prev_val) return false;
                }
                prev_val = node->val;
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
            level++;
        }
        return true;
    }
};
