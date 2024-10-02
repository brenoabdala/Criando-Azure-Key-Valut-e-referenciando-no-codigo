# Configurações
name_key_valut = ""
chave1 = ""
chave2 = ""
chave3 = ""

# Criar credenciais
credential = DefaultAzureCredential()

# Criar um cliente do Key Vault
key_vault_url = f"https://{name_key_valut}.vault.azure.net/"
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Recuperar o segredo
chave1_ = secret_client.get_secret(chave1)
db_chave1 = chave1_.value

chave2_ = secret_client.get_secret(chave2)
db_chave2 = chave2_.value

chave3_ = secret_client.get_secret(chave3)
db_chave3 = chave3_.value
