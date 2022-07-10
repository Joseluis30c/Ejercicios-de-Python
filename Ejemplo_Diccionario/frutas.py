frutas={"Plátano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}
a=input("¿Qué fruta desea? ").title()
kg=float(input("¿Cuántos kilos? "))
if a in frutas:
    print(kg, "kilos de", a, "cuestan", round(frutas[a]*kg,2))
else: 
    print("La fruta", a, "no está en venta.")
