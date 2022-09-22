# Módulos e Pacotes

## Módulos

Todo projeto de software inicia pequeno, seu código provavelmente é escrito em um único arquivo. Mas projetos crescem...

Conforme projetos crescem, se torna cada vez mais inconveniente encontrar algo em um único arquivo, além de gerar problemas de nomenclatura

Nesse momento pode ser uma boa ideia organizar o projeto, dividindo-o em vários arquivos, colocando classes relacionadas juntas.

- Como os arquivos são divididos depende das caraterísticas do projeto, mas geralmente é possível encontrar uma meneira natural de divisão.

- Por exemplo: caso seu projeto possua um backend com DB, uma camada de lógica de negócios, e uma interface gráfica de usuário, pode ser benéfico separar as três camadas.

<img src=".assets/div.jpg">

- **Módulos** são pedaços de código (modulares) que podem ser inseridos e chamados em qualquer algoritmo.

- Python provê métodos para gerar módulos a partir de todo código fonte.

- Para acessar código externo ao nosso arquivo atual, utilizaremos a palavra chave **import**

    - Já Fizemos isso com vários módulos built-in.

EX: Usando Abstract Factory como exemplo

```python
#factory.py
class AbstractFactory(ABC):
    @abstractmethod
    def getObject(self,type):
        pass

# Factory
class ObjectFactory(object):
    def getObject(self,type):
        if type == something:
            return ObjectClass1(arguments)
        elif type == something_else:
            return ObjectClass2(arguments)
        return None

```

- O **nome** do arquivo definirá o **namespace** do módulo, pelo qual importaremos e acessaremos seu conteúdo.
    - para importarmos factory.py
        **import** factory

    - para acessarmos o conteúdo de module1:
        factory.ObjectFactory()

- Como cada módulo tem seu namespace, não há problema em termos classes com nomes iguais em cada módulo. **Caso importemos o módulo por completo.**

- É possível também importar apenas membros específicos do nosso módulo usando o comando:
    - **from** x **import** y

- Do nosso exemplo com abstract.py
    - **from** abstract **import** ObjectFactory

- Caso vários deseje importar múltiplos membros, eles são separados por vírgulas(,)

- Os ***namespaces*** podem ser verbosos, então podemos ainda definir **apelidos** para módulos ou membros dos módulos que importamos

- Exemplo com ***factory.py***
    - **import** factory **as** F
    - **from** facoty **import** ObjectFactory **as** OF


## Pacotes

