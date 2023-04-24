from django.db import models
from django.contrib.auth.models import User
from standard.models import AuditTimestampModel


class PMCareerMoreStructure(AuditTimestampModel, models.Model):
   
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, related_name='%(class)s_updated_by', on_delete=models.PROTECT)
    documento = models.FileField(upload_to='documentos')


    
    class Meta:
        verbose_name = 'Carreira e Estrutura'
        verbose_name_plural = 'Carreiras e Estruturas'
    
    def __str__(self):
        return (f"PMCareerandStructure(id={self.id}, created_by={self.created_by}, updated_by={self.updated_by})")
    

    def get_created_by(self):
        return self.created_by
    
    
    def get_updated_by(self):
    
        return self.updated_by
    
    def get_documento_url(self):

        if self.documento:
            return self.documento.url
    
    def download_documento(self):

        pass
    
    def visualizar_documento(self):

        pass
       

    def test(self):
        print("Sinstese de teste qualquer")
        pass

    def get_valor_estagio_pos_graduacao(self):
        return self.valor_estagio_pos_graduacao

    def get_valor_auxilio_transporte(self):
        return self.valor_auxilio_transporte

    def get_outros_pagamentos(self):
        return self.outros_pagamentos
