from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Tratamiento)
class TratamientoTranslationOptions(TranslationOptions):
    fields = ('nombre', 'descripcion')


@register(Sistema)
class SistemaTranslationOptions(TranslationOptions):
    fields = ('nombresistema',)

@register(Patologia)
class SistemaTranslationOptions(TranslationOptions):
    fields = ('nombrepatologia',)



@register(EntradaBlog)
class EntradaBlogTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descripcion')

@register(Testimonio)
class TestimonioTranslationOptions(TranslationOptions):
    fields = ('nombre', 'descripcion')

@register(Inicio)
class InicioTranslationOptions(TranslationOptions):
    fields = ('tituloPrincipal', 'tituloCentro','textoCentro','textoPerfil')

@register(Contacto)
class ContactoTranslationOptions(TranslationOptions):
    fields = ('nombreCentro','direccion')

 

