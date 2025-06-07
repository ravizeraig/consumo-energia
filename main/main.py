from main.relatorio_utils import gerar_relatorio


import sys

def main():
    gerar_relatorio()
    from main.enviar_email import enviar_relatorio
    enviar_relatorio()
    print("✅ Relatório enviado. Finalizando execução.")
    sys.exit(0)  # <-- encerra o processo com sucesso

if __name__ == "__main__":
    main()


