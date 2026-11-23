# LC 695 Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
# 日期: 2026-11-21 | 章节: 图论 | 结果: B | 用时: 15min

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        directions = [ (-1,0), (1,0),(0,-1),(0,1) ]
        def dfs(i,j):

            if i < 0 or i >= rows or j <0 or j >= cols:
                return 0
            if grid[i][j]==[0]:
                return 0

            area = 1 
            grid[i][j] = [0]
            for dr, dc in directions:
                nr,nc = i+dr, j+dc
                area+=dfs(nr,nc)
            return area

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(area, maxArea)
        return maxArea
