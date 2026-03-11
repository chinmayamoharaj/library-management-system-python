# EMI calculator.

p=int(input("Enter the principal amount:- "))
y=float(input("Enter the year :- "))
r=int(input("Enter the rate of interest :- "))
m=12*y
ri=(r/12)/100
Emi=(p*ri*(1+ri)**m)/(((1+ri)**m)-1)
s_i=(Emi*m)-p
T_A=p+s_i
print("Total payable amount:- ",round(T_A))
print("*"*50)
print("Total interest:- ",round(s_i))
print("*"*50)
print("Total EMI per month:- ",round(Emi))

