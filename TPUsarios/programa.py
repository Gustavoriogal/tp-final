import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tp'
)
cursor = conn.cursor()

def login(usuario, contraseña):
    cursor.execute('SELECT es_admin FROM usuarios WHERE usuario = %s AND contraseña = %s', (usuario, contraseña))
    es_admin = cursor.fetchone()

    return es_admin

def registrar_usuario(usuario, contraseña, es_admin):
    cursor.execute('INSERT INTO usuarios (usuario, contraseña, es_admin) VALUES (%s, %s, %s)', (usuario, contraseña, es_admin))
    conn.commit()

def modificar_contraseña(usuario, nueva_contraseña):
    cursor.execute('UPDATE usuarios SET contraseña = %s WHERE usuario = %s', (nueva_contraseña, usuario))
    conn.commit()
    cursor.fetchall()

def eliminar_usuario(usuario):
    cursor.execute('DELETE FROM usuarios WHERE usuario = %s', (usuario,))
    conn.commit()

def mostrar_usuarios():
    cursor.execute('SELECT usuario, es_admin FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario, es_admin in usuarios:
        print(f'Usuario: {usuario}, Es administrador: {"Sí" if es_admin else "No"}')

def ingresar_producto(nombre, precio, stock):
    cursor.execute('INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)', (nombre, precio, stock))
    conn.commit()

def modificar_producto(producto_id, nombre, precio, stock):
    cursor.execute('UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s', (nombre, precio, stock, producto_id))
    conn.commit()

def agregar_stock(producto_id, cantidad):
    cursor.execute('UPDATE productos SET stock = stock + %s WHERE id = %s', (cantidad, producto_id))
    conn.commit()

def ver_stock_productos():
    cursor.execute('SELECT id, nombre, stock FROM productos')
    productos = cursor.fetchall()
    for producto_id, nombre, stock in productos:
        print(f'ID: {producto_id}, Producto: {nombre}, Stock: {stock}')

def ver_todos_los_productos():
    cursor.execute('SELECT id, nombre, precio, stock FROM productos')
    productos = cursor.fetchall()
    for producto_id, nombre, precio, stock in productos:
        print(f'ID: {producto_id}, Producto: {nombre}, Precio: {precio}, Stock: {stock}')

def menu():
    print("1. Registrar usuario")
    print("2. Modificar usuario")
    print("3. Eliminar usuario")
    print("4. Mostrar todos los usuarios")
    print("5. Ingresar producto")
    print("6. Modificar producto")
    print("7. Agregar stock a un producto")
    print("8. Ver stock de productos")
    print("9. Ver todos los productos")
    print("10. Salir")

def main():
    while True:
        print("Bienvenido al sistema de administración del local")
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        
        es_admin = login(usuario, contraseña)
        if es_admin:
            print("Inicio de sesión exitoso como administrador")
            break
        else:
            print("Inicio de sesión fallido. Intente nuevamente.")
    
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nuevo_usuario = input("Ingrese el nombre del nuevo usuario: ")
            nueva_contraseña = input("Ingrese la contraseña del nuevo usuario: ")
            es_admin = int(input("¿Es administrador? (1: Sí / 0: No): "))
            registrar_usuario(nuevo_usuario, nueva_contraseña, es_admin)
            print("Usuario registrado exitosamente.")
        elif opcion == 2:
            print("Modificar Usuario")
            usuario_modificar = input("Ingrese el nombre del usuario a modificar: ")
            cursor.execute('SELECT usuario FROM usuarios WHERE usuario = %s', (usuario_modificar,))
            usuario_existente = cursor.fetchone()
            if usuario_existente:
                nueva_contraseña = input("Ingrese la nueva contraseña: ")
                modificar_contraseña(usuario_modificar, nueva_contraseña)
                print("Contraseña modificada exitosamente.")
            else:
                print("El usuario no existe.")
        elif opcion == 3:
            print("Eliminar Usuario")
            usuario_eliminar = input("Ingrese el nombre del usuario a eliminar: ")
            cursor.execute('SELECT usuario FROM usuarios WHERE usuario = %s', (usuario_eliminar,))
            usuario_existente = cursor.fetchone()
            if usuario_existente:
                eliminar_usuario(usuario_eliminar)
                print("Usuario eliminado exitosamente.")
            else:
                print("El usuario no existe.")
        elif opcion == 4:
            mostrar_usuarios()
        elif opcion == 5:
            nombre = input("Ingrese el Nombre: ")
            precio = input("Ingrese el Precio: ")
            stock = int(input("Ingrese el Stock: "))
            ingresar_producto(nombre, precio, stock)
        elif opcion == 6:
            print("Modificar Producto")
            producto_id = input("Ingrese el ID del producto a modificar: ")

            # Verificar si el producto existe
            cursor.execute('SELECT id FROM productos WHERE id = %s', (producto_id,))
            producto_existente = cursor.fetchone()

            if producto_existente:
                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                nuevo_precio = input("Ingrese el nuevo precio del producto: ")
                nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
                modificar_producto(producto_id, nuevo_nombre, nuevo_precio, nuevo_stock)
                print("Producto modificado exitosamente.")
            else:
                print("El producto no existe.")
        elif opcion == 7:
            print("Agregar Stock a un Producto")
            producto_id = input("Ingrese el ID del producto al que desea agregar stock: ")

            # Verificar si el producto existe
            cursor.execute('SELECT id FROM productos WHERE id = %s', (producto_id,))
            producto_existente = cursor.fetchone()

            if producto_existente:
                cantidad_agregar = int(input("Ingrese la cantidad de stock a agregar: "))
                agregar_stock(producto_id, cantidad_agregar)
                print("Stock agregado exitosamente.")
            else:
                print("El producto no existe.")
        elif opcion == 8:
            ver_stock_productos()
        elif opcion == 9:
            ver_todos_los_productos()
        elif opcion == 10:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()


