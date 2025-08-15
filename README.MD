
# 📚 Estudo de POO em Python – Conceito de Agregação

Este projeto é um exemplo prático do uso de **Programação Orientada a Objetos (POO)** em Python, com foco no conceito de **Agregação**.  
Foi desenvolvido para demonstrar a criação e interação entre classes representando um **Livro**, seus **Autores** e **Capítulos**.

## 🚀 Conceitos abordados
- **Herança**
- **Encapsulamento**
- **Agregação**
- **Boas práticas de validação de dados**
- **Testes unitários com `unittest`**

> 💡 Observação: Embora este projeto utilize **Agregação** (onde Livro pode existir sem Autores ou Capítulos), o autor do código observa que, em um caso real, poderia ser mais adequado usar **Composição**, exigindo que o livro seja criado já com autores e capítulos.

---

## 📂 Estrutura do projeto
```

poo\_agregacao/
│
├── src/
│   ├── **init**.py
│   ├── agregacao.py       # Código principal com as classes Autor, Capitulo e Livro
│
├── tests/
│   ├── **init**.py
│   ├── test\_agregacao.py  # Testes unitários para as classes
│
├── .gitignore
├── README.md

````

---

## 🛠️ Tecnologias utilizadas
- **Python 3.10+**
- **unittest** (biblioteca padrão do Python para testes)

---

## 📜 Como executar o projeto

### Executar o código principal

```bash
python src/agregacao.py
```



## 🧪 Executando os testes

Para rodar os testes, basta executar o arquivo de testes diretamente:

```bash
python tests/test_agregacao.py
```

Como o script contém:

```
if __name__ == "__main__":
    unittest.main()
```

Os testes serão executados automaticamente.

---

## 📌 Funcionalidades principais

* **Classe `Autor`**

  * Armazena nome e nacionalidade.
  * Valida dados no momento da atribuição.

* **Classe `Capitulo`**

  * Armazena título e número de páginas.
  * Valida dados para evitar valores inválidos.

* **Classe `Livro`**

  * Pode ter zero ou mais autores e capítulos.
  * Métodos para cadastrar autores e capítulos.

---

## 📷 Exemplo de uso

```python
from src.agregacao import Autor, Capitulo, Livro

autor1 = Autor("Flavio Augusto", "Brasileira")
cap1 = Capitulo("O clique da confiança", 5)
cap2 = Capitulo("O bico", 6)

livro = Livro("Ponto de inflexão", 2022)
livro.cadastrar_autores(autor1)
livro.cadastrar_capitulo(cap1)
livro.cadastrar_capitulo(cap2)

print(livro)
```

### 💡 Saída esperada:

```
Livro: Ponto de inflexão 2022 
Autores: Nome do autor: Flavio Augusto | Nacionalidade: Brasileira 
Capítulos: 
 -Titulo do capítulo: O clique da confiança | Quantidade de paginas: 5
 -Titulo do capítulo: O bico | Quantidade de paginas: 6
```

---

## 📄 Licença

Este projeto está sob a licença MIT.
Sinta-se à vontade para utilizar, modificar e distribuir.

---

✍️ **Autor:** Waldir Tiago Dias\
💬 Projeto criado para fins de estudo e prática de POO em Python.

