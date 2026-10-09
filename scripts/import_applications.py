from pathlib import Path
import openpyxl, json, unicodedata

root=Path(__file__).resolve().parents[1]
source=root/'data'/'source'/'applications-2026.xlsx'
book=openpyxl.load_workbook(source,read_only=True,data_only=True)
existing=json.loads((root/'data'/'schools-and-addresses.json').read_text(encoding='utf-8'))
def norm(text):
    return ''.join(c for c in unicodedata.normalize('NFD',text.upper()) if not unicodedata.combining(c))
aliases={'Josinalva Santos Silva':'JOSINALVA SANTOS DA SILVA','Hamilton Alves Rocha':'HAMILTON ALVES ROCHA'}
records={}
for index,row in enumerate(book.active.iter_rows(min_row=2,values_only=True),2):
    school,class_name,shift,note,applications=row
    if school:
        current=school.strip()
        records.setdefault(current,[])
    if class_name:
        records[current].append(dict(class_name=class_name.strip(),shift=shift,applications=applications,row=index))
result=[]
for full,classes in records.items():
    matches=[s for s in existing if norm(aliases.get(s['name'],s['name'])) in norm(full)]
    if len(matches)==1:
        s=dict(matches[0])
    elif 'LOURDES TAVARES' in full:
        s=dict(name='Lourdes Tavares dos Santos',full=full,network='Municipal',address='Caípe Velho',region='Rural Pedreiras',source='https://www.saocristovao.se.gov.br/orgaos/semed?abrir_modal=true',status='Endereço do cadastro municipal')
    elif 'LUZINETE' in full:
        s=dict(name='Luzinete Teixeira Santos de Oliveira',full=full,network='Municipal',address='Unnamed Road, São Cristóvão - SE, 49100-000',region='Rural BR',source='Informado pelo usuário',status='Endereço informado pelo usuário',previous_name='Escola Municipal de Ensino Fundamental Feijão')
    else:
        raise ValueError((full,matches))
    if 'LUZINETE' in full:
        s.update(address='Unnamed Road, São Cristóvão - SE, 49100-000',region='Rural BR',source='Informado pelo usuário',status='Endereço informado pelo usuário',previous_name='Escola Municipal de Ensino Fundamental Feijão')
    s['full']=full
    s['classes']=classes
    result.append(s)
result.sort(key=lambda s:norm(s['name']))
output=root/'data'/'applications-2026.json'
output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
removed=[s['name'] for s in existing if not any(t['name']==s['name'] for t in result)]
print(json.dumps(dict(schools=len(result),classes=sum(len(s['classes']) for s in result),applications=sum(c['applications'] for s in result for c in s['classes']),removed=removed),ensure_ascii=True))
