from datetime import date

def kw_ermitteln(datum: date) -> tuple:
    '''Gibt ein Tupel mit der Kalenderwoche und dem Wochentag
    zurück in folgendem Format: z.B. (25, '2.DI')'''
    wochentag_num = datum.weekday()  # 0 = Montag, 6 = Sonntag
    wochentage = ["1.MO", "2.DI", "3.MI", "4.DO", "5.FR", "6.SA", "7.SO"]
    wochentag = wochentage[wochentag_num]
    kalenderwoche = datum.isocalendar()[1]
    return kalenderwoche, wochentag

if __name__ == "__main__":
    kw_ermitteln()
