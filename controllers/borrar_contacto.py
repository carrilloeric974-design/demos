import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

    def buscarContacto(self, id_contacto:int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query,(id_contacto,))
            resultado = cursor.fetchone()
            conexion.close()

            if resultado:
                contacto = {
                    "id_contacto":resultado[0],
                    "nombre":resultado[1],
                    "primer_apellido":resultado[2],
                    "segundo_apellido":resultado[3],
                    "email":resultado[4],
                    "telefono":resultado[5]
                }
                return contacto
            else:
                return None
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return None
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return None

    def GET(self,id_contacto:int):
        contacto = self.buscarContacto(id_contacto)
        if contacto:
            return render.borrar_contacto(contacto)
        else:
            return "Contacto no encontrado"

    def POST(self,id_contacto:int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query,(id_contacto,))
            conexion.commit()
            conexion.close()
            # Redirige a la lista de contactos después de borrar
            raise web.seeother('/lista_contactos')
        except sqlite3.Error as error:
            return f"ERROR 104: {error.args}"
        except Exception as error:
            return f"ERROR 105: {error.args}"
