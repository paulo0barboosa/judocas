from django.urls import path
from django.conf.urls import url, include
from .views import (
    home,
    filiados_cadastrados,
    cadastra_filiado
)


urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^filiados/$', filiados_cadastrados, name='core_filiados_cadastrados'),
    url(r'^cadastra_filiado/$', cadastra_filiado, name='core_cadastra_filiado'),
]
