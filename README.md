![Azure Key Valut](https://github.com/user-attachments/assets/409aeaec-8792-46e3-8be7-64f967f2b070)

### Criando Azure Key Valut e Referenciando no Código

<p> O propósito do processo a seguir é criar uma "Azure Key Valut" e chama-la no código desenvolvido, no exemplo apresentando será na linguagem Python.</p>

#### Requisitos

 - Acesso ao portal.azure.com;
	
#### Processo de criação da Key Valut

 - Acesse o portal.azure.com;
 - Pesquise por "Azure Key Valuts" e selecione;
 - No painel a esquerda clique em "Criar";

#### Configurar as informações do Key Vault 
 - Assinatura: Selecione a assinatura na qual você deseja criar o Key Vault;
 - Grupo de Recursos: Você pode escolher um grupo de recursos existente ou criar um novo;
 - Nome do Vault: Dê um nome único para o seu Key Vault;
 - Região: Selecione a região onde você deseja que o Key Vault seja hospedado.
 - Days to retain deleted vaults: 90;
 - Purge protection: Disable.
 
 Configurações de acesso
 - Modelo de Permissão: Politica de acesso ao cofre;
 - Acesso a recursos: Selecione as três opções;
 - Passe por todas as etaps e clique em "criar"
 
#### Atribuindo Valores secretos a Key Valut
- Menu lateral a esquerda selecione a opção "Objetos", selecione "Segredos";
- Clique em "Gerar/Importar";

##### Crie um Segredo
- Opção de Upload: Manual;
- Nome: Atribua um nome para chave ex: "Login";
- Valor secreto: passe o valor ex: nome de usuário";
- Tipo de conteúdo (opcional): Coloque a descrição de qual ferramenta vem aquele segredo ex: "Banco de Dados";
- Habilitado: Sim;
- Clique em "Criar".

##### Politica de acesso
###### Aba Permission 

- Selecione no menu lateral "Politica de acesso";
- Criar;
- Nas colunas "Key permissions", "Secret Permissions", "Certificate Permissions" selecione todas as opções dos check box;

###### Aba Principal 

- Selecione a aplicação que deseja acesso key valut ou usuário dentro da Azure, exemplo uma function, databricks e afins;
- Avance as telas e crie.

##### Associando a Key Valut a Azure Functions
- Acesse a function desejada;
- Aba lateral "Settings" -> "Identity" -> "On"

<p> Exemplo de código anexado no repositório </p>

##### Referências bibliográfica
<p> https://learn.microsoft.com/pt-br/azure/key-vault/general/quick-create-portal </p>
  
