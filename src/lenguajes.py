def prefijos(cadena: str) -> list[str]:
    return [cadena[:i] for i in range(len(cadena) + 1)]
