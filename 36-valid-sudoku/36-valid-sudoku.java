class Solution {
    public boolean isValidSudoku(char[][] board) {
    for(int i = 0; i<9; i++){
        HashSet<Character> rows = new HashSet<Character>();
        HashSet<Character> columns = new HashSet<Character>();
        HashSet<Character> cube = new HashSet<Character>();
        for (int j = 0; j < 9;j++){
            if(board[i][j]!='.' && rows.contains(board[i][j]))
                return false;
            else
                rows.add(board[i][j]);
            if(board[j][i]!='.' && columns.contains(board[j][i]))
                return false;
            else
                columns.add(board[j][i]);
            int RowIndex = 3*(i/3);
            int ColIndex = 3*(i%3);
            if(board[RowIndex + j/3][ColIndex + j%3]!='.' && cube.contains(board[RowIndex + j/3][ColIndex + j%3]))
                return false;
            else
                cube.add(board[RowIndex + j/3][ColIndex + j%3]);
            
        }
    }
    return true;
}
}