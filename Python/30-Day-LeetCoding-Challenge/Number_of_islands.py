'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''



class Solution(object):
    def floodfill(self, grid, x,y, prev, new, m,n):
        if x>=m or y>=n or x<0 or y<0:
            return
        if grid[x][y]!=prev:
            return 
        grid[x][y]=new
        self.floodfill(grid,x+1, y, prev, new,m,n)
        self.floodfill(grid, x,y+1, prev, new, m,n)
        self.floodfill(grid, x,y-1, prev, new, m,n)
        self.floodfill(grid, x-1,y, prev, new, m,n)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        
       
        
        count=0
        
        for i in range (0,m):
            for j in range (0,n):
                if grid[i][j]=='1':
                    count=count+1
                    self.floodfill(grid, i, j, '1', '0',m,n)
                    
        return count
