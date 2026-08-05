# 🖨️ Gerador de Etiquetas para Laboratórios de Informática

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Automatize a criação de etiquetas para computadores de laboratórios escolares utilizando **Python**, **Pandas** e **ReportLab**.

O projeto realiza a leitura automática de planilhas Excel contendo os alunos de cada turma e gera um PDF pronto para impressão com as etiquetas de identificação dos computadores.

---

## 📸 Exemplo

![Etiquetas](images/exemplo.png)

---

# ✨ Funcionalidades

* 📄 Leitura automática dos mapões em Excel (`.xlsx`)
* 📂 Processamento de todos os arquivos da pasta `mapoes`
* 🏫 Nome da escola configurável
* 🎨 Layout totalmente personalizável
* 👨‍🎓 Suporte para múltiplas turmas
* 🖨️ Geração automática de etiquetas em PDF
* 🧩 Código modular e de fácil manutenção

---

# 📁 Estrutura do Projeto

```text
ProjetoEtiquetas/
│
├── config.py              # Configurações do projeto
├── desenho.py             # Desenho das etiquetas
├── gerar_etiquetas.py     # Programa principal
├── leitor.py              # Leitura dos arquivos Excel
│
├── mapoes/                # Planilhas das turmas
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Tecnologias utilizadas

* Python 3
* Pandas
* OpenPyXL
* ReportLab

---

# 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/GiovaniRamires/ProjetoEtiquetas.git
```

Entre na pasta:

```bash
cd ProjetoEtiquetas
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# 📄 Estrutura esperada das planilhas

Crie uma pasta chamada **mapoes** na raiz do projeto.

Dentro dela, coloque os arquivos das turmas.

Exemplo:

```text
mapoes/
├── MAPAO_6A.xlsx
├── MAPAO_6B.xlsx
├── MAPAO_7A.xlsx
├── MAPAO_7B.xlsx
├── MAPAO_8A.xlsx
├── MAPAO_8B.xlsx
├── MAPAO_9A.xlsx
└── MAPAO_9B.xlsx
```

O programa identifica automaticamente a turma pelo nome do arquivo.

Cada planilha deve conter uma coluna chamada:

```text
ALUNO
```

As demais colunas são ignoradas.

---

# ▶️ Como executar

Após adicionar os mapões:

```bash
python gerar_etiquetas.py
```

Ao final será criado o arquivo:

```text
Etiquetas_COMP.pdf
```

---

# ⚙️ Personalização

Grande parte da personalização pode ser feita no arquivo `config.py`.

É possível alterar:

* Nome da escola
* Nome dos computadores
* Turmas
* Cores
* Fontes
* Tamanho das etiquetas
* Margens
* Espaçamento
* Quantidade de etiquetas por página

O objetivo é permitir que qualquer instituição adapte facilmente o projeto ao seu próprio padrão.

---

# 📂 Organização do código

O projeto foi dividido em módulos para facilitar a manutenção.

### `config.py`

Centraliza todas as configurações do projeto.

### `leitor.py`

Responsável pela leitura das planilhas Excel e montagem dos dados.

### `desenho.py`

Contém toda a lógica de criação das etiquetas utilizando ReportLab.

### `gerar_etiquetas.py`

Arquivo principal responsável por gerar o PDF.

---

# 🚀 Possíveis melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* Interface gráfica com Tkinter
* Exportação de relatórios em Excel
* Suporte a outros modelos de etiquetas
* Configuração por arquivo `.json`
* Compatibilidade com diferentes modelos de planilhas

---

# 🤝 Contribuições

Contribuições são bem-vindas.

Caso encontre algum problema ou tenha sugestões de melhorias, fique à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

---

# 📄 Licença

Este projeto está licenciado sob a licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por **Giovani Ramires**.

Se este projeto foi útil para você, considere deixar uma ⭐ no repositório.
