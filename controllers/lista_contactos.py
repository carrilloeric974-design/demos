import web
import sqlite3

render = web.template.render('views', base='layout')

class ListaContactos:

    def consultarContactos(self):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()

            query = """
                SELECT id_contacto, nombre, primer_apellido, segundo_apellido, email, telefono
                FROM contactos
            """
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                contacto = {
                    "id_contacto": fila[0],
                    "nombre": fila[1],
                    "primer_apellido": fila[2],
                    "segundo_apellido": fila[3],
                    "email": fila[4],
                    "telefono": fila[5]
                }
                datos.append(contacto)

            conexion.close()
            return datos
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return []

    def GET(self):
        contactos = self.consultarContactos()
        return render.lista_contactos(contactos) # type: ignore