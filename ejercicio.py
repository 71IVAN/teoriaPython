# #Pedir prodcuto, precio y cantidad
# #fx subtotal
# #fx descuento
# #fx iva
# #Neto a pagar

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad que desea llevar: "))

calcularSubtotal = lambda precio, cantidad: precio * cantidad
calcularDescuento = lambda subtotal: subtotal * 0.10
calcularIva = lambda subtotal: subtotal * 0.19
calcularNeto = lambda subtotal, descuento, iva: subtotal - descuento + iva

subtotal = calcularSubtotal(precio, cantidad)
descuento = calcularDescuento(subtotal)
iva = calcularIva(subtotal)
neto_pagar = calcularNeto(subtotal, descuento, iva)

print(f"Producto: {producto}")
print(f"Precio: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {subtotal}")
print(f"Descuento (10%): {descuento}")
print(f"IVA (19%): {iva}")
print(f"Neto a pagar: {neto_pagar}")
