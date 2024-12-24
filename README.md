# Mensagem de Férias Google Workspace

### No Google Admin Console, não existe uma configuração nativa para configurar respostas automáticas de férias diretamente para todos os usuários. Essa funcionalidade precisa ser gerenciada individualmente pelos próprios usuários ou implementada via automação, como com a API do Gmail.

Usar a API do Gmail para configurar mensagens de férias para todos os usuários do Google Workspace envolve algumas etapas.

#### 1. Ativar a API do Gmail
- Acesse o Google Cloud Console (https://console.cloud.google.com/) e faça login com sua conta. Não precisa ser a mesma do Google Workspace
- Crie um projeto ou use um já existente. Ex: Nome de sua Empresa
- No menu do projeto, acesse **APIs e Serviços > Biblioteca**
- Pesquise por **Gmail API** e ative-a.

#### 2. Criar a Conta de Serviço
- Acesse o Google Cloud Console
- No menu superior, selecione o projeto onde você ativou a Gmail API
- No menu lateral, vá para **APIs e Serviços > Credenciais**
- Clique em **Criar credenciais > Conta de serviço**
- Preencha as informações da conta de serviço (nome, descrição)
- Clique em **Criar e continuar**
- Escolha o papel apropriado (proprietário ou administrador)
- Clique em **Concluir**

#### 3. Fazer o Download do Arquivo JSON
- Após criar a conta de serviço, você verá a conta listada em Credenciais
- Clique no nome da conta de serviço recém-criada
- Na página de detalhes da conta de serviço, vá até a seção Chaves
- Clique em **Adicionar chave > Criar nova chave**
- Selecione o formato **JSON**.
- O arquivo será baixado automaticamente para o seu computador

#### 4. Salvar o Arquivo JSON com Segurança
- Renomeie o arquivo, se necessário, para algo como credentials_SuaEmpresa.json.
- Salve o arquivo em um local seguro, pois ele contém informações sensíveis que podem ser usadas para acessar a API.


#### 3. Delegar Domínio para a Conta de Serviço
- Acesse o Admin Console do Google Workspace (https://admin.google.com) com sua conta administrativa
- Acesse **Segurança > Controle de dados e acesso > Controles de API**
- Clique em **GERENCIAR  A DELEGAÇÃO EM TODO DOMÍNIO**
- Crie uma nova  conta de serviço com o ID que você criou (está no arquivo JSON) e com os seguintes escopos OAuth: https://www.googleapis.com/auth/gmail.settings.basic, https://www.googleapis.com/auth/gmail.modify
- Clique em Autorizar

### 4. Utilização do script python
- Faça o download do script para uma pasta em seu computador local ou para um ambiente em que deseja executá-lo
- Certifique-se de que o Python está instalado (versão 3.7 ou superior)
- É uma boa prática usar um ambiente virtual para isolar os pacotes, portanto, crie o ambiente virtual:
```
python -m venv NomeAmbienteVirtual
```
- Ative o ambiente no Linux/Mac/WSL:
```
source NomeAmbienteVirtual/bin/activate
```
- Ative o ambiente no Windows, se estiver utilizando:
```
.\NomeAmbienteVirtual\Scripts\activate
```

Instale as bibliotecas dentro do ambiente:
```
pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib
```

- Ajuste os parâmetros indicados no script (arquivo de credenciais, emails, data de inicío e de término e mensagem html)

- Execute o script:
```
python MensagemFeriasWorkspace.py
```
- Se tudo estiver correto, aparcerá uma mensagem de retorno, indicando que a configuração foi feita com sucesso em cada e-mail.

