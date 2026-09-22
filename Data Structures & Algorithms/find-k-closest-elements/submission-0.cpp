class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        priority_queue<pair<int, int>> pq;

        for (int val : arr) {
            if (pq.size() < k) {
                pq.push({abs(x - val), val});
                continue;
            }

            int d = abs(x - val);
            auto [t_d, t_v] = pq.top();

            if (d < t_d || (d == t_d && d < t_v)) {
                pq.push({d, val});
                pq.pop();
            }
        }

        vector<int> result;

        while (!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        sort(result.begin(), result.end());

        return result;
    }
};