clientes=[
     ["juan",3100],
     ["maria",3101],
     ["pedro",3102],
     ["laura",3103]
     ]
libros=[
     [12552,"iliada",5300,25],
     [12553,"platero",2500,16],
     [12554,"cien",3600,35]
     ]
ventas=[
     (1020,3100,12552,4,21200),
     (1025,3102,12553,2,5000),
     (1030,3100,12554,3,10800),
     (1035,3101,12553,9,22500)
     ]

def menu_principal():
    while True:
        print(">>> MENU PRINCIPAL <<<")
        print("1.Clientes")
        print("2.Libros")
        print("3.Ventas")
        print("4.Estadisticas")
        print("5.Salir")
        opcion=input("ingrese una opcion: ")
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_libros()
        elif opcion == '3':
            menu_ventas()
        elif opcion == '4':
            menu_estadisticas()
        elif opcion=='5':
            break
        else:
            print("opcion invalida, intente nuevamente")
          
def menu_clientes():
    while True:
        print(">>> MENU CLIENTES <<<")
        print("1.Ingresar clientes")
        print("2.Actualizar cliente")
        print("3.Lista de cliente")
        print("4.Borrar cliente")
        print("5.Buscar cliente")
        print("6.Salir")
        opcion1=input("ingrese una opcion: ")
     
        if opcion1 == '1':
            ingresar_clientes()
        elif opcion1 == '2':
            actualizar_cliente()
        elif opcion1 == '3':  
            lista_clientes()
        elif opcion1 == '4':
            borrar_cliente()
        elif opcion1 == '5':
            buscar_cliente()
        elif opcion1 == '6':
            menu_principal()
        else:
            print("opcion ivalida 'intente nuevamente'")

def ingresar_clientes():
    while True:
        print("--------------------------------------------------------")
        print("Para salir, ingrese '5' en ambos campos.")
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre == '5':
            break
        codigo = int(input("Ingrese el código del cliente: "))
        print("--------------------------------------------------------")
        for cliente in clientes:
            if codigo == cliente[1]:
                print("El código ya ha sido registrado.")
                break
        else:
            clientes.append([nombre, codigo])
            print("Cliente registrado exitosamente.")
            
def lista_clientes():

    print("--------------------------------------------------------")
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente[0]}, Código: {cliente[1]}")
    print("--------------------------------------------------------")

def actualizar_cliente():
    while True:
        print("------------------")
        print("Actualizar Cliente")
        print("------------------")
        print("1). Actualizar nombre.")
        print("2). Actualizar Codigo.")
        print("3). para salir.")
        opcion = int(input("Digite una opcion: "))
                #Actualizar nombre.
        if opcion == 1:

            while True:

                nombreAnterior = input("\nIngrese el nombre anterior(1. para salir): ")
                if nombreAnterior != "1":

                    encontrar = False
                    for nombres in clientes:
                        if nombreAnterior in nombres:
                            encontrar = True
                            break

                    if encontrar:
                        while True:
                            nombreNuevo = input("Digite el nombre nuevo: ")
                            for subCliente in clientes:
                                if nombreAnterior in subCliente:
                                    subCliente[0] = nombreNuevo
                            print(f"{nombreAnterior} ha sido actualizado a {nombreNuevo}.")
                            break

                    else:
                        print(f"{nombreAnterior} no se encuentra en la lista...")        

                else:
                    print("Saliendo...")
                    break
        elif opcion == 2:

            while True:
                codigoAnterior = int(input("Ingrese el codigo que desea actualizar(0. para salir): "))
                if codigoAnterior != "x":
                    if codigoAnterior >= 1000 and codigoAnterior < 10000:                
                        encontrarCodigo = False
                        for codigo in clientes:
                            if codigoAnterior in codigo:
                                encontrarCodigo = True
                                break

                        if encontrarCodigo:    
                            
                            while True:
                                codigoNuevo = int(input("Digite el codigo nuevo: "))
                                if codigoNuevo >= 1000 and codigoNuevo < 10000:    
                                    for subClienteCod in clientes:
                                        if codigoAnterior in subClienteCod:
                                            subClienteCod[1] = codigoNuevo
                                    print(f"{codigoAnterior} ha sido actualizado a {codigoNuevo}.")
                                    break
                                else:
                                    print("El código es inválido.")
                        else:
                            print("El código no se encuentra registrado.")
                    else:
                        print("El codigo es inválido.")

                continuar = input("Quiere continuar? 1. para continuar o 2. para salir.: ")
                if continuar == "1":
                    print("Continuando...")
                elif continuar == "2":
                    print("Saliendo...")
                    break
                else:
                    print("Digite una opción valida.")


        elif opcion == 3:
            print("Saliendo de Actualizar...")
            break
        else:
            print("Digite una opcón válida.")

