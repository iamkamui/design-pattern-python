## Definição

A Programação Orienteda à Objetos (POO) ou Object-oriented programming (OOP) é 
um paradigma baseado no conceito de envolver pedaços de dados, e comportamentos
relacionados aqueles dados, em uma coleção chamada objetos, que são construídos
de um conjunto de “planos de construção”, definidos por um programador, chamados
de classes.

## Design

Utiliza-se de um diagrama UML para representação gráfica de uma classe onde que tem 
`campos` da classe que são atributos padrão da mesma, dados armazenados no campo da
clase são referenciados como estado. E tem  `métodos da classe` que são seus comportamentos.
Coletivamente, os campos e métodos podem ser referenciados como membros de suas classes.

### Hierarquia de classe

**Utilização**
Utiliza-se a hierarquia quando se tem objetos com características em comum.

* Classe Mãe - chamada de superclasse possui características em comum que será herdada pela classe filha
* Classe Filha - chamada de subclsse herda estado e comportamento de sua mãe, definindo apenas atributos e comportamentos que diferem

> Subclasses podem sobrescrever o comportamento de métodos que herdam da classe mãe, tanto para 
> substituir o comportamento padrão ou melhorar com coisas adicionais.

## Pilares da OOP

A programação orientada a objetos é baseada em quatro pilares, conceitos que diferenciam ela de
outros paradigmas de programação: [Abstração](_abstraction.py), [Encapsulamento](_encapsulation.py),
[Herança](_inheritance.py) e [Polimorfismo](_polymorphism.py)


### Abstração

A [Abstração](_abstraction.py) é um modelo de um objeto ou fenêmeno do mundo real, limitado a um contexto específico, representando
detalhes relevantes para esse contexto omitindo o que não é.

### Encapsulamento

O [Encapsulamento](_encapsulation.py) é a habilidade de um objeto de escoder parte de seu estado e comportamentos de outros objetos, expondo somente uma interface limitada para o resto do programa. `Encapsular` significa torná-la `privada`, e por tanto acessível apenas por dentro dos métodos da sua própria classe.

> Há um modo um pouco menos restritivo chamado `protegido` que torna um membro da classe disponível para subclasses também.


### Polimorfismo

O [Polimorfismo](_polymorphism.py) é a habilidade de um programa detectar a classe real de um objeto e chamar sua implementação mesmo quando seu tipo real é desconhecido do contexto atual.

### Herança

A [Herança](_inheritance.py) é a habilidade de construir novas classes em cima de classes já existentes. Na qual a subclasse herda da classe mãe os seus campos e métodos.


#### Referência
<ul>
<li><a href="https://refactoring.guru/design-patterns/book">https://refactoring.guru/design-patterns/book</a></li>
</ul>