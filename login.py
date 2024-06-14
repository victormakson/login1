from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image ,AsyncImage
from functools import partial
from kivy.uix.modalview import ModalView
import pyrebase

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
firebase = pyrebase.initialize_app(config)

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

# Função para criar um usuário no Realtime Database
def create_user_in_db(user):
  db = firebase.database()
  data = {
    "nome": "Seu Nome",
    "email": user["email"]
  }
  db.child("usuarios").child(user["uid"]).set(data)
  print("Usuário criado no Realtime Database com sucesso!")

# Exemplo de uso
email = "seu_email@example.com"
password = "sua_senha"

# Criar um usuário
user = create_user(email, password)
if user:
  # Criar um usuário no Realtime Database
  create_user_in_db(user)


Window.size = 360, 640

class Login(BoxLayout):
    def __init__(self, arg1=None, arg2=None, **kwargs):
        Window.clearcolor = get_color_from_hex("#ffffff")
        super().__init__(**kwargs)
        self.arg1 = arg1
        self.arg2 = arg2
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10


        self.add_widget(Image(source=('icone.jpeg'), size=(700, 700)))
        self.add_widget(Label(text="Login", font_size=50, font_name='Impact', color=get_color_from_hex('#000000')))
        self.add_widget(Label(text="Faça o seu login!", font_size=20, font_name='Arial', color=get_color_from_hex('#000000')))
        


        self.username_input = TextInput(hint_text="Digite seu Email ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        

        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.add_widget(self.senha_input)
        
        
        self.cadastrar_button = Button(text="Entrar", background_color=get_color_from_hex('#5e2129'))
        
        self.add_widget(self.cadastrar_button)
        

    def create_new_window(self, arg1, arg2, instance):
            new_window = NewWindow(arg1, arg2)
            new_window.open()
            Window.clearcolor = (1, 1, 1, 1)

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()



class NewWindow(BoxLayout):
    def init(self, arg1, arg2, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super().init(**kwargs)
        self.arg1 = 'value1'
        self.arg2 = 'value2'
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('##e6e5ee')))

        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.email_input = TextInput(hint_text="Digite seu email ...")
        self.celular_input = TextInput(hint_text="Digite o número do seu celular ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Celular:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.celular_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=(0, 0, 1))
        self.button_cadastrar.bind(on_release=partial(self.entrar_interface_login, self.arg1, self.arg2))
        self.add_widget(self.button_cadastrar)

    def entrar_interface_login(self, arg1, arg2, instance):
            entrar_login = Login(arg1, arg2)
            entrar_login.open()
            Window.clearcolor = (1, 1, 1, 1)


    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()