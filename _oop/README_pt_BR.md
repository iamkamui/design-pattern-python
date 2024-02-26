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
outros paradigmas de programação: [Abstração](abstraction.py), [Encapsulamento](encapsulation.py),
[Herança](inheritance.py) e [Polimorfismo](polimorfism.py)


### Abstração

A [Abstração](abstraction.py) um modelo de um objeto ou fenêmeno do mundo real, limitado a um contexto específico, representando
detalhes relevantes para esse contexto omitindo o que não é.
