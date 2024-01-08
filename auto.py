import pyautogui
import time
import json

def execute_clicks(click_data, delay, repetitions):
    print(f"A automação começará em {delay} segundos. Prepare sua tela.")
    for i in range(delay, 0, -1):
        print(f"Iniciando em {i} segundos...", end="\r")
        time.sleep(1)

    print("Iniciando automação agora!")
    for rep in range(repetitions):
        for click_info in click_data:
            position = click_info["position"]
            interval = click_info["interval"]
            time.sleep(interval)
            pyautogui.click(position[0], position[1])
        print(f"Sequência {rep + 1} de {repetitions} concluída.")

# Tempo de atraso antes de iniciar a automação e número de repetições
initial_delay = 10  # Ajuste conforme necessário
print("Quantas vezes deseja repetir a sequência gravada?")
repetitions = int(input("Digite o número de repetições: "))

# Lendo os dados do arquivo
with open('click_data.json', 'r') as file:
    click_data = json.load(file)

execute_clicks(click_data, initial_delay, repetitions)
