from decimal import Decimal
from django.conf import settings
from comida.models import Comida, Categoria
from usuarios.models import Orden, direccion, cantidadComidaOrden


class Cart(object):
    """
    Clase Cart que manejara el carrito
    """
    def __init__(self, request):
        """
        Inicializamos el carrito.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
        # guarda un carrito vacio en la sesion 
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, comida, quantity=1, update_quantity=False):
        """
        Agregar un prodcuto al carrito o actualizar la cantidad del mismo
        """
        product_id = str(comida.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'precio': str(comida.precio)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Guarda el carrito en la sesión actual
        """
        # marca la sesion actual como "modified" para asegurar que sea guardada
        self.session.modified = True  

    def remove(self):
        """
        Remueve un alimento del carrito
        """
        product_id = str(comida.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Itera sobre los alimentos añadidos al carrito y los obtiene
        de la base de datos
        """
        product_ids = self.cart.keys()
        # obtiene los objetos comida y los agrega al carrito
        products = cantidadComidaOrden.object.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(comida.id)]['prodcut'] = product           

        for item in cart.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['quantity']
            yield item  


    def __len__(self):
        """
        Cuanta los elementos en el carrito
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Calcula el precio total de todos los elementos del carrito
        """
        return sum(Decimal(item['precio']) * item['quantity'] for item in self.cart.values())   

    def clear(self):
        """
        Limpia la sesion del carrito actual
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()     