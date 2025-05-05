# ProjektPSS_RFIDctecka

Tento projekt implementuje jednoduchý systém pro evidenci docházky pomocí RFID čtečky.  
Uživatelé přikládají své RFID karty nebo čipy ke čtečce, systém zaznamenává jejich přítomnost a zobrazuje aktuální stav docházky ve webovém rozhraní.

## Struktura projektu

Projekt se skládá z několika základních součástí:

- `rfid_system.py` – Hlavní Python skript, který komunikuje s RFID čtečkou a zpracovává načtená data.
- `prezence.txt` – Textový soubor, do kterého se zapisují záznamy o příchodu uživatelů.
- `templates/` – HTML šablony pro webové rozhraní (např. hlavní přehled docházky).
- `static/` – Statické soubory, například CSS pro stylování webu.

## Požadavky

K běhu projektu potřebujete:

- Python 3.x
- Nainstalované knihovny:
  - `Flask` – pro webové rozhraní
  - `pyserial` – pro komunikaci s RFID čtečkou přes sériový port
- Kompatibilní RFID čtečku (např. USB RFID čtečka 13,56MHz)

##  Instalace a spuštění

1. Klonujte repozitář:

   ```bash
   git clone https://github.com/Se8o/ProjektPSS_RFIDctecka.git
   cd ProjektPSS_RFIDctecka

2. Nainstalujte požadované Python knihovny:
   
  ```bash
   pip install flask pyserial
  ```

3. Připojte RFID čtečku k počítači přes USB. Zjistěte název sériového portu (např. COM3 pro Windows nebo /dev/ttyUSB0 pro Linux).
4. Otevřete soubor rfid_system.py a upravte port:

 ```bash
  ser = serial.Serial('COM3', 9600)  # Změňte COM3 podle potřeby
 ```

5. Spusťte systém:

  ```bash
  python rfid_system.py
  ```
6. V prohlížeči přejděte na adresu http://localhost:5000, kde se zobrazí aktuální seznam přítomných uživatelů.

## Formát souboru prezence.txt

Záznamy v souboru prezence.txt mají tento formát:
```bash
YYYY-MM-DD HH:MM:SS - ID_karty
```
Například:
```bash
2025-05-05 08:30:00 - 1234567890
```


