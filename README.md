# Cadastro de Pacientes — Gradio e Streamlit

## Sobre o projeto

Projeto desenvolvido para a atividade prática da disciplina **Aplicações em Data Science**, da pós-graduação da UNICAMP, ministrada pelo professor Francisco Fambrini.

O objetivo é desenvolver e comparar duas interfaces web para coleta de dados de pacientes, utilizando Python e as bibliotecas Gradio e Streamlit.

**Os dados utilizados nos testes são fictícios e destinados exclusivamente a fins acadêmicos.**

## Funcionalidades

Os dois aplicativos permitem:

- Cadastrar o nome do paciente.
- Informar a idade.
- Selecionar o convênio médico: Particular, Unimed, Bradesco Saúde, SulAmérica ou Outro.
- Definir a prioridade do atendimento de 1 a 5.
- Registrar o motivo da consulta ou observações.
- Registrar automaticamente a data e a hora do cadastro.
- Visualizar os cinco cadastros mais recentes.

### Aplicativo Gradio

O aplicativo Gradio é executado localmente e salva os cadastros no arquivo `pacientes.csv`.

Após cada cadastro, apresenta uma mensagem de confirmação e atualiza a tabela com os cinco registros mais recentes.

### Aplicativo Streamlit

O aplicativo Streamlit utiliza `st.session_state` para armazenar temporariamente os cadastros durante a sessão.

Também disponibiliza um botão para baixar os registros no formato CSV.

A aplicação foi publicada no Streamlit Community Cloud.

## Acessar o aplicativo

**[Abrir aplicativo Streamlit](https://cadastro-pacientes-unicamp-vsc.streamlit.app/)**

## Estrutura do projeto

```text
atividade-datascience-unicamp/
├── gradio_app/
│   ├── app.py
│   ├── pacientes.csv
│   └── gradio_cadastro.png
├── streamlit_app/
│   └── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Tecnologias utilizadas

- Python
- Gradio
- Streamlit
- Pandas
- GitHub
- Streamlit Community Cloud

## Como executar localmente

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Para executar o Gradio:

```bash
python gradio_app/app.py
```

Para executar o Streamlit:

```bash
python -m streamlit run streamlit_app/app.py
```

## Comparação das ferramentas

| Característica | Gradio | Streamlit |
|---|---|---|
| Interface | `gr.Blocks()` | `st.form()` |
| Armazenamento | CSV local | Estado da sessão |
| Visualização | Cinco últimos registros | Cinco últimos registros |
| Exportação | CSV salvo localmente | Download de CSV |
| Disponibilização | Execução local | Publicação na nuvem |

## Evidências da atividade

A pasta `gradio_app` contém:

- `gradio_cadastro.png`: captura de tela do aplicativo Gradio em funcionamento.
- `pacientes.csv`: arquivo de exemplo com registros fictícios.

## Considerações finais

A atividade permitiu explorar o desenvolvimento de interfaces web para coleta de dados utilizando Python.

O Gradio demonstrou uma abordagem baseada em componentes e eventos, enquanto o Streamlit apresentou uma abordagem integrada ao fluxo de execução do script e ao gerenciamento de estado da sessão.

Ambas as ferramentas permitem desenvolver aplicações interativas sem a necessidade de implementar diretamente interfaces em HTML, CSS ou JavaScript.
