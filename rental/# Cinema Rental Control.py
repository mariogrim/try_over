# Cinema Rental Control

import csv

stock = []

def stock_csv(stock):
    csvfile = open('stock.csv', 'w', newline='')
    header = ['Código', 'Detalle', 'Cantidad', 'Valor de Reposición']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    csvfile.close()
    return stock

def modificar_stock_csv(stock):
    nuevo_ingreso = 'Y'
    nuevo_codigo = ''
    nuevo_detalle = ''
    nueva_cantidad = 0
    nuevo_valor = 0
    header = ['Código', 'Detalle', 'Cantidad', 'Valor de Reposición']
    csvfile = open('stock.csv', 'w', newline='')
    stock = csv.DictWriter(csvfile, fieldnames=header)
    while nuevo_ingreso == 'Y' or nuevo_ingreso == 'N':
        if nuevo_ingreso == 'Y':
            nuevo_articulo = {
                'Código': nuevo_codigo, 
                'Delalle': nuevo_detalle,
                'Cantidad': nueva_cantidad, 
                'Valor de Reposición': nuevo_valor
                }
            stock.writerow(nuevo_articulo)
        else:
            break
        nuevo_ingreso = input('Ingresa nuevo artículo?\nIngrese Y para agregar\nIngrese N para salir'
                              ).upper()
    csvfile.close()
    return stock


def listar_pedido_csv():
    listado = []
    nuevo_articulo = 'Y'
    with open(stock) as csvfile:
        stock = list(csv.DictReader(csvfile))
    while nuevo_articulo == 'Y' or nuevo_articulo == 'N':
        if nuevo_articulo == 'Y':
            codigo = input('Ingrese articulo: ').lower()
            artic_listado = stock('Codigo', codigo, 'Detalle')




if __name__ == '__main__':
    opcion = input('Ingrese opción:\n 0 - Crear stock\n 1 - Modificar stock\n 2 - Hacer Lista')
    while opcion >= 0 and opcion <= 2:       
        if opcion == 0:
            stock_csv(stock)
            stock = stock_csv(stock)
        elif opcion == 1:
            modificar_stock_csv(stock)
            stock = modificar_stock_csv(stock)
        elif opcion == 2:
            listar_pedido_csv()
            lista_seguro = listar_pedido_csv()
    

