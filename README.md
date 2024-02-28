# Grave a tela do seu PC com esta lib
O código Python é um gravador de tela com interface gráfica simples. Ele utiliza a biblioteca customtkinter para a interface e screen_recorder_sdk para a funcionalidade de gravação de tela. Aqui está um resumo das principais partes do código:

Imports: 
- Importa os módulos necessários para a aplicação, incluindo customtkinter, os e screen_recorder_sdk.

Classe GravadorTela:
- Define uma classe para a aplicação.
O método __init__ é o construtor da classe, inicializando a janela principal da aplicação.
Configura a janela principal com tamanho fixo e sem possibilidade de redimensionamento.
Chama o método itens_janela para configurar os widgets na janela.
Método itens_janela:

Cria e posiciona os widgets da interface do usuário, incluindo um rótulo e três botões.
Métodos play, stop e folder:
- play: Inicia a gravação da tela quando o botão "Play" é clicado.
- stop: Para a gravação da tela quando o botão "Stop" é clicado.
- folder: Abre a pasta onde o vídeo gravado é salvo.

Bloco __name__ == '__main__':
- Cria uma instância da classe GravadorTela quando o script é executado diretamente.
Em resumo, o código cria uma interface simples para gravar a tela do computador e controlar o processo de gravação através de botões.

## Rodando projeto

Clone o projeto

```bash
  git clone https://github.com/python-brasil/grave-a-tela-do-seu-pc-com-essa-lib.git
```
Recomandamos criar uma venv antes de instalar as dependências
```bash
  python -m venv venv
```
em Linux
```bash
  python3 -m venv venv
```
Instale as dependências

```bash
  pip install -r requirements.txt
```

em Linux

```bash
  pip3 install -r requirements.txt
```

## Screenshot

![Grave a tela  do seu PC  com essa lib](https://github.com/python-brasil/grave-a-tela-do-seu-pc-com-essa-lib/assets/126124866/6e9b4d95-a014-4171-8b75-29e04911841e)

## Infos de commits

- :package: novas funcionalidades
- :up: atualizações
- :ant: correções de bug
- :checkered_flag: release


## Nos acompanhe nas redes

- Instagram - [@python_brasil](https://www.instagram.com/python_brasil/)
- LinkedIn - [Comunidade Python Brasil](https://www.linkedin.com/company/comunidade-python-brasil)
- GitHub - [python-brasil](https://github.com/python-brasil)
- YouTube - [@Python_Brasil](https://www.youtube.com/@Python_Brasil)
- Pinterest - [Python Brasil](https://br.pinterest.com/pythonbrasil/)
- TikTok - [@python_brasil](https://www.tiktok.com/@python_brasil)

