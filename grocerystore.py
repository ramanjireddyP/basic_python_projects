# shopping list store
data={}
class customer:
    def __init__(self,name=None):
        self.name=name
    
    items={}
        
total=0
Flag=True

while Flag==True:
    name=input("enter customer name : ")
    obj=customer()
    data[name.lower()]=obj
    inpu=input("to quit enter q  else press anyvkey :")
    while True:

        if inpu.lower()=='q':
            break
        else:
            p=input("enter product name : ")
            price=input("enter price of product ")
           
            if p not in obj.items:
               obj.items[p]=float(price)
            else:
               obj.items[p]+=1
            total+=float(price)
            inpu=input("to quit enter q  else press enter : ")
            if inpu.lower()=='q':
                Flag=False
                break

if data:
    for j in data.values():
        for k  in j.items.keys():
            print(f"{k}={j.items[k]}")
            print("total = " ,total)

                                    
                                    
                
                
          
                
                   
           
           
    
    