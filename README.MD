# 🧠 Projeto POO com Agregação em Python

Este projeto é um estudo prático de Programação Orientada a Objetos (POO) em Python, com foco nos conceitos de **abstração**, **herança**, **polimorfismo**, **agregação** e uso de `**kwargs`. Ele simula formas geométricas (Círculo, Triângulo e Retângulo) e calcula suas respectivas áreas, aplicando boas práticas de organização de código e testes automatizados.

---

## 📁 Estrutura do Projeto

```
poo_agregacao/
├── src/
│   ├── __init__.py
│   └── agregacao.py
├── tests/
│   ├── __init__.py
│   └── test_agregacao.py
```

- `src/agregacao.py`: contém as classes principais do projeto.
- `tests/test_agregacao.py`: contém os testes unitários para validar o comportamento das classes.

---

## 🧪 Tecnologias e Conceitos Aplicados

- ✅ Programação Orientada a Objetos
  - Abstração
  - Herança
  - Polimorfismo
  - Agregação
- ✅ `**kwargs` para flexibilidade na construção dos objetos
- ✅ Testes automatizados com `unittest`
- ✅ Validação de atributos via `@property` e `@setter`

---

## ▶️ Como Executar

Para rodar os testes, basta executar o arquivo de testes diretamente:

```bash
python tests/test_agregacao.py
```

Como o script contém:

```python
if __name__ == "__main__":
    unittest.main()
```

Os testes serão executados automaticamente.

---

## 📌 Exemplos de Uso

```python
Circulo(raio=5)
Triangulo(base=10, altura=4)
Retangulo(base=8, altura=3)
```

Cada classe possui validações internas e o método `calc_area()` que retorna a área formatada como string.

---

## 📄 Licença

Este projeto é de uso educacional e livre para estudo e aprimoramento. Sinta-se à vontade para contribuir ou adaptar.

---

Feito com dedicação por **Waldir** 💻
```

---
