class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> map;

        for (const string& s : strs) {
            array<int, 26> freq = {};
            for (char c : s) freq[c - 'a']++;
            map[freq].push_back(s);
        }

        vector<vector<string>> res;
        res.reserve(map.size());

        for (auto& [a, b] : map) {
            res.push_back(b);
        }

        return res;
    }
};
