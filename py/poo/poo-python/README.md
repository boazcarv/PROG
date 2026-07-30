# POO em Python — material de estudo

Apostila e códigos da disciplina **Programação Orientada a Objetos**
(Tecnologia em Sistemas para Internet), com exemplos em Python 3.

## Comece por aqui

📖 **[APOSTILA_POO_Python.md](APOSTILA_POO_Python.md)** — 8 capítulos + apêndices.

## Como rodar os códigos

```bash
cd codigo
python3 cap01_fundamentos.py      # classes, encapsulamento, herança, ABC
python3 cap03_excecoes.py         # try/except, exceções personalizadas
python3 cap05_serializacao.py     # arquivos, CSV, JSON, pickle
python3 cap06_gui.py              # janela Tkinter (agenda de contatos)

cd cap04_pacotes && python3 main.py            # módulos e pacotes

cd ../projeto_biblioteca
python3 main.py                                # projeto final (GUI)
python3 main.py --console                      # projeto final (terminal)
```

Requisitos: apenas Python 3.10+ (tudo usa a biblioteca padrão).
Para conferir se o Tkinter está disponível: `python3 -m tkinter`

## Mapa da ementa

| Item da ementa | Capítulo | Código |
|---|---|---|
| 1. Fundamentos de POO | 1 | `cap01_fundamentos.py` |
| 2. Modelagem UML | 2 | (diagramas na apostila) |
| 3. Tratamento de exceções | 3 | `cap03_excecoes.py` |
| 4. Modularização e pacotes | 4 | `cap04_pacotes/` |
| 5. Serialização | 5 | `cap05_serializacao.py` |
| 6. Interface gráfica | 6 | `cap06_gui.py` |
| Todos, integrados | 7 | `projeto_biblioteca/` |
