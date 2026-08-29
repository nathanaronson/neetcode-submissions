class Solution {
public:
    bool isAnagram(string s, string t) {
        int freq[26] = {};

        for (char c : s) freq[c - 'a']++;
        for (char c : t) freq[c - 'a']--;
        for (int i : freq) if (i) return false;

        return true;
    }
};
