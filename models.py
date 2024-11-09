import uuid
from pydantic import BaseModel, Field

class UpsertNew(BaseModel):
    """
    Modelo de datos para representar una noticia.
    Proporciona los campos obligatorios y su estructura para la validación.
    """
    id: str = Field(default_factory=uuid.uuid4, alias="_id")  # ID único de la noticia
    sitio: str  # Sitio web de origen de la noticia
    link: str  # Enlace de la noticia
    fecha: str  # Fecha de la noticia
    titulo: str  # Título de la noticia
    bajada: str  # Bajada de la noticia
    cuerpo: str  # Contenido de la noticia
    foto: str  # URL de la foto de la noticia
    tags: str  # Etiquetas de la noticia
    fecha_extraccion: str # Fecha de extracción de la noticia
    seccion: str  # Sección de la noticia


    class Config:
        populate_by_name = True   # Permite acceder a los campos usando sus nombres originales
        json_schema_extra = {
            "example": {
                "_id": "20240421",
                "sitio": "latercera com",
                "link": "www.latercera.com la-tercera-domingo noticia hegemonia-a-sangre-y-fuego-la-caida-de-los-trinitarios-la-banda-que-domino-la-toma-mas-grande-de-santiago OREVKTXEFBGHRKRFSGX36DPR5M",
                "fecha": "2024-04-21T04:00:00.000+00:00",
                "titulo": "Hegemonía a sangre y fuego: la caída de “Los Trinitarios”, la banda que dominó la toma más grande de Santiago",
                "bajada": "Una banda narco de dominicanos logró dominar, en dos años, una toma donde viven tres mil familias. No solo eso: lograron desplazar una temida banda narco chilena e incluso subyugar al Tren de Aragua. Les indagan 15 homicidios. Los investigadores tratan de explicar su éxito: dicen que la clave está en su disciplina, rudeza y actitud temeraria. “Para ellos, el valor de la vida parecía no tener ningún sentido”, dice un fiscal.",
                "cuerpo": "Esa madrugada del 19 de ",
                "foto": "https://www.latercera.com/resizer/CpgViZVh4FlsmgpIEsJaRN8dsSk=/900x600/smart/cloudfront-us-east-1.images.arcpublishing.com/copesa/GLR7GNK6DZDAXLZK3QT4QHPFU4.jpg",
                "tags": "LT Domingo",
                "fecha_extraccion": "2024-04-22T19:38:51.637+00:00",
                "seccion": "otro"
            }
        }

class Response(BaseModel):
    detail: str

    class Config:
        orm_mode = True  # Permite la compatibilidad con objetos ORM si estás usando uno