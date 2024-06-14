import firebase

# Configuração do Firebase
config = {
  "apiKey": "AIzaSyBbEV8hUZ4sLELpHmp9HPWsrKS9qxs6MCQ",
  "authDomain": "login1-f85ff.firebaseapp.com",
  "projectId": "login1-f85ff",
  "storageBucket": "login1-f85ff.appspot.com",
  "messagingSenderId": "781518658658",
  "appId": "1:781518658658:web:88c6981e58fcbda5f5053b",
  "measurementId": "G-RK7XL5L8BR"
}

# Inicializar o Firebase
firebase = firebase.initialize_app(config)

# Autenticação do Firebase
auth = firebase.auth()

# Função para criar um usuário
def create_user(email, password):
  try:
    user = auth.create_user_with_email_and_password(email, password)
    print("Usuário criado com sucesso!")
    return user
  except Exception as e:
    print("Erro ao criar usuário:", e)

# Função para fazer login
def login_user(email, password):
  try:
    user = auth.sign_in_with_email_and_password(email, password)
    print("Login realizado com sucesso!")
    return user
  except Exception as e:
    print("Erro ao fazer login:", e)

# Exemplo de uso
email = "seu_email@example.com"
password = "sua_senha"

# Criar um usuário
create_user(email, password)

# Fazer login
user = login_user(email, password)

# Imprimir o token de acesso do usuário
print("Token de acesso:", user['idToken'])