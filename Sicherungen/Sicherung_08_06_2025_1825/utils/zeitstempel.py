from datetime import datetime

def zeitstempel(typ: int) -> str:
    '''
    Gibt die aktuelle Zeit und/oder Datum aus.
    Je nach integer wird dann folgendes ausgegeben.
    1 = nur Zeit hh:mm:ss
    2 = nur Datum YYYY-MM-DD
    3 = Datum und Uhrzeit YYYY-MM-DD hh:mm:ss

    '''
    if typ == 1:
        aktuelle_zeit = datetime.now()
        zeitstempel = aktuelle_zeit.strftime("%H:%M:%S")
        return zeitstempel
    
    if typ == 2:
        aktuelle_zeit = datetime.now()
        zeitstempel = aktuelle_zeit.date()
        return zeitstempel
    
    if typ == 3:
        aktuelle_zeit = datetime.now()
        zeitstempel = aktuelle_zeit.strftime("%Y-%m-%d %H:%M:%S")
        return zeitstempel

if __name__ == "__main__":
    print(zeitstempel(3))