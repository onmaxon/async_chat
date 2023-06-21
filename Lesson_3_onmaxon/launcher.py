import os
import subprocess
import time

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        cmd = 'terminator -e "python server.py'
        child = subprocess.Popen(cmd,
                                        stderr=subprocess.PIPE,
                                        # stdout=subprocess.STDOUT,
                                        shell=True,
                                        # close_fds=True
                                        )

        returnCode = child.poll()
        rc = child.returncode
        print(rc)
        print(PROCESS)
        time.sleep(0.1)
        for i in range(2):
            PROCESS.append(subprocess.Popen('terminator -e "python client.py -m send"',
                                            stdout=subprocess.PIPE,
                                            stderr=None,
                                            shell=True
                                            ))
            time.sleep(0.1)
        for i in range(5):
            PROCESS.append(subprocess.Popen('terminator -e "python client.py -m listen"',
                                            stdout=subprocess.PIPE,
                                            stderr=None,
                                            shell=True))
            time.sleep(0.1)
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()