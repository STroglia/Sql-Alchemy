from sqlalchemy import select
from database import engine, SessionLocal
from models import Base, User

def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓN DE USUARIOS (CRUD) ---")
    print("1. Agregar un nuevo usuario (Create)")
    print("2. Ver todos los usuarios (Read)")
    print("3. Modificar un usuario (Update)")
    print("4. Eliminar un usuario (Delete)")
    print("5. Salir")

def main():
    Base.metadata.create_all(bind=engine)

    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ")

        if opcion == "1":
            print("\n--- NUEVO USUARIO ---")
            nombre = input("Ingresa el nombre de usuario: ")
            correo = input("Ingresa el email: ")
            edad_str = input("Ingresa la edad (o presiona Enter para dejar vacío): ")
            
            edad = int(edad_str) if edad_str.isdigit() else None

            with SessionLocal() as session:
                nuevo_usuario = User(username=nombre, email=correo, age=edad)
                session.add(nuevo_usuario)
                session.commit()
                print(f" ¡Usuario '{nombre}' guardado con éxito!")

        elif opcion == "2":
            print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
            with SessionLocal() as session:
                stmt = select(User)
                usuarios = session.scalars(stmt).all()

                if not usuarios:
                    print("No hay usuarios registrados todavía.")
                else:
                    for u in usuarios:
                        print(f"ID: {u.id} | Usuario: {u.username} | Email: {u.email} | Edad: {u.age}")

        elif opcion == "3":
            print("\n--- MODIFICAR USUARIO ---")
            id_str = input("Ingresa el ID del usuario que deseas modificar: ")
            
            if id_str.isdigit():
                user_id = int(id_str)
                with SessionLocal() as session:
                    usuario = session.get(User, user_id)
                    
                    if usuario:
                        print(f"\nDatos actuales -> Usuario: {usuario.username} | Email: {usuario.email} | Edad: {usuario.age}")
                        print("*(Presiona Enter sin escribir nada si no deseas cambiar un campo)*")
                        
                        nuevo_nombre = input(f"Nuevo nombre [{usuario.username}]: ")
                        nuevo_email = input(f"Nuevo email [{usuario.email}]: ")
                        nueva_edad_str = input(f"Nueva edad [{usuario.age}]: ")
                        
                        if nuevo_nombre.strip():
                            usuario.username = nuevo_nombre
                        if nuevo_email.strip():
                            usuario.email = nuevo_email
                        if nueva_edad_str.isdigit():
                            usuario.age = int(nueva_edad_str)
                        
                        session.commit()
                        print(f" ¡Usuario con ID {user_id} actualizado correctamente!")
                    else:
                        print(f" No se encontró ningún usuario con el ID {user_id}.")
            else:
                print(" Por favor, ingresa un número de ID válido.")

        elif opcion == "4":
            print("\n--- ELIMINAR USUARIO ---")
            id_str = input("Ingresa el ID del usuario que deseas eliminar: ")
            
            if id_str.isdigit():
                user_id = int(id_str)
                with SessionLocal() as session:
                    usuario_a_borrar = session.get(User, user_id)
                    
                    if usuario_a_borrar:
                        session.delete(usuario_a_borrar)
                        session.commit()
                        print(f" ¡Usuario con ID {user_id} ({usuario_a_borrar.username}) eliminado correctamente!")
                    else:
                        print(f" No se encontró ningún usuario con el ID {user_id}.")
            else:
                print(" Por favor, ingresa un número de ID válido.")

        elif opcion == "5":
            print("\n¡Saliendo del programa. Hasta luego!")
            break
        else:
            print("\n Opción no válida. Por favor, elige entre 1 y 5.")

if __name__ == "__main__":
    main()