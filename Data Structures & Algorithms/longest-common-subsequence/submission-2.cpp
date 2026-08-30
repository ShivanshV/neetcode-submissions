class Solution {
public:
    int helper(string text1,string text2,int i,int j,int m,int n,vector<vector<int>>& map){
        if(i==m || j==n) return 0;
        if(map[i][j]>0) return map[i][j];
        if(text1[i]==text2[j]){
            return map[i][j] = 1 + helper(text1,text2,i+1,j+1,m,n,map);
        }
        map[i][j] = max(helper(text1,text2,i,j+1,m,n,map),helper(text1,text2,i+1,j,m,n,map));
        return map[i][j];
    }
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();
        int i = 0,j = 0;
        vector<vector<int>> map(m,vector<int>(n,0));
        return helper(text1,text2,i,j,m,n,map);
    }
};
