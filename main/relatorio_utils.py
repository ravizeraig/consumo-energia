def gerar_relatorio():
    import pandas as pd
    from pathlib import Path

    # Caminho do arquivo CSV
    csv_path = Path(__file__).parent.parent / 'data' / 'consumo_energia_vendas.csv'

    # Ler o arquivo CSV
    df = pd.read_csv(csv_path)

    # Criar nova coluna com o total por venda
    df['Total R$'] = df['Quantidade'] * df['Preço Unitário']

    # Agrupar os dados por cidade
    relatorio = df.groupby('Cidade').agg({
        'Total R$': 'sum',
        'Consumo (kWh)': 'sum'
    }).reset_index()

    # Ordenar por total de vendas decrescente
    relatorio = relatorio.sort_values(by='Total R$', ascending=False)

    # Caminho do arquivo de saída
    output_path = Path(__file__).parent.parent / 'data' / 'relatorio_cidade.xlsx'
    relatorio.to_excel(output_path, index=False)

    print(f'\n✅ Relatório gerado com sucesso em: {output_path}\n')
    return output_path

# Adicione esta proteção aqui 👇
if __name__ == "__main__":
    gerar_relatorio()
