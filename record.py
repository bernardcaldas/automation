from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
import time
import json

def record_clicks(delay):
    global last_click_time
    print(f"Gravação começará em {delay} segundos. Prepare sua tela.")

    for i in range(delay, 0, -1):
        print(f"Iniciando em {i} segundos...", end="\r")
        time.sleep(1)

    print("Iniciando gravação de cliques agora!")
    click_positions = []
    last_click_time = time.time()

    def on_click(x, y, button, pressed):
        global last_click_time
        if pressed:
            current_time = time.time()
            interval = current_time - last_click_time
            click_positions.append({"position": (x, y), "interval": interval})
            print(f"Posição registrada: {x}, {y} | Intervalo: {interval:.2f} segundos")
            last_click_time = current_time

    def on_press(key):
        if key == Key.esc:  # Encerra a gravação quando a tecla Esc é pressionada
            mouse_listener.stop()
            keyboard_listener.stop()

    # Iniciando os listeners
    with MouseListener(on_click=on_click) as mouse_listener, KeyboardListener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()

    print("Gravação encerrada.")
    print(f"Posições e intervalos registrados: {click_positions}")
    return click_positions

# Tempo de atraso antes de iniciar a gravação
initial_delay = 10  # 10 segundos, ajuste conforme necessário

click_data = record_clicks(initial_delay)

# Salvando os dados em um arquivo
with open('click_data.json', 'w') as file:
    json.dump(click_data, file)
