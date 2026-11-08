# SAESE 2026 | Polo São Cristóvão

Portal responsivo de consulta para aplicadores do Sistema de Avaliação da Educação Básica de Sergipe (SAESE) no Polo São Cristóvão. Reúne escolas, endereços, turmas, turnos, cronograma e orientações para as aplicações de 2026.

**[Abrir o portal publicado](https://paulo-carvalho01.github.io/saese.polosaocristovao/)**

> No GitHub, clicar em `site/index.html` mostra o código-fonte HTML. Esse é o comportamento normal do visualizador de arquivos do GitHub. Para usar o portal, abra o link publicado acima ou o campo **Website** no painel About do repositório.

## Funcionalidades

- Busca de escolas por nome, endereço, região, turma ou nome do aplicador e filtro por rede.
- Fichas com endereço, mapa por busca, rota e escala por turma: data, turno, horário, aplicador e função.
- Busca por nome anterior quando isso ajuda a identificar uma escola.
- Cronograma de aplicação, com orientações aos aplicadores.
- Endereços em HTML estático para leitores que bloqueiam JavaScript; busca e filtros interativos precisam de JavaScript.
- Layout responsivo para celular e computador.

A relação contém 37 escolas. A planilha de turmas registra 148 linhas e 192 aplicações; a escala de aplicadores contém 392 atribuições. Confirme sua convocação individual. Mapas são buscas por nome/endereço, não coordenadas verificadas.

## Estrutura

```text
.
├── .github/workflows/pages.yml       # Publica site/ no GitHub Pages
├── assets/                            # Imagens-fonte usadas pelo gerador
├── data/
│   ├── applications-2026.json         # Escolas, turmas, turnos e aplicações
│   ├── schools-and-addresses.json     # Export derivado sem turmas
│   └── source/
│       ├── applications-2026.xlsx     # Planilha de escolas, turmas e aplicações
│       └── Consolidado_Escolas_Aplicadores.xlsx # Escala individual por turma
├── docs/
│   ├── previews/                      # Capturas e export local históricos
│   ├── sources/                       # Textos usados no cronograma/contexto
│   └── sources-and-validation.md      # Proveniência, ressalvas e validação
├── scripts/
│   ├── import_applications.py         # Importa escolas/turmas da planilha
│   ├── import_assignments.py          # Importa datas, horários e aplicadores
│   ├── build_page.py                  # Gera o HTML e o export de endereços
│   └── update_from_sheet.py           # Executa o fluxo completo
├── site/index.html                    # Página final publicada pelo Pages
├── requirements.txt                   # Dependência Python do importador
└── README.md
```

O site é estático: HTML, CSS, JavaScript e imagens ficam reunidos em `site/index.html`. Os arquivos-fonte e scripts permitem reconstruir a página; o workflow publica somente `site/`.

## Visualizar

Abra `site/index.html` diretamente no navegador. Mapas e rotas precisam de internet. Para a versão online, use o link **Abrir o portal publicado** no início deste README.

## Reconstruir

Requer Python 3 e dependências de `requirements.txt`. Na raiz do repositório:

```powershell
python -m pip install -r requirements.txt
python scripts/update_from_sheet.py
```

O comando lê as planilhas `data/source/applications-2026.xlsx` e `data/source/Consolidado_Escolas_Aplicadores.xlsx`, atualiza `data/applications-2026.json` e `data/schools-and-addresses.json`, e regenera `site/index.html`. Os caminhos são relativos ao repositório; não dependem de Downloads, OneDrive ou do diretório atual do terminal.

Para executar uma etapa isolada:

```powershell
python scripts/import_applications.py
python scripts/import_assignments.py
python scripts/build_page.py
```

## Publicar alterações

Faça commit e push na branch `main`. O workflow **Publish SAESE site** em `.github/workflows/pages.yml` publica `site/` automaticamente. Em **Settings > Pages**, a origem deve continuar como **GitHub Actions**. Acompanhe execuções pela aba [Actions](https://github.com/paulo-carvalho01/saese.polosaocristovao/actions).

## Dados

O portal informa como fonte dos dados a **Coordenação do Polo São Cristóvão**. A página é pública: os nomes e as atribuições da escala ficarão visíveis a qualquer visitante após a publicação.

Confirme o marcador e o acesso com a escola ou coordenação antes do deslocamento. O portal não substitui a convocação ou as orientações oficiais.

## Licença

Este repositório ainda não declara licença de reutilização. Torná-lo público não concede automaticamente permissão para redistribuir textos, imagens ou dados.
