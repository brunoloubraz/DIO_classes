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