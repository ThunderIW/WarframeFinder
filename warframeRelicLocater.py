import PySimpleGUI as sg
layout=[[sg.Text("Warframe relic locater")],
        [sg.Text("Relic"),sg.Drop(values=["Test"])],
        [sg.Button("Find",tooltip="This finds the location of the relic"),sg.Button("Exit",mouseover_colors="red")]]

win1=sg.Window("TestWin",layout)

while True:
        event,value=win1.read()
        if event==sg.WINDOW_CLOSED or event=="Exit":
                break
        if event=="Find":




win1.close()