def borrar_cliente():
    while True:
        print("--------------------------------------------------------")
        codigo = int(input("Ingrese el código del cliente a borrar - ingrese '5' para salir: "))
        if codigo == 5:
            break
        cliente_encontrado = False
        for cliente in clientes:
            if cliente[1] == codigo:
                cliente_encontrado = True
                for venta in ventas:
                    if venta[1] == codigo:
                        print("El cliente no se puede eliminar porque tiene compras registradas.")
                        break
                else:
                    clientes.remove(cliente)
                    print(f"El cliente con código {codigo} y nombre {cliente[0]} ha sido eliminado.")
                break
        else:
            if not cliente_encontrado:
                print("El cliente no existe.")


def buscar_cliente():
    while True:
        print("--------------------------------------------------------")
        cd_cliente = int(input("Ingrese el código del cliente - ingrese '5' para salir: "))
        if cd_cliente == 5:
            break
        cliente_encontrado = False
        pos = 0
        for cliente in clientes:
            pos += 1
            if cliente[1] == cd_cliente:
                cliente_encontrado = True
                print("--------------------------------------------------------")
                print(f"Nombre del cliente: {cliente[0]}. Código del cliente: {cliente[1]}.")
                print(f"Ubicación en la lista: {pos}")
                print("--------------------------------------------------------")
                break
        if not cliente_encontrado:
            print("el codigo no esta registrado")
     
def menu_libros():
    while True:
        print(">>> MENU LIBROS <<<")
        print("1.Ingresar libros")
        print("2.Lista de libros")
        print("3.Borrar libros")
        print("4.Buscar libro")
        print("5.Salir")
        opcion1=input("ingrese una opcion: ")
        if opcion1== '1':
            ingresar_libros()
        elif opcion1 == '2':
            lista_libros()
        elif opcion1 == '3':
            borrar_libro()
        elif opcion1 == '4':
            buscar_libro()
        elif opcion1 == '5':
            menu_principal()
        else:
            print("opcion invalida - intente nuevamente")

def ingresar_libros():
    while True:
        print(">>> MENUU DE INGRESO DE LIBRO <<<")
        print("1.Ingresar libro nuevo")
        print("2.Actualizar cantidad de libros")
        print("3.Actualizar precio del libro")
        print("4.Volver al menu libros")
        opcion3=input("ingrese una opcion: ")

        if opcion3 == '1':
            ingreso_libros()
        elif opcion3 == '2':
            actualizar_cantidad()
        elif opcion3 == '3':
            actualizar_precio()
        elif opcion3 == '4':
            menu_libros()
        else:
            print("opcion invalida - intente nuevamente")

def ingreso_libros():
    while True:
        print("--------------------------------------------------------")
        print("Para salir, ingrese '5' en todos los campos.")
        nombre = input("Ingrese el nombre del libro: ")
        if nombre == '5':
            break
        codigo = int(input("Ingrese el código del libro: "))
        precio = float(input("Ingrese el precio del libro: "))
        unidades = int(input("Ingrese la cantidad de unidades recibidas: "))
        print("--------------------------------------------------------")
        for libro in libros:
            if codigo == libro[0]:
                print("El código ya ha sido registrado.")
                break
        else:
            libros.append([codigo, nombre, precio, unidades])
            print("Libro registrado exitosamente.")

