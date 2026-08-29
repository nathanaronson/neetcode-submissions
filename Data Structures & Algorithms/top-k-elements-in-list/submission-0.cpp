class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        int n = nums.size();

        for (int i : nums) map[i]++;

        vector<vector<int>> bucket(n + 1);

        for (auto& [a, b] : map) {
            bucket[b].push_back(a);
        }

        int m = 0;
        vector<int> res(k);
        for (auto it = bucket.rbegin(); it != bucket.rend(); ++it) {
            vector<int> v = *it;
            for (int i : v) {
                res[m++] = i;
                if (m == k) return res;
            }
        }

        return {};
    }
};