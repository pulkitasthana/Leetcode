class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # dp0[x][y] = number of arrays with x zeros and y ones ending with 0
        # dp1[x][y] = number of arrays with x zeros and y ones ending with 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # prefix sums:
        # pref1[x][y] = sum_{i=0..x} dp1[i][y]
        # pref0[x][y] = sum_{j=0..y} dp0[x][j]
        pref1 = [[0] * (one + 1) for _ in range(zero + 1)]
        pref0 = [[0] * (one + 1) for _ in range(zero + 1)]

        # base: arrays that consist of a single starting block
        for k in range(1, min(limit, zero) + 1):
            dp0[k][0] = 1
        for k in range(1, min(limit, one) + 1):
            dp1[0][k] = 1

        # build prefix sums and fill DP
        for x in range(zero + 1):
            for y in range(one + 1):
                # keep base values if they were set above
                if not (y == 0 and 1 <= x <= limit):
                    if x > 0:
                        # dp0[x][y] = sum dp1[x-k][y] for k=1..min(limit,x)
                        left = x - limit - 1
                        total = pref1[x - 1][y]
                        if left >= 0:
                            total = (total - pref1[left][y]) % MOD
                        dp0[x][y] = (dp0[x][y] + total) % MOD

                if not (x == 0 and 1 <= y <= limit):
                    if y > 0:
                        # dp1[x][y] = sum dp0[x][y-k] for k=1..min(limit,y)
                        left = y - limit - 1
                        total = pref0[x][y - 1]
                        if left >= 0:
                            total = (total - pref0[x][left]) % MOD
                        dp1[x][y] = (dp1[x][y] + total) % MOD

                # update prefix sums
                pref1[x][y] = (dp1[x][y] + (pref1[x - 1][y] if x > 0 else 0)) % MOD
                pref0[x][y] = (dp0[x][y] + (pref0[x][y - 1] if y > 0 else 0)) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
