from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

Window.size=(480,800)
class MI(Screen):
    def lefter(self,Instance):
        print("Left pressed",Instance.text)
    
    def righter(self,Instance):
        print("Right pressed",Instance.text)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Amber"
        self.theme_cls.theme_style= "Dark"
        return 0


MyApp().run()

