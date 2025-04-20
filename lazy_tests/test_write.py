from divine import Heaven, Paradise

class MainMenu(Heaven):

    def main(self):
        self.write("Hello, World!", 1, 4)
        paradise = Paradise(self, (2, 0), border=True)
        paradise.write("Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original.", 2, 4)
        self.realm.getch()

MainMenu(coordinate=(15, 20), width=50, height=20, border=True).run()