def actualizar_cantidad():
    print("--------------------------------------------------------")
    codigo = int(input("Ingrese el código del libro: "))
    for libro in libros:
        if codigo == libro[0]:
            accion = input("¿Desea sumar (+) o restar (-) unidades al inventario?: ").strip()
            if accion == '+':
                unidades = int(input("Ingrese la cantidad de unidades a sumar: "))
                libro[3] += unidades
                print(f"Se han agregado {unidades} unidades del libro {libro[1]}. Nuevo total: {libro[3]}")
            elif accion == '-':
                unidades = int(input("Ingrese la cantidad de unidades a restar: "))
                if unidades <= libro[3]:
                    libro[3] -= unidades
                    print(f"Se han restado {unidades} unidades del libro {libro[1]}. Nuevo total: {libro[3]}")
                else:
                    print(f"No se pueden restar más unidades de las disponibles ({libro[3]}).")
            else:
                print("Opción no válida. Ingrese '+' para sumar o '-' para restar unidades.")
            break
    else:
        print("El código no está registrado.")
    print("--------------------------------------------------------")

def actualizar_precio():
    print("--------------------------------------------------------")
    codigo = int(input("Ingrese el código del libro a actualizar: "))
    precio = float(input("Ingrese el nuevo precio del libro: "))
    libro_encontrado = False
    for libro in libros:
        if libro[0] == codigo:
            libro[2] = precio
            libro_encontrado = True
            print(f"Se ha actualizado el precio del libro con código {codigo} a ${precio}.")
            break
    if not libro_encontrado:
        print("El libro no está registrado en la lista.")
    print("--------------------------------------------------------")

def lista_libros():
    print("--------------------------------------------------------")
    print("Lista de libros:")
    for libro in libros:
        print(f"Código: {libro[0]}, Nombre: {libro[1]}, Precio: {libro[2]}, Unidades disponibles: {libro[3]}")
    print("--------------------------------------------------------")

def borrar_libro():
    while True:
        codigo = int(input("Ingrese el código del libro a borrar - ingrese '5' para salir: "))
        if codigo == 5:
            break
        libro_encontrado = False
        for libro in libros:
            if libro[0] == codigo:
                libro_encontrado = True
                for venta in ventas:
                    if venta[1] == codigo:
                        print("El libro no se puede eliminar porque tiene ventas registradas.")
                        break
                else:
                    libros.remove(libro)
                    print(f"El libro con código {codigo} y nombre {libro[1]} ha sido eliminado.")
                break
        if not libro_encontrado:
            print("El libro no existe.")

def buscar_libro():
    while True:
        print("--------------------------------------------------------")
        cd_libro = int(input("Ingrese el código del libro - ingrese '5' para salir: "))
        if cd_libro == 5:
            break
        libro_encontrado = False
        pos = 0
        for libro in libros:
            pos += 1
            if libro[0] == cd_libro:
                libro_encontrado = True
                print("--------------------------------------------------------")
                print(f"Nombre del libro: {libro[1]}. Código del libro: {libro[0]}.")
                print(f"Ubicación en la lista: {pos}")
                print("--------------------------------------------------------")
                break
        if not libro_encontrado:
            print("El código no está registrado.")

def menu_ventas():
    while True:
        print(">>> MENU VENTAS <<<")
        print("1.Realizar venta")
        print("2.Lista de ventas realizadas")
        print("3.Buscar venta realizada")
        print("4.Salir")
        opcion4=input("ingrese una opcion: ")
        if opcion4 == '1':
            registrar_venta()
        elif opcion4 == '2':
            mostrar_ventas()
        elif opcion4 == '3':
            buscar_venta_menu()
        elif opcion4 == '4':
            menu_principal()
        else:
            print("opcion invalida")

