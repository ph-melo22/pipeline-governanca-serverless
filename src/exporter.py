import pandas as pd
import os
from datetime import datetime
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font, Alignment

def adjust_columns(worksheet):
    """Ajusta a largura das colunas do Excel automaticamente."""
    for col in worksheet.columns:
        max_length = 0
        column = col[0].column_letter # Nome da coluna (A, B, C...)
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        worksheet.column_dimensions[column].width = adjusted_width

def style_header(worksheet):
    """Aplica negrito na primeira linha."""
    for cell in worksheet[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')

def export_to_excel(df_summary: pd.DataFrame, df_ranking: pd.DataFrame, df_categories: pd.DataFrame, output_dir: str) -> str:
    """
    Gera o arquivo Excel com 3 abas e aplica estilização básica.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    date_str = datetime.now().strftime('%Y-%m-%d')
    file_name = f"relatorio_{date_str}.xlsx"
    file_path = os.path.join(output_dir, file_name)

    # Usando o Pandas ExcelWriter com o engine openpyxl
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df_summary.to_excel(writer, sheet_name='Resumo Executivo', index=False)
        df_ranking.to_excel(writer, sheet_name='Ranking Analistas', index=False)
        df_categories.to_excel(writer, sheet_name='Por Categoria', index=False)

    # Acessar o workbook diretamente para ajustes visuais
    import openpyxl
    wb = openpyxl.load_workbook(file_path)
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        adjust_columns(ws)
        style_header(ws)
        
    wb.save(file_path)
    return file_path
