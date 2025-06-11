"""
en_US:
    List in python are used to store collections of heterogeneus items.
    these are mutable, which means that you can change their content without changing their identity.
    You can recognize/initialize lists by their square brackets '[' and ']' and python built in class 'list()'.

pt_BR:
    Lista em python é utilizada para armazenar coleções de items variados.
    Estes são mutáveis, o que significa que pode trocar seu conteudo sem perder sua identidade.
    Você pode reconhecer listas por seus colchetes '[' e ']' e a classe python padrão 'list()'
"""

# Initializing a empty List
joe = []
doe = list()

# Initializing a List with various types of elements
foo = ["bar", 1, {}, "bar", ["joe", 5, "doe"], "1"] #note: Yes, its possible to have a list inside another list.

# Accessing elements from the list
foo[0]  # output: bar
foo[-1]  # output: 1
foo[2]  # output: {}
