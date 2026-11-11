
import gradio as gr
import pandas as pd
import os
from datetime import datetime

# Nome do arquivo onde os cadastros serao armazenados
ARQUIVO_CSV = os.path.join(os.path.dirname(__file__), "pacientes.csv")

# Colunas do arquivo CSV
COLUNAS = [
    "timestamp",
    "nome",
    "idade",
    "convenio",
    "prioridade",
    "motivo"
]

# Funcao executada ao clicar no botao Cadastrar
def cadastrar_paciente(nome, idade, convenio, prioridade, motivo):

    # Validacao dos campos obrigatorios
    if not nome or not nome.strip():
        return "Informe o nome do paciente.", carregar_ultimos()

    if idade is None or idade < 0 or idade > 120:
        return "Informe uma idade valida entre 0 e 120.", carregar_ultimos()

    if not motivo or not motivo.strip():
        return "Informe o motivo da consulta.", carregar_ultimos()

    # Criacao do registro
    linha = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": nome.strip(),
        "idade": int(idade),
        "convenio": convenio,
        "prioridade": int(prioridade),
        "motivo": motivo.strip()
    }

    # Transformacao em tabela Pandas
    novo = pd.DataFrame([linha], columns=COLUNAS)

    # Grava o cadastro no arquivo CSV
    if os.path.exists(ARQUIVO_CSV):
        novo.to_csv(
            ARQUIVO_CSV,
            mode="a",
            header=False,
            index=False,
            encoding="utf-8-sig"
        )
    else:
        novo.to_csv(
            ARQUIVO_CSV,
            mode="w",
            header=True,
            index=False,
            encoding="utf-8-sig"
        )

    return "Paciente cadastrado com sucesso!", carregar_ultimos()


# Funcao que mostra os cinco cadastros mais recentes
def carregar_ultimos():
    if os.path.exists(ARQUIVO_CSV):
        return pd.read_csv(ARQUIVO_CSV).tail(5)

    return pd.DataFrame(columns=COLUNAS)


# Construcao da interface com Gradio
with gr.Blocks() as demo:

    gr.Markdown("# Cadastro de Pacientes")
    gr.Markdown("Formulario de registro de atendimentos")

    nome = gr.Textbox(label="Nome do paciente")

    idade = gr.Number(
        label="Idade",
        minimum=0,
        maximum=120,
        precision=0
    )

    convenio = gr.Dropdown(
        choices=[
            "Particular",
            "Unimed",
            "Bradesco Saúde",
            "SulAmérica",
            "Outro"
        ],
        label="Convênio",
        value="Particular"
    )

    prioridade = gr.Slider(
        minimum=1,
        maximum=5,
        step=1,
        value=1,
        label="Prioridade do atendimento"
    )

    motivo = gr.Textbox(
        label="Motivo da consulta / observações",
        lines=3
    )

    botao = gr.Button("Cadastrar", variant="primary")

    saida_msg = gr.Textbox(
        label="Status do cadastro",
        interactive=False
    )

    tabela = gr.Dataframe(
        label="Últimos cinco pacientes cadastrados",
        interactive=False
    )

    botao.click(
        fn=cadastrar_paciente,
        inputs=[nome, idade, convenio, prioridade, motivo],
        outputs=[saida_msg, tabela]
    )

# Inicia o aplicativo
demo.launch()
