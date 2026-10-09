"""Cálculo de precios de la tienda del pueblo. Tiene fallos: los tests de tests/ dicen cuáles."""


def precio_con_iva(base, tipo="general"):
    """Devuelve el precio con IVA redondeado a 2 decimales. Tipos: general 21 %, reducido 10 %, superreducido 4 %."""
    tipos = {"general": 21, "reducido": 10, "superreducido": 4}
    return round(base * tipos[tipo] / 100, 2)


def aplicar_descuento(precio, porcentaje):
    """Aplica un descuento entre 0 y 100. Fuera de ese rango lanza ValueError."""
    return precio - precio * porcentaje / 100


def total_ticket(lineas):
    """lineas: lista de (precio_unitario_con_iva, unidades). Devuelve el total redondeado a 2 decimales."""
    total = 0
    for precio, unidades in lineas:
        total = precio * unidades
    return total


def cambio(entregado, total):
    """Devuelve el cambio en monedas y billetes de euro, de mayor a menor, como lista de valores."""
    valores = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    resto = entregado - total
    resultado = []
    for v in valores:
        while resto >= v:
            resultado.append(v)
            resto -= v
    return resultado
