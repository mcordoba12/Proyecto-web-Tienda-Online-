class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        # Obtiene el carro de la sesión, o lo inicializa como un diccionario vacío si no existe
        carro= self.session.get('carro')
        
        if not carro:
            carro = self.session['carro'] = {}
            
        self.carro = carro

            
    def agregar(self, producto): #metodo para agregar productos al carro
        
        if(str(producto.id) not in self.carro.keys()): #si el producto no esta en el carro
            self.carro[producto.id] = { #lo agregamos al carro
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else: #si el producto ya esta en el carro
            for key, value in self.carro.items(): #recorremos el carro
                if key == str(producto.id): #si el producto ya esta en el carro
                    value["cantidad"] = value["cantidad"] + 1 #aumentamos la cantidad del producto
                    value["precio"] = str(float(value["precio"]) + producto.precio) #aumentamos el precio del producto
                    break
        self.guardarCarro() #guardamos el carro en la sesion
    
    
    def guardarCarro(self):
        self.session["carro"] = self.carro #guardamos el carro en la sesion
        self.session.modified = True #indicamos que la sesion ha sido modificada
        
    def eliminar(self, producto):
        producto.id = str(producto.id) #convertimos el id del producto a string
        if producto.id in self.carro: #si el producto esta en el carro
            del self.carro[producto.id] #lo eliminamos
            self.guardarCarro()

    def restar_producto(self, producto): #metodo para restar productos al carro
        for key, value in self.carro.items(): #recorremos el carro
            if key == str(producto.id): #si el producto ya esta en el carro
                value["cantidad"] = value["cantidad"] - 1 #restamos la cantidad del producto
                value["precio"] = str(float(value["precio"]) - producto.precio)
                
                if value["cantidad"] < 1: #si la cantidad del producto es menor a 1
                    self.eliminar(producto) #eliminamos el producto del carro   
                    
                break
        self.guardarCarro()


    def limpiar_carro(self): #metodo para limpiar el carro
        self.session["carro"] = {} #limpiamos el carro
        self.session.modified = True #indicamos que la sesion ha sido modificada
