class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int longest = 0;

        for (int i : s) {
            if (s.count(i - 1)) continue;
            int curr = 0;
            int j = i;
            while (s.count(j++)) curr++;
            longest = max(longest, curr);
        }

        return longest;
    }
};
