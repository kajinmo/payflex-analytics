import pandas as pd

def ler_csv(filepath, delimiter=',', encoding='utf-8', **kwargs):
    """
    Lê um arquivo CSV e retorna um DataFrame do Pandas.
    """
    try:
        df = pd.read_csv(
            filepath_or_buffer=filepath,
            delimiter=delimiter,
            encoding=encoding,
            **kwargs
        )
        print(f"Arquivo '{filepath}' lido com sucesso!")
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filepath}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None