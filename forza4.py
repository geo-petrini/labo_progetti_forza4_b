"""Forza 4 per due giocatori, giocabile nel terminale."""

RIGHE = 6
COLONNE = 7


def nuova_griglia() -> list[list[str]]:
    """Crea una griglia vuota di 6 righe e 7 colonne."""
    return [[" " for _ in range(COLONNE)] for _ in range(RIGHE)]


def disegna_griglia(griglia: list[list[str]]) -> None:
    """Stampa la griglia con le colonne numerate da 1 a 7."""
    bordo_sup    =  " ┌" + "┬".join(["───"] * COLONNE) + "┐"
    bordo_interno = " ├" + "┼".join(["───"] * COLONNE) + "┤"
    bordo_inf    =  " └" + "┴".join(["───"] * COLONNE) + "┘"
    print()
    print("  " + "   ".join(str(n) for n in range(1, COLONNE + 1)))
    print(bordo_sup)
    for i, riga in enumerate(griglia):
        print(" │" + "│".join(f" {c} " for c in riga) + "│")
        if i < len(griglia) -1:
            print(bordo_interno)
    print(bordo_inf)
    print()


def chiedi_colonna(giocatore: str) -> int:
    """Chiede la colonna finché non viene inserito un numero valido."""
    while True:
        scelta = input(f"Giocatore {giocatore}, scegli la colonna (1-{COLONNE}): ").strip()
        if not scelta.isdigit():
            print(f"  {scelta} non è un numero: serve una colonna da 1 a {COLONNE}.")
            continue
        colonna = int(scelta)
        if colonna < 1 or colonna > COLONNE:
            print(f"  Colonna {colonna} fuori range: serve da 1 a {COLONNE}.")
            continue
        return colonna


def inserisci_gettone(griglia: list[list[str]], colonna: int, giocatore: str) -> int:
    """Posiziona il gettone e restituisce la riga, oppure -1 se la colonna è piena."""
    c = colonna - 1
    for r in range(RIGHE - 1, -1, -1):
        if griglia[r][c] == " ":
            griglia[r][c] = giocatore
            return r
    return -1


def controlla_vittoria(
    griglia: list[list[str]], giocatore: str, riga: int, colonna: int
) -> bool:
    """True se la pedina appena posizionata completa quattro in fila."""
    pass


def conta_spazi(griglia: list[list[str]]) -> int:
    """Quante celle della griglia sono ancora vuote."""
    return sum(cella == " " for riga in griglia for cella in riga)

