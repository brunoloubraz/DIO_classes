curso = "pYtHon"
curso2 = "  pYtHon  "

print(curso.upper())
print(curso.lower())
print(curso.title())

print(curso2.strip() + ".")
print(curso2.lstrip()+ ".")
print(curso2.rstrip() + ".")

print(curso.center(10, "#"))
print(curso.center(20, "#"))
print(".".join(curso))

month = 1

months_dict = {
  "1":"January"

}
print(months_dict)
print(months_dict)

dog = "doguinho"
    
print(dog[:-1])
if month == 1:
  print(months_dict[0])
n = 1

while(n > 0):
  a = 'dog'
  b = 'big'
  n -= 1  
  if a[-1] == b[-1]:
    print("encaixa")
  else:
    print("nao encaixa")
