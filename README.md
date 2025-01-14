# API de Gestión de Productos y Pedidos

Esta aplicación es un servicio de gestión de productos y pedidos desarrollado con **FastAPI**. Permite crear productos, consultar productos por ID, crear órdenes, listar órdenes, actualizar y eliminar órdenes. Los productos y las órdenes se almacenan en archivos JSON y se gestionan mediante estructuras de datos como el **Árbol Binario de Búsqueda (BST)** para los productos y **Lista Enlazada (Linked List)** para las órdenes.

## Características

### Productos:
- **Crear un producto**: Permite añadir un nuevo producto a la base de datos.
- **Consultar un producto por ID**: Recupera la información de un producto específico usando su ID.

### Pedidos:
- **Crear un pedido**: Permite registrar un nuevo pedido con los productos seleccionados y sus cantidades.
- **Consultar un pedido por ID**: Recupera los detalles de un pedido, incluyendo los productos, cantidades y precios.
- **Actualizar un pedido**: Modifica un pedido existente actualizando los productos o sus cantidades.
- **Eliminar un pedido**: Elimina un pedido específico de la base de datos.
- **Listar todos los pedidos**: Obtiene una lista de todos los pedidos realizados, con los detalles de productos y cantidades correspondientes.


## Configuración

### Requisitos previos

- Python 3.7+
- FastAPI
- Uvicorn (para ejecutar el servidor)

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/DanielCaldes/Estructuras-de-datos-para-desarrollo-web.git
   cd Estructuras-de-datos-para-desarrollo-web
   cd app
   ```

2. Crea y activa el entorno virtual (ejemplo con conda):

   ```bash
   conda create --name nombre_del_entorno python=3.x
   conda activate nombre_del_entorno
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. Inicia el servidor de FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

2. Accede a la documentación interactiva de la API en Swagger:
   http://127.0.0.1:8000/docs

## Endpoints

### **1. Crear un producto**

- **Método**: POST
  ```url
  /api/products/
  ```
- **Descripción**: Crea un nuevo producto y lo agrega a la base de datos.
- **Cuerpo de la solicitud** (JSON):
  ```json
  {
    "product_name": "Patatas",
    "price": 2.5
  }
  ```
- **Respuesta**:
  ```json
  {
    "message": "Product created with id: 1"
  }
  ```

### **2. Consultar un producto por ID**

- **Método**: GET
   ```url
   /api/products/{id}
   ```
- **Descripción**: Recupera la información de un producto usando su ID.
- **Respuesta**:
  ```json
  {
    "product name": "Patatas",
    "product price": 2.5
  }
  ```

### **3. Crear un pedido**

- **Método**: POST
  ```url
  /api/orders/
  ```
- **Descripción**: Crea un nuevo pedido con los productos seleccionados y sus cantidades.
- **Cuerpo de la solicitud** (JSON):
  ```json
  {
    "products": {
      "1": 2,
      "2": 1
    }
  }
  ```
- **Respuesta**:
  ```json
  {
    "message": "Order created with id: 1"
  }
  ```

### **4. Consultar un pedido por ID**

- **Método**: GET
  ```url
  /api/orders/{id}
  ```
- **Descripción**: Recupera los detalles de un pedido por su ID, incluyendo los productos en el pedido.
- **Respuesta**:
  ```json
  {
     "products": [
       {
         "product_name": "Patatas",
         "product_price": 2,
         "quantity": 2,
         "total_price": 4
       },
       {
         "product_name": "Tableta de chocolate",
         "product_price": 1.5,
         "quantity": 1,
         "total_price": 1.5
       }
     ],
     "total_price": 5.5
   }
  ```

### **5. Actualizar un pedido**

- **Método**: PUT
  ```url
  /api/orders/{id}
  ```
- **Descripción**: Actualiza un pedido existente con nuevos productos o cantidades.
- **Cuerpo de la solicitud** (JSON):
  ```json
  {
    "products": {
      "1": 3,
      "3": 2
    }
  }
  ```
- **Respuesta**:
  ```json
  {
    "message": "Order updated!"
  }
  ```

### **6. Eliminar un pedido**

- **Método**: DELETE
   ```url
   /api/orders/{id}
   ```
- **Descripción**: Elimina un pedido existente por su ID.
- **Respuesta**:
  ```json
  {
    "message": "Order deleted!"
  }
  ```

### **7. Listar todos los pedidos**

- **Método**: GET
  ```url
  /api/orders/
  ```
- **Descripción**: Lista todos los pedidos con los productos y cantidades correspondientes.
- **Respuesta**:
  ```json
  {
     "order_1": {
       "products": [
         {
           "product_name": "Patatas",
           "product_price": 2,
           "quantity": 2,
           "total_price": 4
         },
         {
           "product_name": "Tableta de chocolate",
           "product_price": 1.5,
           "quantity": 1,
           "total_price": 1.5
         }
       ],
       "total_price": 5.5
     },
     "order_3": {
       "products": [
         {
           "product_name": "Patatas",
           "product_price": 2,
           "quantity": 2,
           "total_price": 4
         },
         {
           "product_name": "Salchichas",
           "product_price": 1,
           "quantity": 2,
           "total_price": 2
         }
       ],
       "total_price": 6
     }
   }
  ```

## Estructura del Proyecto

```
.                            # Carpeta app
├── main.py                  # Archivo principal con las rutas de la API
├── requirements.txt         # Dependencias del proyecto
├── data/
│   ├── products.json        # Archivo JSON donde se almacenan los productos
│   └── orders.json          # Archivo JSON donde se almacenan los pedidos
└── structures/
    ├── linked_list.py       # Implementación de la lista enlazada
    ├── bst.py               # Implementación del árbol binario de búsqueda (BST)
```
