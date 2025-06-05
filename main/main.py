from main.relatorio_utils import gerar_relatorio


def main():
    # Gerar relatório
    gerar_relatorio()

    # Importação atrasada para evitar erro de importação circular
    from main.enviar_email import enviar_relatorio

    # Enviar e-mail
    enviar_relatorio()

if __name__ == "__main__":
    main()

