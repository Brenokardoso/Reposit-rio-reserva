from django.db import models
from standard.models import AuditTimestampModel




class Author(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return(self.name)


class Category(models.Model):
    title = models.CharField(max_length=200)



class Book(models.Model):
    autor = models.ForeignKey(Author,related_name="books",on_delete=models.PROTECT)
    categoria = models.ForeignKey(Category,related_name="books",on_delete=models.SET_NULL,null = True,blank=True)
    tittle = models.CharField(max_length=200)
    publication_year = models.SmallIntegerField(null = True,blank = True)#
    #control_number = models.SmallIntegerField(blanck = True) \/\/ #Não usar o blanck,O usuário não irá preencher esse campo,porem o BD n aceita null

class BookLead(models.Model):
    employer = models.ForeignKey('rh.Servidor',related_name = 'library_leads',on_delete=models.PROTECT )
    book = models.ForeignKey(Book,related_name='leads',on_delete=models.PROTECT)
    lead_date = models.DateField(auto_now=True)
    lead_return = models.DateField(null=True,blank=True)
    lead_days = models.SmallIntegerField()
    lead_by = models.ForeignKey('auth.User',related_name='+',on_delete=models.PROTECT)
    returned_by = models.ForeignKey('auth.User',related_name='+',on_delete=models.PROTECT,null=True,blank=True)



class BookEvents(models.Model):
    book = models.ForeignKey(Book,related_name='events',on_delete=models.PROTECT)
    lead = models.ForeignKey(BookLead,related_name='events',on_delete=models.PROTECT,null=True ,blank=True)
    by = models.ForeignKey('auth.User',related_name= "+",on_delete=models.PROTECT,blank=True)#A aplicação não vai cobrar no formulário,ela memsmo vai preencher/ A validação do formulário
    at = models.DateField(auto_now_add=True,blank=True)
    event = models.SmallIntegerField(
        choices=(
        (1,'Cadastro'),
        (2,'Atalização de cadastro'),
        (3,'Emprestimo'),
        (4,'Devolução'),
        (5,'renovação'),
        (6,'Avaria'),
        (7,'Perda')
        )
    )

description = models.TextField( )



class CarreiraEstrutura(AuditTimestampModel):
    documento = models.FileField(upload_to='documentos')

    class Meta:
        verbose_name = 'Carreira e Estrutura'
        verbose_name_plural = 'Carreiras e Estruturas'
    
    def __str__(self):
        return f"CarreiraEstrutura(id={self.id}, created_by={self.created_by}, updated_by={self.updated_by})"


    @classmethod
    def get_created_by(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        return obj.created_by
    
    @classmethod
    def get_updated_by(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        return obj.updated_by
    
    @classmethod
    def get_documento_url(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        if obj.documento:
            return obj.documento.url
    
    @classmethod
    def download_documento(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        # Adicionar código para download do documento
    
    @classmethod
    def visualizar_documento(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        # Adicionar código para visualização do documento
       
    @classmethod
    def test(cls):
        print("Síntese de teste qualquer")
        # Adicionar código para realizar testes
    
    @classmethod
    def get_valor_estagio_pos_graduacao(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        return obj.valor_estagio_pos_graduacao
    
    @classmethod
    def get_valor_estagio_pos_graduacao(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        return obj.valor_estagio_pos_graduacao
    
    @classmethod
    def get_valor_auxilio_transporte(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        return obj.valor_auxilio_transporte
    
    @classmethod
    def get_outros_pagamentos(cls, obj_id):
        obj = cls.objects.get(id=obj_id)
        return obj.outros_pagamentos





#./manage.py restfactory -m library.Author -p BRN --with-manager -d library -n library.author --overwrite --with-package