# Myeye Backend

O Myeye Backend é um sistema desenvolvido em Python para controle de custos, permitindo a geração de relatórios por multiempresas.

## Funcionalidades

- Controle de custos por multiempresas.
- Geração de relatórios de custos.
- Outras funcionalidades relevantes do sistema.

## Requisitos

- Python 3.x
- Django Framework
- Outras dependências (listar todas as dependências relevantes)

## Instalação

1. Clone este repositório para o seu ambiente local.
2. Crie um ambiente virtual usando o comando: `python -m venv venv`.
3. Ative o ambiente virtual com o comando: 
   - No Windows: `venv\Scripts\activate`
   - No Linux/Mac: `source venv/bin/activate`
4. Instale as dependências com o comando: `pip install -r requirements.txt`.
5. Execute o script de inicialização do banco de dados (se houver).
6. Inicie o servidor backend com o comando: `python app.py`.

## Configuração

Antes de executar o sistema, é necessário realizar algumas configurações adicionais.

1. Verifique as configurações do banco de dados no arquivo de configuração do sistema (`config.py`) e atualize-as de acordo com o seu ambiente.
2. Verifique e atualize as configurações de autenticação, se aplicável.
3. Configure as empresas disponíveis para controle de custos no banco de dados, conforme necessário.

## Uso

- Acesse a API do sistema utilizando um cliente HTTP (por exemplo, cURL ou Postman) para realizar as requisições.
- Consulte a documentação da API para obter informações sobre as rotas disponíveis e os parâmetros necessários.
- Realize as requisições apropriadas para controle de custos, geração de relatórios, etc.

## Estrutura do Projeto

O projeto possui a seguinte estrutura de diretórios:

- `app/`: Diretório contendo o código-fonte do sistema.
- `migrations/`: Diretório contendo as migrações do banco de dados (se houver).
- `tests/`: Diretório contendo os testes automatizados do sistema (se houver).
- `requirements.txt`: Arquivo contendo as dependências do projeto.
- `config.py`: Arquivo de configuração do sistema.
- `app.py`: Script de inicialização do sistema.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie uma nova branch com a sua feature ou correção: `git checkout -b minha-feature`.
3. Faça as alterações desejadas no código.
4. Faça o commit das suas alterações: `git commit -m 'Minha nova feature'`.
5. Faça o push para a branch criada: `git push origin minha-feature`.
6. Envie um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
