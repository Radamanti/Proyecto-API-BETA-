from datetime import datetime
from django.contrib.sessions.models import Session
import psycopg2
import csv

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ClientApp.models import Clients,Product,Bills,Bills_Products
from ClientApp.serializers import ClientsSerializer, BillsSerializer, ProductSerializer,Bills_ProductsSerializer, UserTokenSerializer

from django.core.files.storage import default_storage
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.authtoken.models import Token
from ClientApp import Templates

token = 0

def Index(request):
    return render(request,'Index.html')

class Login(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data=request.data,context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return JsonResponse({
                        'token':token.key,
                        'user': user_serializer.data,
                        'message':'Inicio de sesion exitoso.'
                    }, status = status.HTTP_201_CREATED)
                else:
                    all_sessions=Session.objects.filter(expire_date = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return JsonResponse({
                        'token':token.key,
                        'user': user_serializer.data,
                        'message':'Inicio de sesion exitoso.'
                    }, status = status.HTTP_201_CREATED)
            else:
                return JsonResponse({'Error': 'Este usuario no puede iniciar sesion.'}, status = status-HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({'error': 'Nombre de uusario o contraseña incorrecta'}, status = status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'mensaje':'Hola desde response'}, status = status.HTTP_200_OK)


@csrf_exempt
def clientAPI(request, id = 0):
    if request.method =='GET':
        client = Clients.objects.all()
        clients_serializer=ClientsSerializer(client,many=True)
        return JsonResponse(clients_serializer.data, safe=False)
    elif request.method =='POST':
        client_data = JSONParser().parse(request)
        clients_serializer=ClientsSerializer(data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("Añadido correctamente",safe=False)
        return JsonResponse("Error al añadir", safe=False)
    elif request.method == 'PUT':
        client_data=JSONParser().parse(request)
        client=Clients.objects.get(idClient=client_data['idClient'])
        clients_serializer=ClientsSerializer(client, data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("Modificado correctamente", safe=False)
        return JsonResponse("Error al modificar", safe=False)
    elif request.method == 'DELETE':
        client=Clients.objects.get(idClient=id)
        client.delete()
        return JsonResponse("Eliminado correctamente",safe=False)

@csrf_exempt
def billsAPI(request, id = 0):
    if request.method =='GET':
        bill = Bills.objects.all()
        bills_serializer=BillsSerializer(bill,many=True)
        return JsonResponse(bills_serializer.data, safe=False)
    elif request.method =='POST':
        bills_data = JSONParser().parse(request)
        bills_serializer=BillsSerializer(data=bills_data)
        if bills_serializer.is_valid():
            bills_serializer.save()
            return JsonResponse("Añadido correctamente",safe=False)
        return JsonResponse("Error al añadir", safe=False)
    elif request.method == 'PUT':
        bills_data=JSONParser().parse(request)
        bill=Bills.objects.get(idBill=bills_data['idBill'])
        bills_serializer=BillsSerializer(bill, data=bills_data)
        if bills_serializer.is_valid():
            bills_serializer.save()
            return JsonResponse("Modificado correctamente", safe=False)
        return JsonResponse("Error al modificar", safe=False)
    elif request.method == 'DELETE':
        bill=Bills.objects.get(idBill=id)
        bill.delete()
        return JsonResponse("Eliminado correctamente",safe=False)

@csrf_exempt
def productsAPI(request, id = 0):
    if request.method =='GET':
        product = Product.objects.all()
        products_serializer=ProductSerializer(product,many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method =='POST':
        product_data = JSONParser().parse(request)
        products_serializer=ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Añadido correctamente",safe=False)
        return JsonResponse("Error al añadir", safe=False)
    elif request.method == 'PUT':
        product_data=JSONParser().parse(request)
        product=Product.objects.get(idProduct=product_data['idProduct'])
        products_serializer=ProductSerializer(product, data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Modificado correctamente", safe=False)
        return JsonResponse("Error al modificar", safe=False)
    elif request.method == 'DELETE':
        product=Product.objects.get(idProduct=id)
        product.delete()
        return JsonResponse("Eliminado correctamente",safe=False)

@csrf_exempt
def Bills_ProductsAPI(request, id = 0):
    if request.method =='GET':
        bills_Product = Bills_Products.objects.all()
        bills_Product_serializer=Bills_ProductsSerializer(bills_Product,many=True)
        return JsonResponse(bills_Product_serializer.data, safe=False)
    elif request.method =='POST':
        bills_Product_data = JSONParser().parse(request)
        bills_Product_serializer=Bills_ProductsSerializer(data=bills_Product_data)
        if bills_Product_serializer.is_valid():
            bills_Product_serializer.save()
            return JsonResponse("Añadido correctamente",safe=False)
        return JsonResponse("Error al añadir", safe=False)
    elif request.method == 'PUT':
        bills_Product_data=JSONParser().parse(request)
        bills_Product=Bills_Products.objects.get(idBills_Products=bills_Product_data['idBills_Products'])
        bills_Product_serializer=Bills_ProductsSerializer(bills_Product, data=bills_Product_data)
        if bills_Product_serializer.is_valid():
            bills_Product_serializer.save()
            return JsonResponse("Modificado correctamente", safe=False)
        return JsonResponse("Error al modificar", safe=False)
    elif request.method == 'DELETE':
        bills_Product=Bills_Products.objects.get(idBills_Products=id)
        bills_Product.delete()
        return JsonResponse("Eliminado correctamente",safe=False)

@csrf_exempt
def LoadFile(request):
    EXTENSION = ".csv"
    file=request.FILES['file']
    if EXTENSION in file.name:
        file_name = default_storage.save(file.name, file)
        conexion = psycopg2.connect(user='postgres', password= 'admin', host = '127.0.0.1', port = '5432', database = 'ApiDjango')
        cursor = conexion.cursor()
        file = open("E:/API Django/API/Archivos/"+file_name)
        reader = csv.reader(file)
        try:
            with conexion:
                for row in reader:
                    if 'NOMBRE' in row[0] or 'nombre' in row[0]:
                        pass
                    else:
                        datos = row[0]
                        nombre, apellido, documento, email = datos.split(';')
                        if nombre == "" and documento == "" and apellido =="" and email =="":
                            break
                        else:
                            sentenciaIngreso = 'INSERT INTO public."ClientApp_clients" ("firstNameClient", "lastNameClient", "documentClient", "emailClient") VALUES (%s, %s, %s, %s)'
                            valores = (nombre, apellido, documento,email)
                            cursor.execute(sentenciaIngreso, valores)
            return JsonResponse("Se ha insertado todos los campos del archivo "+file_name, safe=False)
        except Exception as e:
            JsonResponse(f'Ocurrió un error: {e}')
        finally:
            conexion.close
    else:
        return JsonResponse("El archivo adjuntado no es válido, recuerda que debe ser un archivo con extesión CSV.", safe=False)

@csrf_exempt
def SaveFile(request):
    if request.method =='GET':
        file=request.FILES['file']
        file_name = default_storage.save(file.name, file)
        ARCHIVO = "C:/Detalle.csv"
        id = print(f'''Ingresa el id de la persona de la cual desea saber el
        nombre completo, documento y cantidad de facturas, recuerda que puedes ver la lista
        ingresando al API y haciendo solicitud Get en el URL "client": 
        ''')
        conexion = psycopg2.connect(user='postgres', password= 'admin', host = '127.0.0.1', port = '5432', database = 'ApiDjango')
        cursor = conexion.cursor()
        try:
            with conexion:
                valores = id
                sentenciaUsuarios = 'SELECT * FROM public."ClientApp_clients" WHERE "ClientApp_clients"."idClient" = %s'
                cursor.execute(sentenciaUsuarios, valores)
                registrosUsuarios = cursor.fetchone()
                nombre = registrosUsuarios[1] + " " + registrosUsuarios[2]
                documento = str(registrosUsuarios[3])
                sentenciaUsuarios = 'SELECT Count(*) FROM public."ClientApp_bills" WHERE "clienteId_id" = %s'
                cursor.execute(sentenciaUsuarios, valores)
                registrosUsuarios = cursor.fetchone()
                facturas = str(registrosUsuarios[0])
                with open(ARCHIVO, 'w') as file:
                    columnas=['NAME', 'DOCUMENT', 'BILLS']
                    writer = csv.DictWriter(file, fieldnames=columnas)
                    writer.writeheader()
                    write.writerow({'NAME': nombre,
                    'DOCUMENT': documento,
                    'BILLS': facturas
                    })
        except Exception as e:
            JsonResponse(f'Ocurrió un error: {e}')
        finally:
            return JsonResponse('Datos descargados')
            conexion.close