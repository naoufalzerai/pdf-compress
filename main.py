import PySimpleGUI as sg
import helper as h

sg.theme('TanBlue')
quality = [
    '/default',
    '/prepress',
    '/printer',
    '/ebook',
    '/screen'
]

layout = [
    [sg.T('File :'),sg.Combo(sorted(sg.user_settings_get_entry('-filenames-', [])),default_value=sg.user_settings_get_entry('-last filename-', ''),size=(50, 1),key='-FILENAME-'),sg.FileBrowse(key='-filepath-'),sg.Button('Clear History')],
    [sg.T('Quality :'),sg.Combo(quality,key="-QUALITY-")],
    [sg.Button('Compress', bind_return_key=True),  sg.Button('Exit')]
]

window = sg.Window('Filename Chooser With History', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Compress':
        sg.user_settings_set_entry(
            '-filenames-', list(set(sg.user_settings_get_entry('-filenames-', []) + [values['-FILENAME-'], ])))
        sg.user_settings_set_entry('-last filename-', values['-FILENAME-'])
        print(f"{values['-QUALITY-']}{values['-FILENAME-']}")
        h.compress(values['-FILENAME-'],values['-FILENAME-']+"_compress.pdf",values['-QUALITY-'])
    elif event == 'Clear History':
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')


window.close()
