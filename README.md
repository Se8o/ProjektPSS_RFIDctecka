ProjektPSS_RFIDctecka
Tento projekt implementuje jednoduchý systém pro evidenci docházky pomocí RFID čtečky. Uživatelé přikládají své RFID karty nebo čipy ke čtečce, systém zaznamenává jejich přítomnost a zobrazuje aktuální stav docházky ve webovém rozhraní.

 Struktura projektu
rfid_system.py – Hlavní Python skript, který komunikuje s RFID čtečkou a zpracovává data.

prezence.txt – Textový soubor, do kterého se ukládají záznamy o přítomnosti uživatelů.

templates/ – Složka obsahující HTML šablony pro webové rozhraní.

static/ – Složka s CSS styly a případnými statickými soubory pro frontend.

 Požadavky
Python 3.x

Knihovny:

Flask – pro webové rozhraní

pyserial – pro komunikaci s RFID čtečkou přes sériový port

RFID čtečka kompatibilní se sériovým rozhraním (např. USB RFID čtečka 13,56MHz)
laskakit.cz
+8
Root.cz
+8
Papouch
+8
dratek.cz
+1
dratek.cz
+1

Instalace a spuštění
Klonování repozitáře:

bash
Zkopírovat
Upravit
git clone https://github.com/Se8o/ProjektPSS_RFIDctecka.git
cd ProjektPSS_RFIDctecka
Instalace závislostí:

bash
Zkopírovat
Upravit
pip install flask pyserial
Připojení RFID čtečky:

Připojte RFID čtečku k počítači přes USB port. Zjistěte, na kterém portu je zařízení připojeno (např. /dev/ttyUSB0 na Linuxu nebo COM3 na Windows).

Úprava skriptu:

V souboru rfid_system.py upravte název sériového portu podle vašeho systému:

python
Zkopírovat
Upravit
ser = serial.Serial('COM3', 9600)  # Nahraďte 'COM3' správným portem
Spuštění aplikace:

bash
Zkopírovat
Upravit
python rfid_system.py
Přístup k webovému rozhraní:

Otevřete webový prohlížeč a přejděte na adresu http://localhost:5000, kde uvidíte aktuální stav docházky.

Formát souboru prezence.txt
Každý řádek v souboru prezence.txt reprezentuje jeden záznam o přítomnosti uživatele ve formátu:

css
Zkopírovat
Upravit
[časový_údaj] - [ID_karty]
Například:

yaml
Zkopírovat
Upravit
2025-05-05 08:30:00 - 1234567890
Testování
Pro otestování systému přiložte RFID kartu nebo čip ke čtečce. Pokud je vše správně nastaveno, systém zaznamená přítomnost a aktualizuje webové rozhraní.

 Poznámky
Ujistěte se, že máte nainstalované všechny potřebné ovladače pro vaši RFID čtečku.

Při spuštění aplikace se ujistěte, že žádný jiný program nepoužívá stejný sériový port.

Pro běh aplikace může být potřeba mít administrátorská práva, zejména při přístupu k sériovým portům.
