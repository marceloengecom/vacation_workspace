# Nome: Mensagem de Férias Workspace
# Descrição: Esse script Python permite acessar a API do Google e criar a mensagem de férias de contas do Google Workspace de forma automatizada.
#
# É necessário criar uma API no Google Cloud Console e conectar essa API ao Admin Console do Google Workspace. As instruções estão no arquivo README.md.
# 
# Antes de executar o script, defina os seus respectivos parâmetros (arquivo de credenciais, emails, data de inicío e de término e mensagem html), na seção de VARIÁVEIS A AJUSTAR.


from googleapiclient.discovery import build
from google.oauth2 import service_account
import datetime

SCOPES = [
    'https://www.googleapis.com/auth/gmail.settings.basic',
    'https://www.googleapis.com/auth/gmail.modify'
]

# Sequências ANSI para cores e estilos
RESET = "\033[0m"       # Reseta as cores e estilos
BOLD = "\033[1m"        # Negrito
GREEN = "\033[32m"      # Verde
RED = "\033[31m"        # Vermelho


#####################################################################
######################## VARIÁVEIS A AJUSTAR ########################
#####################################################################

# Informe o see arquivo de credencial gerado no Google Cloud Console
SERVICE_ACCOUNT_FILE = "Credenciais_SuaEmpresa.json"

# Informe a sua lista de emails
EMAILS = [
    "email_1@suaempresa.com",
    "email_2@suaempresa.com",
    "email_3@suaempresa.com",
    "email_4@suaempresa.com"
]
# Defina a data de início, no formato YYYY-MM-DD
START_DATE = "2024-12-22"

# Defina a data de término, no formato YYYY-MM-DD
END_DATE = "2025-01-05"

# Defina o assunto da mensagem
RESPONSE_SUBJECT = "**Recesso de Férias**"

# Defina a sua mensagem em HTML. A mensagem deve ficar entra as três aspas (""") e pode-se usar variáveis que estão no script.
RESPONSE_BODY_HTML = """
<div style="text-align: center;">
    <span style="color: #444444;">Prezados clientes e amigos,</span>
</div>
<div style="text-align: center;">
    <span style="color: #444444;">&nbsp;</span>
</div>
<div style="text-align: center;">
    <span style="color: #444444;">
        Informamos que estaremos em período de recesso entre os dias&nbsp;<strong>23/12/2024</strong>&nbsp;até&nbsp;<strong>05/01/2025</strong>.
    </span>
</div>
<div style="text-align: center;">&nbsp;</div>
<div style="text-align: center;">&nbsp;</div>
<div style="text-align: center;">&nbsp;</div>
<div style="text-align: center;">
    <strong>
        <span style="color: #e06666; font-size: large;">Boas festas!!!</span>
    </strong>
</div>
<div style="text-align: center;">&nbsp;</div>
<div style="text-align: center;">
    <hr noshade="noshade" size="2" />
    <strong>
        <span style="color: #333333; font-family: Verdana;">
            ENGESIS Tecnologia da Informação<br />
        </span>
    </strong>
    <span style="color: #666666; font-family: Verdana;">
        <br />Av. Manoel Elias, 2200/203 · Porto Alegre, RS · CEP: 91240-261<br />
        https://engesis.com.br  - WhatsApp: (51) 2160.9170
    </span>
</div>
"""
######################## FIM VARIÁVEIS A AJUSTAR ########################


# Função para autenticação
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Função para configurar férias
def set_vacation(user_ids, start_date, end_date):
    start_time = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_time = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    start_time_timestamp = int(start_time.timestamp() * 1000)
    end_time_timestamp = int(end_time.timestamp() * 1000)

    vacation_settings = {
        "enableAutoReply": True,
        "responseSubject": RESPONSE_SUBJECT,
        "responseBodyHtml": RESPONSE_BODY_HTML.format(start_date=start_date, end_date=end_date),
        "restrictToContacts": False,
        "restrictToDomain": False,
        "startTime": start_time_timestamp,
        "endTime": end_time_timestamp
    }

    for user_id in user_ids:
        try:
            delegated_credentials = credentials.with_subject(user_id)
            service = build('gmail', 'v1', credentials=delegated_credentials)
            result = service.users().settings().updateVacation(userId=user_id, body=vacation_settings).execute()
            print(f"{BOLD}{GREEN}Configuração de férias realizada com sucesso para {user_id}.{RESET}\n")
        except Exception as e:
            print(f"{BOLD}{RED}Erro ao configurar férias para {user_id}: {e}{RESET}\n")

# Configurar férias
set_vacation(EMAILS, START_DATE, END_DATE)
