from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class': 'form-control'})
            self.fields[fields].widget.attrs.update({'placeholder': fields})

        choices = list()
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display()))
            #print(categoria.get_titulo_display()) 
        self.fields['categoria_manutencao'].choices = choices
            
            
            
            
            
            
            
            
            
            
            
            #print(fields)
                # titulo
                # cliente
                # categoria_manutencao
                # data_inicio
                # data_entrega
        
        
        
        
        #self.fields['titulo'].widget.attrs.update({'class': 'form-control'})
        #self.fields['data_inicio'].widget.attrs.update({'class': 'form-control'})