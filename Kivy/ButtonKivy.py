import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


red= [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors= [red, green, blue, purple]
        for i in range(5):
            btn = Button(text=f'Este é o botão {i+1}', background_color=random.choice(colors))

            layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    HBoxLayoutExample().run()

#Padding = Você pode especificar os padding pixels entre o layout e seus filhos
#Para o exemplo acima, o padding é de 10 pixels. Isso significa que o layout terá 10 pixels de espaço entre ele e seus filhos.

#Spacing = Você pode adicionar espaço entre os widgets filhos com este argumento
#Para o exemplo acima, o spacing é de 10 pixels. Isso significa que os widgets filhos terão 10 pixels de espaço entre eles.

#orientation = Você pode alterar o padrão orientation de BoxLayouthorizontal para vertical
