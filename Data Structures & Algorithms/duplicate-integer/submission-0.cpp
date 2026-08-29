class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int i : nums) {
            if (!seen.insert(i).second) {
                return true;
            }
        }

        return false;
    }
};