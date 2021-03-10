class sourcefinder():
    def __init__(self,map,r,c):
        self.map=map
        self.r=r
        self.c=c
        self.finpath=[]
        
    def checkpath(self,i,j):
        movleftx,movlefty=[1,0]
        movdownx,movdowny=[0,1]
        movleftx,movlefty=i+movleftx,j+movlefty
        movdownx,movdowny=i+movdownx,j+movdowny
        if i==self.r-1 and j==self.c-1:
            print(self.finpath)
            return
        if movdowny<self.c and self.map[movdownx][movdowny]==1:
            i=movdownx
            j=movdowny
            self.finpath.append([i,j])
            self.checkpath(i,j)
        elif movleftx<self.c and self.map[movleftx][movlefty]==1:
            i=movleftx
            j=movlefty
            self.finpath.append([i,j])
            self.checkpath(i,j)
        else:
            print("NO PATH TO DEST")

    def findpath(self):
        self.finpath.append([0,0])
        self.checkpath(0,0)

if __name__=="__main__":
    map=[[1,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1]]
    r=len(map)
    c=len(map)
    obj=sourcefinder(map,r,c)
    obj.findpath()