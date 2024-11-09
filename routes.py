from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models import UpsertNew, Response
import datetime
from pymongo.errors import PyMongoError

router = APIRouter() # Crear el enrutador para gestionar las rutas

@router.post("/upsertNew", response_description="Insertar o actualizar noticia", status_code=status.HTTP_201_CREATED)
def upsert_new(request: Request, noticia: UpsertNew = Body(...)):
    """
    Inserta o actualiza una noticia en la base de datos.
    Si la noticia ya existe, actualiza el contenido; de lo contrario, la crea.
    """
    try:
        # Convertir el modelo de noticia a un formato JSON serializable
        noticia = jsonable_encoder(noticia)

        # Seleccionar la colección "noticias" de la base de datos
        collection = request.app.database["noticias"]

        # Buscar el documento por ID. Si no existe, se crea uno nuevo
        doc_ref = collection.find_one({"_id": noticia["_id"]})
        if doc_ref is None:
            collection.insert_one({"_id": noticia["_id"]})
            doc_ref = collection.find_one({"_id": noticia["_id"]})

        # Verificar y crear la estructura anidada para el sitio de noticias
        if noticia["sitio"].replace(".", " ") not in doc_ref:
            doc_ref[noticia["sitio"].replace(".", " ")] = {}

        # Crear la subestructura para el enlace si no existe
        if noticia['link'].replace("/", " ") not in doc_ref[noticia["sitio"].replace(".", " ")]:
            doc_ref[noticia["sitio"].replace(".", " ")][noticia['link'].replace("/", " ")] = {}
            response_detail = "Noticia insertada exitosamente"
        else:
            response_detail = "Noticia actualizada exitosamente"

        # Definir el objeto de la noticia para almacenar en la base de datos
        post = {
            u'fecha': datetime.datetime.strptime(noticia['fecha'],"%Y-%m-%dT%H:%M:%S.%f%z"),
            u'titulo': noticia['titulo'],
            u'bajada': noticia['bajada'],
            u'cuerpo': noticia['cuerpo'],
            u'foto': noticia['foto'],
            u'tags': noticia['tags'],
            u'link': noticia['link'],
            u'fecha_extraccion': datetime.datetime.strptime(noticia['fecha_extraccion'],"%Y-%m-%dT%H:%M:%S.%f%z"),
            u'seccion': noticia['seccion']
        }

        # Actualizar la estructura anidada del documento en la colección
        doc_ref[noticia["sitio"].replace(".", " ")][noticia['link'].replace("/", " ")] = post.copy()
        collection.update_one({"_id": noticia["_id"]}, {"$set": doc_ref})

        # Retornar mensaje de éxito
        return Response(detail=response_detail)
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error de datos: {str(e)}")