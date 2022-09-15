# MVC

**Model View Controller** (MVC) é um padrão de projeto que define que uma aplicação possui: modelo de dados, informação de apresentação, e informação de controle.

## MVC

- MVC é um padrão arquitetural, mas não define uma aplicação completa.

- MVC se relaciona, principalmente, as camadas de interação/UI. Portanto, ainda pode ser necessária criação de camadas de negócio, serviço ou acesso de dados, por exemplo.

<img src=".assets/mvc.jpg">

## Model

- O **Modelo** contém apenas dados puros da aplicação. É o componente central do padrão de projeto.

- Não contém lógica em como apresentar os dados ao usuário.

- Gerencia diretamente os dados, regras e lógica da aplicação


<img src=".assets/model.jpg">

### Model

```python

class Estudante:
    def __init__(self,nome:str,matricula:int):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def nome(self,matricula):
        self._matricula = matricula

```

## Visualização

- A **Visualização** define a representação dos dados para o usuário em qualquer maneira (tabelas, diagramas, gráficos).

- É possível que várias **Visualizações** existam para um único **Modelo**.

<img src=".assets/view.jpg">

## View

```python

class EstudanteView:
    def mostrarEstudante(self,nome:str,matricula:int):
        print("Estudante:")
        print(f"Nome:{nome}")
        print(f"Matrícula:{matricula}")

```

## Controlador

- O **Controlador** gerencia a comunicação entre **Modelo** e **Visualização**

- Aceita entradas do usuário escutando **eventos** ativados pelas **Visualizações** e reage apropriadamente

- Comumente a reação envolve a chamada de métodos dos modelos.

<img src=".assets/controler.jpg">

## Controler

```python

class Estud