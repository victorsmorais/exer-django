from django.db import models
from ordered_model.models import OrderedModel
from django.utils.translation import gettext_lazy as _


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=32)
    publico = models.TextField(null=True)
    descricao = models.TextField(null=True)
    order = models.PositiveIntegerField(_("order"), editable=False, db_index=True, null=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo
