"""Forza 4 per due giocatori, giocabile nel terminale."""

RIGHE = 6
COLONNE = 7


def nuova_griglia() -> list[list[str]]:
    """Crea una griglia vuota di 6 righe e 7 colonne."""
    pass


def disegna_griglia(griglia: list[list[str]]) -> None:
    """Stampa la griglia con le colonne numerate da 1 a 7."""
    pass


def chiedi_colonna(giocatore: str) -> int:
    """Chiede la colonna finché non viene inserito un numero valido."""
    pass


def inserisci_gettone(griglia: list[list[str]], colonna: int, giocatore: str) -> int:
    """Posiziona il gettone e restituisce la riga, oppure -1 se la colonna è piena."""
    pass


def controlla_vittoria(
    griglia: list[list[str]], giocatore: str, riga: int, colonna: int
) -> bool:
    """True se la pedina appena posizionata completa quattro in fila."""
    pass


def conta_spazi(griglia: list[list[str]]) -> int:
    """Quante celle della griglia sono ancora vuote."""
    pass

