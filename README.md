## README.md impecável para o seu projeto: Guia completo para download e execução no Windows

**Seja bem-vindo ao guia completo para baixar e executar seu projeto no Windows!**

Este guia detalhado irá te auxiliar a instalar e executar seu projeto com sucesso, passo a passo.

**Requisitos:**

* Git instalado no seu sistema.
* MySQL instalado e em execução.
* Arquivo `requirements.txt` com as dependências do projeto.
* Arquivo `.env` com as configurações de banco de dados.
* Arquivos `auxiliar.py` e `main.py` do projeto.

**Passo a passo:**

**1. Clone o repositório:**

Abra o prompt de comando (cmd) e navegue até o diretório onde deseja clonar o repositório. Utilize o seguinte comando:

```bash
git clone https://github.com/ricardoasmendes/alura-projeto-flask-jogoteca.git
```

**2. Instale as dependências:**

Acesse o diretório do projeto clonado e execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

**3. Configure o arquivo .env:**

Crie o arquivo `.env` na raiz do diretório do projeto e adicione as seguintes variáveis de ambiente, substituindo os valores de acordo com sua configuração do MySQL:

```
HOST=localhost
USER=usuario_mysql
PASSWORD=senha_mysql
```

**4. Crie o banco de dados e tabelas:**

Execute o seguinte comando para executar o script `prepara_banco.py` e criar o banco de dados e as tabelas:

```bash
python prepara_banco.py
```

**5. Execute o projeto:**

Finalmente, execute o seguinte comando para iniciar o projeto:

```bash
python jogoteca.py
```

**Observações importantes:**

* Certifique-se de ter o MySQL em execução antes de executar o script `auxiliar.py`.
* Substitua os valores de `HOST`, `USER` e `PASSWORD` no arquivo `.env` com as credenciais de acesso ao seu banco de dados MySQL.
* Se você encontrar algum erro durante a execução, consulte os logs do projeto ou procure ajuda na comunidade online.


**Com este guia completo, você estará pronto para baixar, instalar e executar seu projeto no Windows com sucesso!**
