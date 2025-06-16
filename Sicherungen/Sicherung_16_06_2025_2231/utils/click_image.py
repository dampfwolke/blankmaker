from pyautogui import locateCenterOnScreen, click
from time import sleep, time

# Bildpfad
bauteil_pfad = "C:\\Users\\hasanovic\\Desktop\\Blank_Master_6.6\\bilder\\bauteil.png"

def click_image(image_path, toleranz:float) -> None:
    start_time = time()
    while True:
        position = locateCenterOnScreen(image_path, confidence=toleranz,grayscale=True)
        if position or time() - start_time > 2:
            break
    if position:
        x, y = position
        click(x, y)
        print("Bild gefunden")
        sleep(0.12)

if __name__ == "__main__":
    click_image(bauteil_pfad, toleranz=0.65)
