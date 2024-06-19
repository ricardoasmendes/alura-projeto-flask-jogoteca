## Guia para download e execução no Windows

**Seja bem-vindo ao guia para baixar e executar seu projeto no Windows!**

Este guia detalhado irá te auxiliar a instalar e executar seu projeto com sucesso, passo a passo.

**Requisitos:**

* Git instalado no seu sistema.
* MySQL instalado e em execução.
* Python versão 3.12.4

**Passo a passo:**

**1. Clone o repositório:**

Abra o prompt de comando Git Bash e navegue até o diretório onde deseja clonar o repositório. Utilize o seguinte comando no Git Bash:

```bash
git clone https://github.com/ricardoasmendes/alura-projeto-flask-jogoteca.git
```

**2. Versão do Python:**

Certifique-se de ter o Python 3.12.4 instalado em seu sistema. Você pode verificar sua versão do Python executando o seguinte comando no prompt de comando:

```terminal
python --version
```


**3. Criar um ambiente virtual:**

Para isolar as dependências do projeto e evitar conflitos com outros sistemas Python, é recomendável criar um ambiente virtual. Siga estas etapas:

1. Abra o prompt de comando e navegue até o diretório raiz do seu projeto.
2. Execute o seguinte comando para criar o ambiente virtual :

```terminal
python -m venv venv
```

3. Ative o ambiente virtual executando o seguinte comando :

```terminal
venv\Scripts\activate
```

**4. Ativar o ambiente virtual:**

Sempre que iniciar uma nova sessão no prompt de comando, você precisará ativar o ambiente virtual para que os comandos funcionem corretamente. Utilize o comando de ativação conforme descrito na etapa 3.3.



**5. Instale as dependências:**

Acesse o diretório do projeto clonado e execute o seguinte comando para instalar as dependências:

```terminal
pip install -r requirements.txt
```

**6. Configure o arquivo .env:**

Crie o arquivo `.env` na raiz do diretório do projeto e adicione as seguintes variáveis de ambiente, substituindo os valores de acordo com sua configuração do MySQL:

```
HOST=localhost
USER=usuario_mysql
PASSWORD=senha_mysql
```

**7. Crie o banco de dados e tabelas:**

Execute o seguinte script `prepara_banco.py` para criar a database e as tabelas:


**8. Execute o projeto:**

Finalmente, execute o seguinte script `jogoteca.py` para iniciar o projeto:


**Observações importantes:**

* Certifique-se de ter o MySQL em execução antes de executar o script `prepara_banco.py`.
* Substitua os valores de `HOST`, `USER` e `PASSWORD` no arquivo `.env` com as credenciais de acesso ao seu banco de dados MySQL.
* Se você encontrar algum erro durante a execução, consulte os logs do projeto ou procure ajuda na comunidade online.


**Com este guia completo, você estará pronto para baixar, instalar e executar seu projeto no Windows com sucesso!**





