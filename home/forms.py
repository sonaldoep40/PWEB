from django.forms import ModelForm
from .models import Produto

# Create the form class.
class ProdutoForm(ModelForm):
     class Meta:
         model = Produto
         fields = ['nome', 'preco']
