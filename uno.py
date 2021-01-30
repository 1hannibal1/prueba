n = int(input("Ingrese numero del 1 al 4 : "))

cargo = ["Operador", "Tecnico", "Supervisor","Jefe"]
sueldo = [100,1400,1800,2300]

if (n >= 1 and n <= 4):
    c = cargo[n - 1]
    s = sueldo[n - 1]
else:
    c = "Desconocido"
    s = 0
print(c, " - ", s)