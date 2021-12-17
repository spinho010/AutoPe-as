from django.urls import path

from projeto.core import views as v
from .views import TempAtividade, TempAtividadeCon, TempAtividadePen, CreateConclu, AtividadeDelete, CreatePende, CreateComprovante, ListComprovante

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('atividades/', TempAtividade.as_view(), name='ativv'),
    path('atividades/pendentes', TempAtividadePen.as_view(), name='ativvp'),
    path('atividades/concluidas', TempAtividadeCon.as_view(), name='ativvc'),
    path('create_attc/', CreateConclu.as_view(), name='create-concluida'),
    path('atividades/pendentes/<int:pk>/', AtividadeDelete.as_view(), name='delete-atividade'),
    path('create_attp/', CreatePende.as_view(), name='att-atividade-pendente'),
    path('comprovante-interno/', CreateComprovante.as_view(), name='create_comprovante'),
    path('list-comprovante/', ListComprovante.as_view(), name='list_comprovante'),
]