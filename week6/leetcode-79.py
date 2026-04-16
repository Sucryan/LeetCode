class Solution {
public:
    vector<vector<bool>> visited;
    int dirs[4][2] = {
        {1, 0},
        {0, 1},
        {-1, 0},
        {0, -1}
    };

    bool dfs(vector<vector<char>>& board, int i, int j, string word, int c){
        int m = board.size();
        int n = board[0].size();
        if(c == word.size()){
            return true;
        }
        if(i < 0 || j < 0 || i >= m || j >= n || visited[i][j] || word[c] != board[i][j]){
            return false;
        }
        
        // 如果合理則設定為visited，開始dfs
        visited[i][j] = true;
        bool res = false;
        for(auto dir : dirs){
            res |= dfs(board, i + dir[0] , j + dir[1], word, c+1);
        }
        // 結束，還原回去以免影響其他結果
        visited[i][j] = false;
        
        return res;
    }
    bool exist(vector<vector<char>>& board, string word) {
        bool res = false;
        // 可以在這邊再初始化！！！
        int m = board.size();
        int n = board[0].size();
        visited = vector<vector<bool>>(m, vector<bool>(n, false));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(word[0] == board[i][j]){
                    res = dfs(board, i, j, word, 0);
                    if(res == true) return true;
                }
            }
        }
        return res;
    }
};