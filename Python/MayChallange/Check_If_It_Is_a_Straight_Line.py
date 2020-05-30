class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates)==2:
            return True
        
        n=len(coordinates)
        x1=coordinates[0][0]
        y1=coordinates[0][1]
        
        x0=coordinates[1][0]
        y0=coordinates[1][1]
        
        dy=y1-y0
        dx=x1-x0
    
        for i in range (0,n):
            x=coordinates[i][0]
            y=coordinates[i][1]
          #  print(x,y)
            if ((y-y1)*dx)!=((x-x1)*dy):
           #     print((y-y1)*dx)
            #    print((x-x1)*dy)
             #   print("yui")
                return False
            
        return True
