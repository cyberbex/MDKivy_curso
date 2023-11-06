from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

Window.size=(380,640)
class MI(BoxLayout):
    def lefter(self,Instance):
        print("Left pressed",Instance.text)
    
    def righter(self,Instance):
        print("Right pressed",Instance.text)

class MyApp(MDApp):

    def maker(self):
        password = self.root.ids.password.text
        print(password)
    def build(self):
        self.theme_cls.primary_palette="Teal"
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.accent_palette="Orange"
        return 0


MyApp().run()

