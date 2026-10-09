# Fontes e validação

Este documento registra a origem dos dados publicados e as ressalvas para uso dos endereços.

## Materiais do projeto

- `data/source/applications-2026.xlsx`: planilha SAESE 2026, aba `Tuma_Escola_Polo`, intervalo A1:E149. Tem 37 escolas, 148 linhas de turma e soma de 192 aplicações. Células vazias de escola pertencem ao grupo iniciado pela escola nomeada na linha anterior. A planilha não informa data individual por escola.
- `docs/sources/application-schedule-2026.txt`: cronograma local: treinamento em 07/11/2026; aplicações prioritárias de 09 a 13/11 e contingência de 16 a 19/11; manhã 8h–11h e tarde 13h–16h. O local do treinamento seria divulgado.
- `docs/sources/saese-overview.txt`: contexto histórico do SAESE. O cronograma ali descrito pertence a outra edição e não foi usado para 2026.
- `assets/saese-logo.jpeg` e `assets/sao-cristovao-illustration.jpeg`: imagens originais incorporadas ao HTML pelo gerador.

A cópia versionada da planilha teve os metadados de autoria removidos. O original local foi preservado.

## Referências de endereços

- [Cadastro municipal de São Cristóvão](https://www.saocristovao.se.gov.br/orgaos/semed?abrir_modal=true): endereços municipais.
- Cadastros estaduais SIAE/Escola Eficiente: endereços e fontes individuais registrados nas fichas.
- [Diretório complementar de escolas estaduais](https://www.escol.as/cidades/1817-sao-cristovao/dependencia/estadual): usado quando necessário para Luiz Guimarães, Neyde Mesquita e complemento da Rua 62 de Glorita Portugal.
- [Painel DRE 08](https://app.powerbi.com/view?r=eyJrIjoiNmI4YWQ1ZTMtZDllOC00Mjk2LThlZTYtMjRkMmY4ZThjOGQxIiwidCI6ImUxNmI0YjM5LWI4ZmMtNGE2Mi05YThmLTQ1YjdkYjU3NmRjOSJ9): consulta anterior da edição 2025, usada como apoio para associar nomes abreviados a cadastros; a lista publicada de 2026 segue a planilha de aplicações.
- Endereço da Escola Municipal Professora Luzinete Teixeira Santos de Oliveira: informado pelo usuário como `Unnamed Road, São Cristóvão - SE, 49100-000`.

## Ressalvas

- Feijão e Professora Luzinete Teixeira Santos de Oliveira são a mesma escola, conforme informação de alteração de denominação fornecida para o projeto.
- O endereço de Luzinete foi informado pelo usuário; o nome anterior aparece como auxílio à busca.
- Luiz Guimarães e Neyde Mesquita ainda precisam de confirmação em cadastro estadual.
- Para Elísio Carmelo, foi usado Rua Erundino Prado Filho, apesar de o diretório complementar indicar outro logradouro.
- Para Manoel dos Passos, foi usado Avenida Dom José Vicente Távora, Centro; outro diretório informa uma variação do logradouro.
- Glorita Portugal aparece no cadastro estadual apenas como Conjunto Eduardo Gomes; Rua 62 vem do diretório complementar.
- Alguns cadastros municipais informam apenas povoado ou loteamento.
- Os mapas são buscas do Google Maps, não coordenadas verificadas uma a uma. Confirme o marcador e o acesso antes do deslocamento.

## Pré-vias

Os PNGs em `docs/previews/` são capturas históricas de etapas anteriores. `previous-local-export.html` é uma cópia do HTML antes da reorganização. Esses arquivos preservam o processo, mas não são a fonte atual; a aplicação vigente é `site/index.html` e a versão online está vinculada no README e no painel About do repositório.
