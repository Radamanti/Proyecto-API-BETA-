# Proyecto-API-BETA-
Buen día a todos.

De primera mano, muchas gracias por leer y brindar de su tiempo para poder calificar de alguna manera el esfuerzo dado por mi en este proyecto.

Lo considero bastante útil, dado que es la base de un proyecto que tiene bastante potencial en el manejo de datos y desarrollo web backend. Tener en cuenta, que todas las pruebas realizadas, se generaron a través de un tester de API's como lo es Postman y se de nota como la conexión a PostgreSQL es bastante efectiva al igual que el manejo de información.

Para empezar, tenemos alrededor de 11 urls, cuyas actúan con respecto a diferentes vistas y tienen variantes según sea la petición que se les haga, se explicará a grozo modo el funcionamiento del proyecto:

Los path´s client, bill, product y bill_product, nos brindan la posibilidad de ingresar o acceder al CRUD de cada relación y/o tabla, en donde se tendrá la interfaz de Postman y la sintaxis es bastante intuitiva, se tendrá algo como:
  ![imagen](https://user-images.githubusercontent.com/92836663/147016434-2d56abf0-9227-4806-b620-bd786c50fb9d.png)
En donde se verá que el método GET, es quien nos permite el obtener toda la información conforme a esa tabla, relación o modelo. En segundo caso, el método de solicitud POST, será quien nos ayude a ingresar información a nuestra tabla, solo es necesario el ingresar de la siguiente manera a través de Body > raw:
  ![imagen](https://user-images.githubusercontent.com/92836663/147016611-321bff99-9539-464a-b199-5296927922bd.png)
Donde se podrá el modificar los valores allí a excepción del ID en todas las tablas, dado que es PK, del resto, podrá ser cambiado y al enviar la solicitud, la API la recibirá y agregará la información a la BD, quien está compuesta por las siguientes tablas:
  ![imagen](https://user-images.githubusercontent.com/92836663/147016676-13b37be1-8f04-47ce-97f7-140a44268180.png)
  
En tercer término, tenemos el método PUT, el cual nos ayudará a modificar las valores de la base de datos, en donde el punto de referencia, será el ID del cliente, factura o producto que se desee alterar.

Por último, tenemos el método DELETE, que al igual que el método PUT, usa el ID para poder eliminar algún elemento de la lista, en este caso, el ID, es colocado luego de la URL principal, agregando "/" + el número del ID que se desea eliminar de esa tabla.

El inicio de sesión, se puede realizar a travéz del método POST y el URL + /login, en donde se pedirán credenciales y será posible el ingresar con los datos del usuario brindados en el inicio (HTML básico) del proyecto.

![imagen](https://user-images.githubusercontent.com/92836663/147017011-23d7f577-4ced-454d-bee6-356fa697becf.png)

Como se ve en la imagen, se hará la petición, brindando el valor de cada variable para que sean acogidas por la API REST.

Por otro lado, queda resaltar, que cada inicio de sesión está controlado por un token, el cual solo dispone de una sesión posible abierta en cualquier parte, en caso contrario, si se abriese una segunda, la primera cerrará y esta segunda tendrá un token distinto al primero, de esta manera se proteje cada ingreso del usuario y de igual manera las URL's visitadas, acompañado de un csrftoken, que nos brinda más seguridad en la navegación y será único por cada path, se podrá ver de esta manera en caso posible:

![imagen](https://user-images.githubusercontent.com/92836663/147017180-cc8cb31b-bd13-4b43-9e73-40b7429f03f8.png)


Por otro lado, la API tiene dos funcionalidades más, en donde se guardan y se leen archivos, respectivamente en el archivo views.py, se tendrán dos funciones de Loadfile y SaveFile, los cuales, este primero, nos ayuda a acoger un archivo y poderlo leer en un archivo CSV, donde obtendrá cada información de este para subir datos de clientes a la tabla, en el repositorio, estará un archivo llamado "archivo.csv", el cual fue usado con éxito para estas pruebas y la segunda función, nos ayudará a generar un archivo del nombre de la persona que se desea, con el documento respectivo y la cantidad de facturas que este tiene asociadas.

De igual manera, se generó un backend sencillo con C# de adicional, en donde se brinda una perspectiva mejor de lo que sería el futuro de la API con ideas basadas en ideas similares gracias a la comunicación entre lenguajes.

Desde ya, muchas gracias por leer toda la documentación y espero poder ser seleccionado para mejorar y brindar buenos resultados.
