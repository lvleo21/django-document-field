# Django Document Field

**Django Document Field** é um campo customizado para o Django que permite armazenar e validar documentos brasileiros, como CPF e CNPJ. Ele inclui validação automática, formatação e suporte para exibição amigável dos valores.

## Recursos

- Validação de CPF e CNPJ com base nas regras oficiais.
- Formatação automática para exibição amigável.
- Integração simples com modelos Django.
- Mensagens de erro traduzíveis usando `gettext_lazy`.

## Instalação

Clone o repositório para o app `core` do seu projeto:
```bash
git clone https://github.com/seu-usuario/django-document-field.git
```

## Uso
Adicionando o campo ao modelo para usar o DocumentField, basta importá-lo e adicioná-lo ao seu modelo:

```python
from django.db import models
from document.field import DocumentField

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    documento = DocumentField()

    def __str__(self):
        return f"{self.nome} - {self.get_documento_display()}"
```

## Validação
O campo valida automaticamente os valores inseridos, garantindo que sejam CPFs ou CNPJs válidos. Caso o valor seja inválido, uma exceção ValidationError será levantada.

## Formatação
O método `get_<field_name>_display` é adicionado automaticamente ao modelo, permitindo exibir o documento formatado:

```python
pessoa = Pessoa.objects.get(id=1)
print(pessoa.get_documento_display())
# Output: "123.456.789-09" ou "12.345.678/0001-95"
```

## Estrutura do Projeto
- `document/constants.py`: Define constantes como o tamanho de CPF e CNPJ.
- `document/validators.py`: Contém as funções de validação para CPF e CNPJ.
- `document/utils.py`: Inclui utilitários como a formatação de documentos.
- `document/field.py`: Implementa o campo customizado DocumentField.


## Testes
Para garantir que o campo funcione corretamente, você pode criar testes unitários para validar CPFs e CNPJs:

```python
from django.core.exceptions import ValidationError
from document.validators import validate_document

# CPF válido
validate_document("123.456.789-09")

# CNPJ válido
validate_document("12.345.678/0001-95")

# Documento inválido
try:
    validate_document("123")
except ValidationError as e:
    print(e)  # Exibe mensagem de erro
```