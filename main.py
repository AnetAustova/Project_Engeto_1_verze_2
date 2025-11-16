# Seznam pro ukládání úkolů
ukoly = []


def hlavni_menu():
    """
    Zobrazuje hlavní menu a zpracovává volbu uživatele.
    Umožňuje přidání, zobrazení a odstranění úkolů, nebo ukončení programu.
    """
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ")

        if volba == '1':
            pridat_ukol()
        elif volba == '2':
            zobrazit_ukoly()
        elif volba == '3':
            odstranit_ukol()
        elif volba == '4':
            print("Program byl ukončen. Děkujeme za použití Správce úkolů.")
            break
        else:
            print("Neplatná volba. Zadejte prosím číslo od 1 do 4.")

ukoly = []

def pridat_ukol():
    """
    Přidá nový úkol s názvem a popisem do seznamu 'ukoly'.
    Uživatel musí zadat oba údaje – název i popis – jinak bude znovu vyzván.
    """
    while True:
        nazev = input("Zadejte název nového úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        # Pokud jsou oba vstupy neprázdné, úkol se uloží
        novy_ukol = {
            "Název": nazev,
            "Popis": popis
        }
        ukoly.append(novy_ukol)
        print(f"Úkol '{nazev}' byl úspěšně přidán.")
        break


def zobrazit_ukoly():
    """
    Zobrazí všechny úkoly v seznamu s indexy pro snadnější identifikaci.
    """
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\n--- Seznam úkolů ---")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol}")
        print("--------------------")


def odstranit_ukol():
    """
    Umožní uživateli odstranit úkol podle jeho pořadového čísla ze seznamu.
    """
    if not ukoly:
        print("Nelze odstranit. Seznam úkolů je prázdný.")
        return

    zobrazit_ukoly()

    while True:
        try:
            cislo_ukolu = input("Zadejte číslo úkolu, který chcete odstranit (pro zrušení zadejte 0): ")

            if cislo_ukolu == '0':
                print("Odstranění úkolu zrušeno.")
                return

            # Převedení vstupu na celé číslo a kontrola rozsahu
            index_k_odstraneni = int(cislo_ukolu) - 1

            if 0 <= index_k_odstraneni < len(ukoly):
                odstraneny_ukol = ukoly.pop(index_k_odstraneni)
                print(f"Úkol '{odstraneny_ukol}' byl úspěšně odstraněn.")
                break
            else:
                print("Neplatné číslo úkolu. Zkuste to prosím znovu.")
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.")

print("Správce úkolů - Hlavní Menu")
hlavni_menu()