class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # What is the number of the unique path from (m-1, n-1) to (i, j)?
        # base case: G(m-1,n-1) = 1
        # G(i, j) = 
        # {
        #   1 -> 0
        #   0 -> G(i+1,j) + G(i,j+1)
        # }
        # return G(0, 0)
        # n * m subproblems
        # each subproblem takes O(1) time
        # O(mn) runtime
        # memoize in O(n) time
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j + 1] if j + 1 < n else 0
        
        return dp[0]

        '''
        000   321
        000   111
        010   001
        '''