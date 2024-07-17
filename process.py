import subprocess
import os
import time
import psutil

file_path = 'archivo.txt'

process = subprocess.Popen(['notepad.exe', file_path], shell=True)

# codigo del proceso
pid_principal = process.pid

# codigo subproceso
principal_process = psutil.Process(pid_principal)

subprocesos = principal_process.children(recursive=True)

# terminar multiples subprocesos
for subproceso in subprocesos:
    try:
        subproceso.terminate()
    except psutil.NoSuchProcess:
        pass