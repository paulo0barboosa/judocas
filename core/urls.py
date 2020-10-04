from django.urls import path
from django.conf.urls import url, include
from .views import (
    home,
    filiados_cadastrados,
    cadastra_filiado,
    professores_cadastrados,
    cadastra_professor,
    academias_cadastrados,
    cadastra_academia
)


urlpatterns = [
    url(r'^home/$', home, name='core_home'),
    url(r'^cadastra_filiado/$', cadastra_filiado, name='core_cadastra_filiado'),
    url(r'^filiados/$', filiados_cadastrados, name='core_filiados_cadastrados'),
    url(r'^cadastra_professor/$', cadastra_professor, name='core_cadastra_professor'),
    url(r'^professores/$', professores_cadastrados, name='core_professores_cadastrados'),
    url(r'^cadastra_academia/$', cadastra_academia, name='core_cadastra_academia'),
    url(r'^academias/$', academias_cadastrados, name='core_academias_cadastrados'),
    path('accounts/', include('django.contrib.auth.urls')),
]
