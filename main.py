from axez_gui import Handler
from axez_gui import GUI

# Event Loop to process "events" and get the "values" of the inputs

if __name__ == '__main__':
    windows_obj = GUI()
    wind_arr = windows_obj.get_windows()

    handler_obj = Handler(wind_arr[0])

    while True:
        event, values = windows_obj.read()

        handler_obj.setState(event)
        handler_obj.setValues(values)
        
        handler_obj.state_machine()

    windows_obj.close()
    