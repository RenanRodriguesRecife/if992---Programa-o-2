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


### Fachada

Fachadas é uma classe que provém uma interface mais transparente e unificada para processos complexos, permitindo acesso mais simplificado a subsistemas

#### Pontos positivos:

- Isolar o código da complexidade do sistema;

- Facilidade no processo de teste;

#### Pontos negativos:

- Mudanças nos métodos podem levar a mudanças na fachada;

- Definição de uma fachada pode ser custoso

#### Possíveis usos:

- Prover interface simples a sistemas complexos

- Divisão de sistemas grandes em camadas;



```python
class SocialSharing:
    def shareURL(self, url):
        facebookAPI.share(url)
        twitterAPI.share(url)
        instagramAPI.share(url)

```

### Flyweight



#### Pontos positivos:




#### Pontos negativos:




#### Possíveis usos:


```python

```