def generar_codigo_venta(cliente_actual):
    codigo_actual = ventas[-1][0] # obtener el codigo de venta mas alto
    codigo_cliente_actual = cliente_actual[1]
    nuevo_codigo = codigo_actual + 5 if codigo_actual != 0 else 1020
    return nuevo_codigo, codigo_cliente_actual

def buscar_cl(codigo):
    for cliente in clientes:
        if cliente[1] == codigo:
            return cliente
    return None

def buscar_li(codigo):
    for libro in libros:
        if libro[0] == codigo:
            return libro
    return None

def registrar_venta():
    codigo_cliente = int(input("Ingrese el codigo del cliente: "))
    cliente = buscar_cl(codigo_cliente)
    if cliente is None:
        print("El cliente no existe.")
        return
    codigo_libro = int(input("Ingrese el codigo del libro: "))
    libro = buscar_li(codigo_libro)
    if libro is None:
        print("El libro no existe.")
        return
    cantidad = int(input("Ingrese la cantidad vendida: "))
    if cantidad > libro[3]:
        print("No hay suficientes unidades disponibles.")
        return
    nuevo_codigo_venta, codigo_cliente_actual = generar_codigo_venta(cliente)
    valor_venta = cantidad * libro[2]
    venta = (nuevo_codigo_venta, codigo_cliente_actual, codigo_libro, cantidad, valor_venta)
    ventas.append(venta)
    libro[3] -= cantidad
    print("Venta registrada exitosamente.")
    print(f"codigo de venta: {nuevo_codigo_venta}")


def mostrar_ventas():
    print(">>> Lista de ventas realizadas <<<")
    for venta in ventas:    
        print(f"Código de venta: {venta[0]}")
        print(f"Código del cliente: {venta[1]}")
        print(f"Código del libro: {venta[2]}")
        print(f"Cantidad vendida: {venta[3]}")
        print(f"Valor de la venta: ${venta[4]}")
        print("--------------------------------------------------------")

def buscar_venta(codigo_venta):
    for venta in ventas:
        if venta[0] == codigo_venta:
            return venta
    return None

def buscar_venta_menu():
    while True:
        print("para salir ingrese '0' ")
        codigo_venta = int(input("Ingrese el código de la venta a buscar: "))
        venta = buscar_venta(codigo_venta)
        if codigo_venta==0:
            break
        if venta is None:
            print("La venta no fue encontrada.")
        else:
            print("--------------------------------------------------------")
            print(f"Código de venta: {venta[0]}")
            print(f"Código de cliente: {venta[1]}")
            print(f"Código de libro: {venta[2]}")
            print(f"Cantidad vendida: {venta[3]}")
            print(f"Valor de venta: {venta[4]}")
            print("--------------------------------------------------------")

def menu_estadisticas():
    while True:
        print(">>> MENU ESTADISTICAS <<<")
        print("1.Ventas totales de libros por ISBN")
        print("2.Libro mas y menos vendido")
        print("3.Venta total de la libreria")
        print("4.Cliente con mayor compra por venta")
        print("5.Cliente con mayor volumen de compra total")
        print("6.Salir")
        opcion5=int(input("ingrese una opcion:" ))

        if opcion5 == 1:
            obtener_ventas_totales_por_codigo_libro()
        elif opcion5 == 2:
            mostrar_libros_mas_y_menos_vendido()
        elif opcion5 == 3:
            print("Venta Total de la librería:", venta_total_libreria)
        elif opcion5 == 4:
             obtener_cliente_con_mayor_compra_por_venta()
        elif opcion5 ==5:
            obtener_cliente_con_mayor_volumen_compra_total()
        elif opcion5 == 6:
            menu_principal()
        else:
            print("opcincion inavalida")

