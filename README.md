# 2-Imersão Alura IA

Este projeto é um sistema de recomendação baseado em IA que utiliza o modelo LLM Gemini do Google para sugerir séries de TV com base nas preferências do usuário. Ele é projetado para demonstrar a integração de modelos avançados de IA em aplicações web usando Streamlit, proporcionando uma interface amigável para recomendações personalizadas.

Para testar, acesse o meu [sistema de recomendação](link-para-o-sistema-recomendacao)

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Contribuições](#contribuições)
- [Suporte](#suporte)
- [Licença](#licença)

## Instalação

Certifique-se de ter o Python 3.8 ou superior instalado. Siga os passos abaixo para configurar o ambiente:

```bash
git clone https://github.com/seu-usuario/2-imersao-alura-ia.git
cd 2-imersao-alura-ia
pip install pipenv
pipenv install
```

Crie o arquivo \`.env\` na raiz do diretório do projeto e adicione sua chave da API do Google:

```plaintext
API-KEY=sua-chave-da-api-google
```

Nota: Lembre-se de substituir \`sua-chave-da-api-google\` pela sua chave real.

## Uso

Para utilizar este sistema de recomendação, siga estes passos:

```bash
pipenv run streamlit run main.py
```

Para instruções detalhadas de uso, assista o vídeo em [Guia de Uso](link-para-guia-detalhado).

Não esqueça de baixar o arquivo EXCEL base para ser utilizado na ferramenta disponível [aqui](link-para-o-arquivo).

## Funcionalidades

- Recomendações de séries em tempo real.
- Interface web amigável.
- Configurações de recomendação personalizáveis.
- MAPEADO: Inclusão de imagens das séries sugeridas para melhor visualização.
- MAPEADO: Possibilidade de extrair a lista de sugestões e integrar com sistemas de gestão de episódios.

## Contribuições

Contribuições são bem-vindas! Abra sua requisição que iremos analisar!

## Suporte

Encontrou problemas? Mande e-mail para lucas.pastana@gmail.com

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
