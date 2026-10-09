# SAESE 2026 | Polo São Cristóvão

Portal responsivo de consulta para os aplicadores do Sistema de Avaliação da Educação Básica de Sergipe (SAESE) no Polo São Cristóvão. Reúne a relação de escolas, endereços, turmas e turnos, além do cronograma e das orientações para as aplicações de 2026.

## Acesso

- **Site:** [paulo-carvalho01.github.io/saese.polosaocristovao](https://paulo-carvalho01.github.io/saese.polosaocristovao/)
- **Repositório:** [github.com/paulo-carvalho01/saese.polosaocristovao](https://github.com/paulo-carvalho01/saese.polosaocristovao)

O site é público e pode ser aberto em navegadores de computador ou celular. As rotas e os mapas do Google Maps precisam de conexão com a internet.

## O que o portal oferece

- Busca de escolas por nome, endereço ou região, com filtro por rede de ensino.
- Fichas com endereço, mapa por busca, link para rota e informações de turmas e turnos.
- Identificação de nomes anteriores quando isso ajuda a localizar a escola.
- Cronograma do treinamento e das semanas de aplicação, com orientações gerais.
- Conteúdo de endereços disponível também no HTML para visualizadores que não executam JavaScript; busca e filtros interativos requerem JavaScript.

A relação publicada contém 37 escolas e as turmas registradas no material do SAESE 2026. O arquivo de origem não informa uma data individual de aplicação para cada escola; consulte a convocação para confirmar esses dados.

## Estrutura do repositório

```text
.
├── .github/
│   └── workflows/
│       └── pages.yml     # Publica site/ no GitHub Pages
├── site/
│   └── index.html        # Aplicação estática publicada
└── README.md             # Documentação do projeto
```

O portal não usa framework, etapa de compilação ou instalação de dependências. O HTML, CSS, JavaScript e as imagens necessárias estão reunidos em `site/index.html`.

## Visualizar localmente

Abra `site/index.html` diretamente no navegador. A busca e os filtros funcionam sem servidor local. Mapas, rotas e demais recursos externos dependem de conexão com a internet.

## Atualizar e publicar

1. Edite `site/index.html`.
2. Envie as alterações para a branch `main` do repositório.
3. O workflow **Publish SAESE site** publica automaticamente a pasta `site/` pelo GitHub Pages.

O workflow está em `.github/workflows/pages.yml`. A origem de publicação do repositório deve permanecer configurada como **GitHub Actions** em **Settings > Pages**. O andamento e eventuais erros podem ser acompanhados na aba [Actions](https://github.com/paulo-carvalho01/saese.polosaocristovao/actions).

## Dados e conferência dos endereços

As informações de escolas e turmas seguem o material do SAESE 2026 fornecido para o polo. Os endereços foram reunidos de cadastros públicos e informações fornecidas para o projeto; a procedência é indicada nas fichas quando disponível.

Os mapas são resultados de busca por nome e endereço, não coordenadas verificadas previamente. Confirme o marcador e o acesso com a escola ou a coordenação antes do deslocamento. O portal é um guia de consulta e não substitui a convocação nem as orientações oficiais.

## Licença

Este repositório ainda não declara uma licença de uso. A disponibilidade pública do site não concede, por si só, autorização para reutilizar ou redistribuir seus textos, imagens ou dados. Para solicitar permissão, entre em contato com o responsável pelo repositório.
