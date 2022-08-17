## Padrões

### Singleton

O padrão Singleton garante que apenas uma instância de uma classe seja criada e que a instância seja acessível globalmente.

- O objeto singleton é inicializado de forma lazy.

#### Pontos positivos:

- Inicialização cara;

- Uso raro;


#### Pontos negativos:

- Fácil, mal uso;

- Difícil teste;

#### Possíveis usos:

- Ler arquivos de configuração durante um startup;

- Classe de logging;

- Gerenciamento de conexão para recurso limitado;

```python
class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance
```