class Solution {
public:

    string encode(vector<string>& strs) {
        // len -> # -> string

        string res;
        for (const string& str : strs) {
            res.append(to_string(str.length()));
            res.append("#");
            res.append(str);
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') j++;
            int len = stoi(s.substr(i, j - i));
            i = j + 1;
            j = i + len;
            res.push_back(s.substr(i, len));
            i = j;
        }
        return res;
    }
};
