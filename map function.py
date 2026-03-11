oldsal=[1000,2000,3000] #existing list

def salhike(s): #function definition
    return s+(s*50/100)

mapobj=list(map(salhike,oldsal)) #map function process
print("New sal:- ",mapobj) # new list from the existing list applying certain condition or modification 