def obtener_ventas_totales_por_codigo_libro():
   while True:
        codigo_libro = int(input("Ingrese el código del libro: "))
        if codigo_libro==0:
            break
        ventas_totales = 0
        for venta in ventas:
            if venta[2] == codigo_libro:
                ventas_totales += venta[3]
                print("Las ventas totales del libro con código", codigo_libro, "son:", ventas_totales)
        return ventas_totales
   
def mostrar_libros_mas_y_menos_vendido():
    libros_vendidos = [] 

    # Contar las ventas de cada libro
    for venta in ventas:
        codigo_libro = venta[2]
        encontrado = False
        for i in range(len(libros_vendidos)):
            if libros_vendidos[i][0] == codigo_libro:
                libros_vendidos[i][1] += venta[3]
                encontrado = True
                break
        if not encontrado:
            libros_vendidos.append([codigo_libro, venta[3]])

    # Encontrar el libro más vendido
    max_vendidos = libros_vendidos[0]
    for libro in libros_vendidos:
        if libro[1] > max_vendidos[1]:
            max_vendidos = libro
    codigo_mas_vendido = max_vendidos[0]
    unidades_mas_vendidas = max_vendidos[1]

    # Encontrar el libro menos vendido
    min_vendidos = libros_vendidos[0]
    for libro in libros_vendidos:
        if libro[1] < min_vendidos[1]:
            min_vendidos = libro
    codigo_menos_vendido = min_vendidos[0]
    unidades_menos_vendidas = min_vendidos[1]

    print("==============================================")
    print("Libro más vendido:")
    print("Código:", codigo_mas_vendido)
    print("Unidades vendidas:", unidades_mas_vendidas)
    print("==============================================")
    print("Libro menos vendido:")
    print("Código:", codigo_menos_vendido)
    print("Unidades vendidas:", unidades_menos_vendidas)
    print("==============================================")





def calcular_venta_total_libreria():
    venta_total = 0

    for venta in ventas:
        valor_venta = venta[4]
        venta_total += valor_venta
    return venta_total
venta_total_libreria = calcular_venta_total_libreria()

def obtener_cliente_con_mayor_compra_por_venta():
    total_compras_por_cliente = {}

    for venta in ventas:
        codigo_cliente = venta[1]
        valor_venta = venta[4]

        if codigo_cliente in total_compras_por_cliente:
            total_compras_por_cliente[codigo_cliente] += valor_venta
        else:
            total_compras_por_cliente[codigo_cliente] = valor_venta

    cliente_max_compra_por_venta = max(total_compras_por_cliente, key=total_compras_por_cliente.get, default=None)

    if cliente_max_compra_por_venta is not None:
        for cliente in clientes:
            if cliente[1] == cliente_max_compra_por_venta:
                cantidad_precio_gastado = total_compras_por_cliente[cliente_max_compra_por_venta]
                print(f"El cliente {cliente[0]} realizó la mayor compra con un total de {cantidad_precio_gastado}$ en gastos.")
                return cliente[0], cantidad_precio_gastado

    return None, 0


def obtener_cliente_con_mayor_volumen_compra_total():
    volumen_compra_total = {}
    cliente_max_volumen_compra_total = ""

    for venta in ventas:
        codigo_cliente = venta[1]
        valor_venta = venta[4]

        if codigo_cliente in volumen_compra_total:
            volumen_compra_total[codigo_cliente] += valor_venta
        else:
            volumen_compra_total[codigo_cliente] = valor_venta

    max_volumen_compra_total = 0
    for cliente in volumen_compra_total:
        if volumen_compra_total[cliente] > max_volumen_compra_total:
            max_volumen_compra_total = volumen_compra_total[cliente]
            for c in clientes:
                if c[1] == cliente:
                    cliente_max_volumen_compra_total = c[0]
                    break

    return cliente_max_volumen_compra_total


menu_principal()