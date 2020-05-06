import PySimpleGUI as sg
import axez

class GUI():
    def __init__(self, theme='DarkTeal2'):
        sg.theme(theme)
        window_menu = [['File', ['Exit',]],['Help', ['About...', 'Help', 'Formulas used'],]]
        self.layout = [  [sg.Menu(window_menu)],
                [sg.Text('LINEAR EXPRESSION SOLVER')],
                [sg.Text('EXPRESSION :'), sg.InputText(do_not_clear=False, size=(10,1))],
                [sg.Button('SOLVE')] 
            ]

    def create_windows(self):
    # Create the Window
        self.window = sg.Window('Integrals solver', self.layout, icon='integral.ico', size=(380,180))
    
    def get_windows(self):
        self.create_windows()
        return (self.window)

    def read(self):
        return self.window.read()

    def close(self):
        return self.window.close()

class Handler:

    def __init__(self, *window):
        self.window = window
        print(window)

    def setState(self, state):
        self.state = state

    def setValues(self, values):
        self.values = values

    def state_machine(self):
        
        if self.state == 'SOLVE':
            self.solve()

        elif self.state in (None, 'Exit'):
            exit()
        elif self.state == 'About...':
            sg.Popup('EXPRESSION SHITTER by Pavlo Chaikovskyi 100500B')  
        elif self.state == 'Help':
            sg.Popup('HELPER', 'helps you out')

    def solve(self):
        if '' not in self.values.values():
            print(self.values.values())
            #result = axez.solver([self.values[1])
            axez.solver(self.values[1])
        else:
            sg.Popup('Opps!', 'One of the fields is empty.')