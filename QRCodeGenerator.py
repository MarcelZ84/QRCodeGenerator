#Dies ist ein Pythonscript zum Erstellen von farbigen QR-Codes.
#Die Größe und die Fehlerkorrektur sind einstellbar.
#Es werden die Dateiformate PNG, BMP und JPEG unterstützt.

import qrcode
import os

#Eingabe der Daten die im QR-Code enthalten sein sollen
daten = input("Daten für den QR-Code: ")

#erstellen
while True:
    try:
        grroesseQRCode = int(input("Größe des QR-Codes: "))
        break
    except ValueError:
        print("Ungültige Eingabe, geben Sie eine Zahl ein!")

#Auswahl Fehlerkorrektur
while True:
    fehlerKorrektur = input("Fehlerkorrekturstufe: (L, M, Q, H): ")
    if fehlerKorrektur in ["L", "M", "Q", "H"]:
        break

#pruefe Fehlerkorrektur
if fehlerKorrektur == "L":
    error_correction = qrcode.constants.ERROR_CORRECT_L
elif fehlerKorrektur == "M":
    error_correction = qrcode.constants.ERROR_CORRECT_M
elif fehlerKorrektur == "Q":
    error_correction = qrcode.constants.ERROR_CORRECT_Q
else:
    error_correction = qrcode.constants.ERROR_CORRECT_H


qr = qrcode.QRCode(version=1, error_correction=error_correction, box_size=grroesseQRCode, border=2)

qr.add_data(daten)
qr.make(fit=True)

while True:
    try:
        farbe = int(input("Welche Farbe soll der QR-Code haben? 1: rot, 2: grün, 3: blau, 4: schwarz \n"+
                    ": "))
        break
    except ValueError:
        print("Ungültige Eingabe, geben Sie eine Zahl ein!")

#pruefe Farbe
if(farbe == 1):
    farbeQR = "red"
elif(farbe == 2):
    farbeQR = "green"
elif(farbe == 3):   
    farbeQR = "blue"    
else:
    farbeQR = "black"   

bild = qr.make_image(fill_color=farbeQR, back_color="white")

#Eingabe Dateiname
dateiName = input("Dateiname: ")

print("Datei-Endung: \n"+
        "1: PNG, 2: BMP, 3: JPEG")
while True:
    try:
        dateiEndung = int(input("Dateiformat: "))
        if(dateiEndung < 1  or dateiEndung > 4):
            continue
        break
    except ValueError:
        print("Ungültige Eingabe, geben Sie eine Zahl ein!")

#pruefe Dateiendung
if(dateiEndung == 1):
    endung = ".png"
elif(dateiEndung == 2):
    endung = ".bmp"
else:
    endung = ".jpg"
#speichern
bild.save(dateiName + endung)

#pruefen ob die Bilddatei gespeichert wurde
if os.path.exists(dateiName + endung):
    print("Der QR-Code wurde erfolgreich erstellt und gespeichert.")
else:
    print("Der QR-Code konnte nicht erstellt werden.")

input()