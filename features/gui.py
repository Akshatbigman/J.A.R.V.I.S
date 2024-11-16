import PySimpleGUI as sg

def create_window():
    layout = [
        [sg.Text("Conversation Log", size=(50, 1), font='Any 20', text_color='white', background_color='black')],
        [sg.Multiline(size=(80, 20), key='-CHAT-', font='Any 12', text_color='white', background_color='black', disabled=True, border_width=0)],

        [sg.Text('', size=(1, 1), background_color='black')],
        
        [sg.Button('Run', size=(10, 1), button_color=('white', 'grey'), border_width=0, pad=((0, 10), (0, 0))),
         sg.Button('Exit', size=(10, 1), button_color=('white', 'grey'), border_width=0)],
        
        [sg.Text('', size=(1, 1), background_color='black')]
    ]

    window = sg.Window('Jarvis', layout, background_color='black', resizable=True, finalize=True)

    for button in window.AllButtons:
        button.Widget.config(borderwidth=0, relief='flat')
        button.Widget.config(highlightbackground='grey', highlightcolor='grey')

    return window

def main():
    window = create_window()

    while True:
        event, values = window.read(timeout=1000)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Run':
            window['-CHAT-'].update(value="Jarvis: Running tasks...\n", append=True)

        from datetime import datetime
        now = datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')

    window.close()

if __name__ == "__main__":
    main()
 