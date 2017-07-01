import math
class point:
    def __init__(self,X,Y):
        
        self.x = X
        self.y = Y
        self.guarda = None
        
    def Move(self,X,Y):
        
        self.x = X
        self.y = Y
        
    def calculate_distance(self, B):
        
        y1 = B.y
        x1 = B.x
        y2 = self.y
        x2 = self.x
#formula de distancia
        distancia = math.sqrt(((y1 - y2)**2)+((x1 - x2)**2))
        print distancia
        
    def reset(self):
  #puntos para medir distancia      
        self.guarda = point(self.x,self.y)
        self.x = 0
        self.y = 0
        
    def regresa(self):
        
        self.x = guarda.x
        self.y = guarda.y
        
list=[]

n = raw_input("")
g = int(n)

for i in range(g):
    
    D = raw_input("")
    a = D.split(" ")
    x = int(a[0])
    y = int(a[1])
    z = point(x,y)
    
    list.append(z)
for i in range((len(list)-1)):
    
    f = list[i*2]
    t = list[(i*2)+1]
    
t.calculate_distance(f)
