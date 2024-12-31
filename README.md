# API de Gestión de Productos y Pedidos

Este es un servicio de gestión de productos y pedidos desarrollado con **FastAPI**. La aplicación permite crear productos, consultar productos por ID, crear órdenes, listar órdenes, actualizar y eliminar órdenes. Los productos y las órdenes se almacenan en archivos JSON y se gestionan mediante estructuras de datos como el **Árbol Binario de Búsqueda (BST)** para los productos y **Lista Enlazada (Linked List)** para las órdenes.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn (para ejecutar el servidor)

## Instalación

1. Clona este repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:
   
   - En Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación:

   ```bash
   uvicorn "Estructuras de datos:app" --reload
   ```

   Esto iniciará el servidor en `http://127.0.0.1:8000`.

## Endpoints

### **1. Crear un producto**

- **Método**: `POST /api/product`
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

- **Método**: `GET /api/product/{id}`
- **Descripción**: Recupera la información de un producto usando su ID.
- **Respuesta**:
  ```json
  {
    "product name": "Patatas",
    "product price": 2.5
  }
  ```

### **3. Crear un pedido**

- **Método**: `POST /api/order`
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

- **Método**: `GET /api/order/{id}`
- **Descripción**: Recupera los detalles de un pedido por su ID, incluyendo los productos en el pedido.
- **Respuesta**:
  ```json
  [
    {
      "product name": "Patatas",
      "product price": 2.5,
      "quantity": 2,
      "total price": 5
    },
    {
      "product name": "Tomates",
      "product price": 3.0,
      "quantity": 1,
      "total price": 3
    }
  ]
  ```

### **5. Actualizar un pedido**

- **Método**: `PUT /api/order/{id}`
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

- **Método**: `DELETE /api/order/{id}`
- **Descripción**: Elimina un pedido existente por su ID.
- **Respuesta**:
  ```json
  {
    "message": "Order deleted!"
  }
  ```

### **7. Listar todos los pedidos**

- **Método**: `GET /api/orders`
- **Descripción**: Lista todos los pedidos con los productos y cantidades correspondientes.
- **Respuesta**:
  ```json
  [
    [
      {
        "product name": "Patatas",
        "product price": 2.5,
        "quantity": 2,
        "total price": 5
      },
      {
        "product name": "Tomates",
        "product price": 3.0,
        "quantity": 1,
        "total price": 3
      }
    ]
  ]
  ```

## Estructura del Proyecto

```
.
├── app.py                   # Archivo principal con las rutas de la API
├── requirements.txt         # Dependencias del proyecto
├── data/
│   ├── products.json        # Archivo JSON donde se almacenan los productos
│   └── orders.json          # Archivo JSON donde se almacenan los pedidos
└── structures/
    ├── linked_list.py       # Implementación de la lista enlazada
    ├── bst.py               # Implementación del árbol binario de búsqueda (BST)
```