class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        vector<pair<int, int>> freqVec(count.begin(), count.end());
        sort(freqVec.begin(), freqVec.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second; // sort by frequency descending
        });

        vector<int> result;
        for (int i = 0; i < k && i < freqVec.size(); ++i) {
            result.push_back(freqVec[i].first);
        }
        return result;
    }
};