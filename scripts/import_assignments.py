from datetime import date, datetime, time
import json
from pathlib import Path
import unicodedata

from openpyxl import load_workbook


root = Path(__file__).resolve().parents[1]
source = root / 'data' / 'source' / 'Consolidado_Escolas_Aplicadores.xlsx'
data_path = root / 'data' / 'applications-2026.json'
required_headers = (
    'Escola',
    'Data',
    'Turno',
    'Horário',
    'Turma',
    'Nome do aplicador',
    'Função',
)


def normalize(value):
    normalized = unicodedata.normalize('NFD', value.casefold())
    return ''.join(
        character
        for character in normalized
        if unicodedata.category(character) != 'Mn' and character.isalnum()
    )


def required_text(value, field, row_number):
    if value is None or not str(value).strip():
        raise ValueError(f'Linha {row_number}: campo obrigatório vazio: {field}')
    return str(value).strip()


def application_date(value, row_number):
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    try:
        return datetime.strptime(str(value).strip(), '%d/%m/%Y').date().isoformat()
    except ValueError as error:
        raise ValueError(
            f'Linha {row_number}: data inválida: {value!r}'
        ) from error


def application_time(value, row_number):
    if isinstance(value, (datetime, time)):
        return value.strftime('%H:%M')
    text = required_text(value, 'Horário', row_number)
    try:
        return datetime.strptime(text, '%H:%M').strftime('%H:%M')
    except ValueError as error:
        raise ValueError(
            f'Linha {row_number}: horário inválido: {value!r}'
        ) from error


def main():
    schools = json.loads(data_path.read_text(encoding='utf-8'))
    by_full_name = {}
    for school in schools:
        key = normalize(school['full'])
        if key in by_full_name:
            raise ValueError(f'Nome de escola duplicado nos dados: {school["full"]}')
        by_full_name[key] = school
        school['assignments'] = []

    workbook = load_workbook(source, read_only=True, data_only=True)
    try:
        if 'Resumo' not in workbook.sheetnames:
            raise ValueError(f'A planilha não contém a aba "Resumo": {source}')
        rows = workbook['Resumo'].iter_rows(values_only=True)
        headers = next(rows, None)
        if headers is None or tuple(headers) != required_headers:
            raise ValueError(
                f'Cabeçalhos inesperados na planilha: {headers!r}; '
                f'esperado: {required_headers!r}'
            )

        imported = 0
        for row_number, row in enumerate(rows, start=2):
            school_name = required_text(row[0], 'Escola', row_number)
            school = by_full_name.get(normalize(school_name))
            if school is None:
                raise ValueError(
                    f'Linha {row_number}: escola não encontrada em '
                    f'applications-2026.json: {school_name!r}'
                )
            school['assignments'].append(
                {
                    'date': application_date(row[1], row_number),
                    'shift': required_text(row[2], 'Turno', row_number),
                    'time': application_time(row[3], row_number),
                    'class_name': required_text(row[4], 'Turma', row_number),
                    'applicator': required_text(
                        row[5], 'Nome do aplicador', row_number
                    ).upper(),
                    'function': required_text(row[6], 'Função', row_number),
                }
            )
            imported += 1
    finally:
        workbook.close()

    if imported == 0:
        raise ValueError(f'Nenhuma atribuição encontrada na planilha: {source}')

    for school in schools:
        school['assignments'].sort(
            key=lambda assignment: (
                assignment['date'],
                assignment['time'],
                assignment['class_name'],
                assignment['applicator'].casefold(),
            )
        )

    data_path.write_text(
        json.dumps(schools, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )
    print(f'Escolas: {len(schools)}; atribuições importadas: {imported}')


if __name__ == '__main__':
    main()
