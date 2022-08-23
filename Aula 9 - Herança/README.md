# Herança

## Composição

Composição é uma maneira de **agregar** objetos, tornando objetos atributos de outros.


Dadas duas classes Pessoa e Data:

- Pessoa tem um atributo dataDeAniverario, objeto da classe Data;

- Se descrevemos uma relação com tem um (**has-a**), há composição 

Composição pode ocorrer em relações:

- um-para-um;

- um-para-muitos;

- muitos-para-muitos.

E podem ser **unidirecionais** ou **bidirecionais**, dependendo das especificidades dos papéis.

Diferente da **agregação**, composição aponta em uma ligação forte entre objetos.

Se o objeto **possuidor** deixa de existir, o objeto **possuído** também deixa de existir.

<img src=".assets/arvfolha.jpg">