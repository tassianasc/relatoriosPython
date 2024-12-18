## Testes Automatizados em Python
### Descrição do Projeto
Este projeto foi desenvolvido como parte de um trabalho de graduação para demonstrar a identificação e correção de bugs em métodos Python, além da criação de testes automatizados para validar essas correções.

### Três classes foram analisadas:

**FibonacciGenerator** (manipulação da sequência de Fibonacci),
**StringUtils** (manipulação de strings),
**UserManager** (gerenciamento de usuários).

O objetivo principal foi garantir que os métodos dessas classes funcionem corretamente após a correção e sejam testados adequadamente.
---
## Tecnologias Utilizadas
### Python 3.8+
### Biblioteca de Testes:
### unittest (nativo do Python)
### pytest (opcional, para rodar os testes de forma simplificada)
---
## Como Executar o Projeto
### 1. Pré-requisitos
Certifique-se de ter o Python instalado:
```
python --version
```

### 3. Executando os Testes
Usando unittest:
Navegue até o diretório do projeto no terminal.
Execute os testes individualmente:

```
python -m unittest test_fibonacci_generator.py
python -m unittest test_string_utils.py
python -m unittest test_user_manager.py

```
Ou rode todos os testes de uma vez:
```
python -m unittest discover

```
Usando pytest (opcional):
Instale o pytest:

```
pip install pytest
```
Execute todos os testes com:
```
pytest
```
