class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        unordered_map<int, int> a, b;

        for (vector<int> v : trust) {
            a[v[1]]++;
            b[v[0]]++;
        }

        for (int i = 1; i <= n; ++i) if (a[i] == n - 1 && b[i] == 0) return i;

        return -1;
    }
};