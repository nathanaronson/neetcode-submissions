class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i = 0; i < 9; ++i) {
            unordered_set<int> row, column, box;
            row.reserve(9);
            column.reserve(9);
            box.reserve(9);
            for(int j = 0; j < 9; ++j) {
                int x = 3 * (i / 3) + j / 3;
                int y = 3 * (i % 3) + j % 3;
                if(
                    !row.insert(board[i][j]).second &&
                    board[i][j] != '.' ||
                    !column.insert(board[j][i]).second &&
                    board[j][i] != '.' ||
                    !box.insert(board[x][y]).second &&
                    board[x][y] != '.'
                ) {
                    return false;
                }
            }
        }

        return true;
    }
};
