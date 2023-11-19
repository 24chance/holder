# this is the another calculatorApp, kinda like the test but it doesn't matter

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator0(App):
    def build(self):

        # functions; note that they always come first. I just invented that law

        # this one displays the button the very moment you clicked it
        def display_buttons(self):
            btnText = self.text
            currentText = inputField.text

            # tryna overwrite the answer and error


            # i am checking a lot of stuffs right here, just pay attention you'll get it enventually
            if (currentText and currentText[0] == "E") or (currentText and currentText[0] == "A"):
                # just checking if this shit is an operator or not
                if btnText in ['+', '-', '*', '/']:
                   pass

                else:
                    inputField.text = btnText
            else:

                # just checking if this shit is an operator or not
                if btnText in ['+', '-', '*', '/']:
                    if currentText and currentText[-1] in ['+', '-', '*', '/']:
                        inputField.text = currentText[:-1] + btnText
                    elif currentText == '':
                        pass
                    else:
                        inputField.text = currentText + btnText

                else:
                    inputField.text = currentText + btnText


        # how about we now start cleaning some stuff
        # this is the function that backspaces
        def backspacing(self):
            currentText = inputField.text

            if len(currentText) == 1:
                inputField.text = ''
            else:
                inputField.text = currentText[:-1]
        
        # enough with deleting one stuff, let's get'em all
        def cleaning(self):
            inputField.text = ''
        # easiest function so far


        # let's create a dot then
        def dotting(self):
            btnText = self.text
            currentText = inputField.text

            if not btnText in currentText:
                inputField.text = currentText + btnText


        def action(self):
            currentText = inputField.text
            try:
                inputField.text ="Answer: " + str(eval(currentText))
                
            except Exception as e:
                inputField.text = "Error"
            







        # defining the containers
        wholeLayout = BoxLayout(orientation="vertical")
        inputDiv = GridLayout(cols=4, size_hint_y=0.2)
        buttonDiv = GridLayout(cols=4)





        # creating and adding widget in the damn window


        # then here comes the input
        inputField = TextInput(multiline=False, readonly=True)
        inputDiv.add_widget(inputField)





        # these are the buttons, mostly the numbers and shit

        # these are operators
        for i in ['+', '-', '*', '/']:
            operators = Button(text=str(i))
            operators.bind(on_press=display_buttons)
            buttonDiv.add_widget(operators)

        # and these are the nbrs
        for i in range(1, 10):
            buttons = Button(text=str(i))
            buttons.bind(on_press=display_buttons)
            buttonDiv.add_widget(buttons)


        # here's the dot button (shit is harder to write than to speak)
        dot = Button(text='.')
        dot.bind(on_press=dotting)
        buttonDiv.add_widget(dot)

        # and there's the cleaning btn too
        clean = Button(text='C')
        clean.bind(on_press=cleaning)
        buttonDiv.add_widget(clean)

        # last shit gotta be the backspace button
        backspace = Button(text='B')
        backspace.bind(on_press=backspacing)
        buttonDiv.add_widget(backspace)


        # i don't know what to tell you, this btn comes from nowhere
        zero = Button(text='0')
        zero.bind(on_press=display_buttons)
        inputDiv.add_widget(zero)


        # sorry, this is the last one yet [hhhhhhh]
        equal = Button(text='=')
        equal.bind(on_press=action)
        inputDiv.add_widget(equal)


        # i am now just putting all the stuff in the window
        wholeLayout.add_widget(inputDiv)
        wholeLayout.add_widget(buttonDiv)
        return wholeLayout

# run the app
if __name__ == "__main__":
    Calculator0().run()     
