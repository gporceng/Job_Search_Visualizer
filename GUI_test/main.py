from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

#Window.clearcolor = (.0059,63,255,255)
class JobSearch(App):
    def build(self):
        #returns a window object with all it's widgets

        self.title = 'Job Search Visualizer - By Gregory Porceng'
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.95, 0.85)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.50}
        self.window.padding = [0,-45]

        

        # image widget
        self.window.add_widget(Image(
                        source="logo.png",))

        # Adding a Text box enviorment

        #Overall container
        overall_layout = GridLayout(cols =2)
        layout = GridLayout(cols = 2)
        checkbox = GridLayout(rows = 2)
        
        #Text input
        #Waiting text input
        layout.add_widget(Label(                        
                    text= "Waiting",
                    font_size= 20,
                    halign="left",
                    valign="middle",
                    size_hint = (2,0.5),
                    color= '#554dff'))
        
        layout.add_widget(TextInput(
                    multiline= False,
                    size_hint= (2.5, 0.01),
                    line_height = 0))

        
        #Accepted text input
        layout.add_widget(Label(                        
                    text= "Accepted",
                    font_size= 20,
                    size_hint = (1,0.5),
                    color= '#554dff'))
        
        layout.add_widget(TextInput(
                    multiline= False,
                    size_hint= (2.5, 0.01),
                    line_height = 0))

        
        #First Interview text input
        layout.add_widget(Label(                        
                    text= "1st Interview",
                    font_size= 20,
                    size_hint = (1,0.5),
                    color= '#554dff'))
        
        layout.add_widget(TextInput(
                    multiline= False,
                    size_hint= (2.5, 0.01),
                    line_height = 0))

        
        #Waiting text input
        layout.add_widget(Label(                        
                    text= "Waiting",
                    font_size= 20,
                    size_hint = (1,0.5),
                    color= '#554dff'))
        
        layout.add_widget(TextInput(
                    multiline= False,
                    size_hint= (2.5, 0.01),
                    line_height = 0))

        
        #Accepted text input
        layout.add_widget(Label(                        
                    text= "Accepted",
                    font_size= 20,
                    size_hint = (1,0.5),
                    color= '#554dff'))
        
        layout.add_widget(TextInput(
                    multiline= False,
                    size_hint= (2.5, 0.01),
                    line_height = 0))

        
        #First Interview text input
        layout.add_widget(Label(                        
                    text= "1st Interview",
                    font_size= 20,
                    size_hint = (1,0.5),
                    color= '#554dff'))
        
        layout.add_widget(TextInput(
                    multiline= False,
                    size_hint= (2.5, 0.01),
                    line_height = 0))


        # Add checkbox layout]
        checkbox.add_widget(Label(text = "Box Chart"))
        boxChart_check = CheckBox()
        checkbox.add_widget(boxChart_check)
        checkbox.add_widget(Label(text = "Waffle Chart"))
        waffleChart_check = CheckBox()
        checkbox.add_widget(waffleChart_check)

        #Add to containers in the correct order
        overall_layout.add_widget(layout)
        overall_layout.add_widget(checkbox)
        self.window.add_widget(overall_layout)

        #Add Run button
        self.button = Button(
                      text= "Run",
                      size_hint= (.1,0.2),
                      bold= True,
                      background_color ='#ff9c9c',
                      
                      #remove darker overlay of background colour
                      background_normal = ""
                      )
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Hello " + self.user.text + "!"

# run
if __name__ == "__main__":
    JobSearch().run()
