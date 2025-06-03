from datetime import datetime

def kw_ermitteln() -> tuple:
    '''Gibt ein Tupel mit der Kalenderwoche und dem Wochentag
    zurück in folgendem Format: z.B. (25, '2.DI')'''
    # Aktuelles Datum und Zeit abrufen
    aktueller_zeitpunkt = datetime.now()
    # Wochentag ermitteln (0 = Montag, 6 = Sonntag)
    wochentag_num = aktueller_zeitpunkt.weekday()
    wochentage = ["1.MO", "2.DI", "3.MI", "4.DO", "5.FR", "6.SA", "7.SO"]
    wochentag = wochentage[wochentag_num]
    # Kalenderwoche ermitteln
    kalenderwoche = aktueller_zeitpunkt.isocalendar()[1]
    return kalenderwoche, wochentag

if __name__ == "__main__":
    testpfad = f"K:\\Esprit\\NC-Files\\AT-25-KW{kw_ermitteln()[0]}\\Hasanovic\\{kw_ermitteln()[1]}"
    kw_ermitteln()
    print(testpfad)