class Productos:
    def buscarProducto(self, sku: str) -> bool: # Metodo para buscar un producto
        # TODO programar el método buscarProducto()
        print("Metodo buscarProducto ")
        return True # Regresa False si ocurrio un error en el metodo

    def buscarProducto2(self) -> bool: # Metodo para buscar un producto
        # TODO programar el método buscarProducto()
        sku = input("Ingresa un valor ")
        print("Metodo buscarProducto 2")
        return True # Regresa False si ocurrio un error en el metodo 
productos = Productos()
sku = input("Ingresa un valor")
productos.buscarProducto(sku)
productos.buscarProducto2()