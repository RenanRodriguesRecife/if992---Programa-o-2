## Visibilidade

### Público, protegido e privado

OOP tem como um de seus conceitos principais o encapsulamento. A ideia de agrupar dados e métodos e **esconder** representações internas.

### Encapsulamento

- Isso inclui esconder tanto atributos quanto métodos em escopos em que não precisam ser acessados.

- Para algumas linguagens (Java, PHP, etc.) o programador deve ser considerado um risco.

- Surgem então, as visibilidades para definirmos em que escopos atributos e propriedades serão acessadas.

#### Publico

Meus alunos sabem que eu moro na praia, se estivermos em um dia quente, eles sabem que podem bater na minha porta e eu oferecerei um refrigerante. Eu não moro em um condomínio fechado, logo qualquer um pode aparecer, minha porta é **pública**.
Stephen Gilbert

- Atributos e métodos públicos podem ser acessados em qualquer lugar.

- Em Python, a filosofia é um pouco diferente, programadores são considerados adultos responsáveis. 

- Portanto, em Python, todos os atributos e métodos são públicos.

- Em linguagens de visibilidade explícita, utilizamos a palavra chave public.

#### Protegido

Os alunos, no entanto, não podem simplesmente entrar e pegar um refrigerante na minha geladeira, ela não é **pública**.
Mas meus netos, que moram perto, não ligam para entrar e pegar o que quiserem na cozinha, na nossa **casa (pacote)**, minha geladeira é **protegida**.
Stephen Gilbert

- Atributos e métodos **protegidos** só podem ser acessados/modificados por membros do mesmo projeto.

- Em Python, utilizamos ‘_’ como convenção para definir atributos “protegidos”, a ideia é apenas evitar acessos/re-escritas não-intencionais.

- Em linguagens explícitas, definimos com protected.

### Privado

