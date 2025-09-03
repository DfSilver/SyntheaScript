
import pandas as pd
from ctgan import CTGAN

INPUT_PATH = "Files/output/df_sinfaltantes.csv"
OUTPUT_PATH = "Files/output/data_syntetic.csv"
NUM_RECORDS = 2000



def main():
    # Leer el archivo de referencia con delimitador ;
    df = pd.read_csv(INPUT_PATH, sep=';', encoding='utf-8')

    # Detectar columnas categóricas (tipo object)
    discrete_columns = df.select_dtypes(include=['object']).columns.tolist()

    # Entrenar el modelo CTGAN
    model = CTGAN()
    model.fit(df, discrete_columns=discrete_columns)

    # Generar datos sintéticos
    synthetic_data = model.sample(NUM_RECORDS)

    # Guardar el resultado con el mismo delimitador ;
    synthetic_data.to_csv(OUTPUT_PATH, sep=';', index=False, encoding='utf-8')

if __name__ == "__main__":
    main()
