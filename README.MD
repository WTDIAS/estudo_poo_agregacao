```markdown
# 📚 Estudo de POO com Python

Este projeto tem como objetivo explorar os principais conceitos da Programação Orientada a Objetos (POO) utilizando Python, por meio da modelagem de um sistema simples de livros, autores e capítulos.

## 🧠 Conceitos Abordados

- **Herança**
- **Encapsulamento**
- **Agregação**

> ⚠️ **Nota pessoal:**  
> O exemplo proposto originalmente pela IA Gemini utiliza o conceito de **agregação** para modelar a classe `Livro`, permitindo que ela exista sem autores ou capítulos. No entanto, considero que o mais adequado seria aplicar **composição**, exigindo que `Livro` receba obrigatoriamente `Autor` e `Capitulo` como parâmetros no momento da criação. Isso garantiria maior integridade na modelagem do domínio.

---

## 🏗️ Estrutura do Projeto

```
poo_agregacao/
├── src/
│   ├── __init__.py
│   ├── agregacao.py
├── tests/
│   ├── __init__.py
│   ├── test_agregacao.py
├── .gitignore
└── README.md
```

---

## 📦 Módulos

### `Autor`
Representa um autor com nome e nacionalidade, com validações para garantir dados consistentes.

### `Capitulo`
Modela um capítulo com título e número de páginas, também com validações.

### `Livro`
Agrega autores e capítulos, permitindo o cadastro posterior. Contém métodos para adicionar autores e capítulos dinamicamente.

---

## 🧪 Testes

Os testes foram desenvolvidos com `unittest` e cobrem:

- Validação de atributos
- Comportamento esperado das classes
- Casos de erro com dados inválidos

Para rodar os testes, basta executar o arquivo de testes diretamente:

python tests/test_agregacao.py
Como o script contém:

if __name__ == "__main__":
    unittest.main()
Os testes serão executados automaticamente.

---

## ▶️ Execução

O script principal (`agregacao.py`) contém um exemplo de uso das classes:

```python
if __name__ == "__main__":
    autor1 = Autor("Flavio Augusto", "Brasileira")
    capitulo1 = Capitulo("O clique da confiança", 5)
    capitulo2 = Capitulo("O bico", 6)
    livro1 = Livro("Ponto de inflexão", 2022)
    livro1.cadastrar_autores(autor1)
    livro1.cadastrar_capitulo(capitulo1)
    livro1.cadastrar_capitulo(capitulo2)

    print(livro1)
```

---

## 💡 Aprendizados

Este projeto reforça a importância de:

- Validar dados de entrada
- Separar responsabilidades entre classes
- Refletir sobre o uso adequado de agregação vs. composição
- POO Programação Orientada a Objetos
---

## 📜 Licença

Este projeto é apenas para fins educacionais e não possui uma licença específica. Sinta-se à vontade para estudar, modificar e compartilhar.

---

Feito com 💻 e curiosidade por WALDIR.
```
