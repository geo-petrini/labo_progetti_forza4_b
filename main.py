from forza4 import (
    chiedi_colonna,
    conta_spazi,
    controlla_vittoria,
    disegna_griglia,
    inserisci_gettone,
    nuova_griglia,
)


def main() -> None:
    griglia = nuova_griglia()
    giocatore = "X"
    print("=== FORZA 4 === due giocatori: quattro in fila vince")
    while True:
        disegna_griglia(griglia)
        colonna = chiedi_colonna(giocatore)
        riga = inserisci_gettone(griglia, colonna, giocatore)
        if riga == -1:
            print("  Colonna piena: scegli una colonna diversa.")
            continue
        if controlla_vittoria(griglia, giocatore, riga, colonna - 1):
            disegna_griglia(griglia)
            print(f"  VITTORIA del giocatore {giocatore}!")
            break
        if conta_spazi(griglia) == 0:
            disegna_griglia(griglia)
            print("  Pareggio: la griglia è piena.")
            break
        giocatore = "O" if giocatore == "X" else "X"


if __name__ == "__main__":
    main()

