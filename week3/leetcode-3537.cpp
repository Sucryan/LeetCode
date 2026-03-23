class Solution {
public:
    vector<vector<int>> specialGrid(int n) {
        // base case:
        // n = 0 時，矩陣大小是 1 x 1，只能放 0
        if (n == 0) {
            return {{0}};
        }

        // 先遞迴取得較小的 special grid
        vector<vector<int>> small = specialGrid(n - 1);

        // small 的邊長 = 2^(n-1)
        int m = small.size();

        // 一個子象限內有多少個數字
        // 例如 m=2 時，一個子象限有 4 格，所以 block=4
        int block = m * m;

        // 建立大小為 2m x 2m 的答案矩陣
        vector<vector<int>> ans(2 * m, vector<int>(2 * m));

        // 把 small 複製到四個象限
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                // 題目要求四個象限的大小順序為：
                // 右上 < 右下 < 左下 < 左上

                // 左上：最大，所以加 3 * block
                ans[i][j] = small[i][j] + 3 * block;

                // 右上：最小，所以加 0 * block
                ans[i][m + j] = small[i][j];

                // 左下：第三小，所以加 2 * block
                ans[m + i][j] = small[i][j] + 2 * block;

                // 右下：第二小，所以加 1 * block
                ans[m + i][m + j] = small[i][j] + block;
            }
        }

        return ans;
    }
};