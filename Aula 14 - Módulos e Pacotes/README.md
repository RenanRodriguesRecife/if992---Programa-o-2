# Módulos e Pacotes

## Módulos

Todo projeto de software inicia pequeno, seu código provavelmente é escrito em um único arquivo. Mas projetos crescem...

Conforme projetos crescem, se torna cada vez mais inconveniente encontrar algo em um único arquivo, além de gerar problemas de nomenclatura

Nesse momento pode ser uma boa ideia organizar o projeto, dividindo-o em vários arquivos, colocando classes relacionadas juntas.

- Como os arquivos são divididos depende das caraterísticas do projeto, mas geralmente é possível encontrar uma meneira natural de divisão.

- Por exemplo: caso seu projeto possua um backend com DB, uma camada de lógica de negócios, e uma interface gráfica de usuário, pode ser benéfico separar as três camadas.

<img src="./.assets/div.jpg">

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

Tal como podemos organizar classes e função em um módulo, também podemos organizar módulos em uma **estrutura de arquivos**

Há apenas dois requisitos para transformar nossos módulos em um pacote (ou vários pacotes).
    
    - Um diretório onde nossos módulos existam.

    - Um arquivo chamado __init__.py no diretório


O nome do diretório se torna o ***namespace*** do nosso pacote e a partir dele conseguimos acessar os módulos.

>> package
    >> __init__.py
    >> module1.py
    >> module2.py

Agora podemos acessar **module1** e **module2** usando:

**from** package **import** module1, module2


>> package
    >> __init__.py
    >> module1.py
    >> module2.py


É possível também aninhar pacotes. Acessamos **subpack** por meio de:

**from** package.subpack **import** module2

>> package
    >> __init__.py
    >> module1.py
    >> subpack
        >> __init__.py
        >> module2.py

O arquivo __init__.py é interpretado por Python de maneira a criar o namespace e permitir acesso aos conteúdos internos do diretório.

Apesar disso, é importante entender que o arquivo __init__.py é um script python como qualquer outro, e podemos utilizá-lo para configurações, proteção de visibilidade ou facilidade de acesso.

Um exemplo comum é importar o módulos dentro do próprio __init__.py, permitindo acessá-los por meio do ***namespace*** do pacote:


```python
#__init__.p
from.import module1
#main.py
import package
package.module1

>> package
    >> __init__.py
    >> module1.py
```

>> package
    >>__init__.py
    >> module1.py

# Docstring

Documentação de código é comumente vista como um pensamento secundário.

Conforme escrevemos nosso código, os métodos e classes podem parecer óbvios. Mas provavelmente pensaríamos diferente se forçados a entender o código de outra pessoa.

Nós sabemos utilizar comentários (#) para explicar brevemente a intenção de determinado bloco de código.

    - Comentários podem não servir para explicações longas.

    - Para isso temos **docstrings**.

Docstrings são strings normais, comumente escritas usando aspas triplas (''') para possibilitar a definição de string multilinhas.

    - O que torna docstrings especial é sua localização no código.

Docstrings aparecem após uma definição, seja de um módulo, classe, método ou função.

    - Diversas ferramentas vasculham arquivos de código fonte buscando docstrings para conversão automática em documentos de documentação.

Sintaxe compatível com Sphinx, pacote comumente utilizado para gerar documentação. Usado para documentação por: Google, Facebook e NASA

- Documentação escrita assim pode ser mais fácil de manter do que um documento completamente separado

- Possui a vantagem de também funcionar como comentário, ficando visível enquanto se olha o código fonte.