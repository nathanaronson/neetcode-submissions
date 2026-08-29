class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(curr, curr_open, open_left):
            nonlocal res
            if open_left == 0 and curr_open == 0:
                res.append(curr)
                return
            if curr_open > 0:
                recurse(curr + ')', curr_open - 1, open_left)
            if open_left > 0:
                recurse(curr + '(', curr_open + 1, open_left - 1)

        recurse('', 0, n)
        return res