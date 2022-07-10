total=0
monto=float(input("Monto de su compra (o para salir): "))
while monto!=0:
    if monto<0:
        print("Monto no valido.")
    else:
        total+=monto
    monto=float(input("Monto de su compra (0 para salir): "))
if total>1000:
    total-=total*0.1
print("Su monto total a pagar es de ", total, "soles")
