#include <bits/stdc++.h>
#define ll long long;
using namespace std;

//depth-first-search to count rooms

class CountingRooms{
    public:
        int rows, cols;
        //direction right, left, up, down;
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        //constructor
        CountingRooms(int r, int c){
            rows= r; 
            cols=c;
        }

        int solve(vector<string> &grid){
            int ans=0;
            for(int r=0; r<rows; r++){
                for(int c=0;c<cols;c++){
                    if(grid[r][c] == '.'){
                        ans++;
                        dfs(r,c,grid);
                    }
                }
            }
            return ans;
        }

        void dfs(int row, int col, vector<string> &grid){
            grid[row][col] = '#';
            for(int curr=0; curr<4; curr++){
                int r = row+directions[curr][0];
                int c = col+directions[curr][1];
                if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == '#') continue;
                dfs(r, c, grid);
            }
        }
};

int main(){
    //input
    int rows, cols;
    cin >> rows >> cols;
    vector<string> grid(rows);
    for (int i=0; i<rows; i++){
        cin >> grid[i];
    }
    CountingRooms solver(rows, cols);
    cout << solver.solve(grid);
    return 0;
}

