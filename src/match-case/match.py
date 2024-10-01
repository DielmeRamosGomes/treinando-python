
def que_dia_eh(dia):
    match dia:
        case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira" | "sábado" | "domingo":
            return True
        case _:
            return False
        



