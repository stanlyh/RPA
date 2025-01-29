import pyautogui

### Alerts ###

#a = pyautogui.alert('Revisar hay un problema', title='Advertencia')
#print(a)   #OK

### Confirm ###

#a = pyautogui.confirm('Quiere continuar??', title='Consulta')
#print(a)    #OK   Cancel

### Confirm v2 ###

a = pyautogui.confirm('Seleccione una opción', title='Opciones', buttons=['Celeste','Evangeline','Cristal','Aleli'])
print(a)