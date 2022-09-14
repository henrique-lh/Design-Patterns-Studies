# Atividade 9- Padrão de Projeto Builder

## Desafio

* Criar uma aplicação precisa construir produtos (objetos): Pessoa, e Empresa. Para cada Empresa uma Pessoa deve ser responsável.

* Para construir uma Pessoa é preciso obter nome e identidade. Apenas se os dois forem lidos é que  Pessoa pode ser criada

* Para construir uma Empresa é preciso ler o nome e identidade do responsável e depois construir a Pessoa responsável.

Mostre em UML como poderia ser implementada uma aplicação que realizasse as tarefas acima utilizando o padrão de projeto Builder. Se possível, implemente (simule os dados com Strings).

**OBS**: Disponibiliza apenas os arquivos o PDF do UML e fonte (.java, .cpp, .py, etc) sem nenhum tipo de compressão.

## Resolução

* Como indicado na atividade, foi utilizado o padrão builder.
* O projeto conta com um arquivo "in.txt" que indica as entradas para o programa, e "out.txt" que fornecerá saídas.

## Execução

* Execute em seu terminal (comando voltando para computadores Linux):

```bash
$ python3 main.py <in.txt> out.txt
```

* Dessa forma será automaticamente colocado os inputs vindos do arquivo "in.txt" e redirecionando as saídas para o arquivo "out.txt".
* Para testar o programa manualmente, basta executar o programa em sua máquina ou digitar no terminal:

```bash
$ python3 main.py
```
