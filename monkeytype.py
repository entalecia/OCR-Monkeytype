import pyscreenshot as ImageGrab
import time
import pytesseract
import pyautogui as pg

three_lines = (82, 350, 1268, 480) # X1,Y1,X2,Y2 for all three lines
last_line = (82, 433, 1268, 480)  #XI,Y1,X2,Y2 for the last line

def take_screenshot(i: int) -> ImageGrab:
    if i == 0:
        time.sleep(2)
        im1 = ImageGrab.grab(bbox=three_lines) 
    else:
        im1 = ImageGrab.grab(bbox=last_line)
    return im1
    

def ocr(im) -> str: #Image to Text
    return pytesseract.image_to_string(im).strip()

def typedis(string: str, i: int) -> None: #Text to Keyboard
    if i == 1:
        string = " " + string
    pg.write(string, interval=0.01)

    
def main(i: int):
    im = take_screenshot(i)
    ocr_text = ocr(im)
    ocr_text = (ocr_text.replace("\n", " ")).replace("I", "") #probability of reading Cursor as I
    typedis(ocr_text, i)
    

if __name__ == "__main__":
    sec = int(input("How long is the time?: "))
    s = time.time()
    i = 0
    while (int(time.time() - s)) < sec + 1:
        main(i)
        i = 1