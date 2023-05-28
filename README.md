# Gerador de Senhas Aleatórias

Este é um código simples em Python que gera senhas aleatórias com base nas propriedades selecionadas pelo usuário.

## Como utilizar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Faça o download ou clone este repositório em sua máquina local.
3. Abra o arquivo em um editor de código ou ambiente de desenvolvimento Python.
4. Execute o código.

## Descrição do código

O código utiliza o módulo `random` do Python para gerar senhas aleatórias. O usuário pode selecionar as propriedades das quais deseja que a senha seja composta, como números, letras maiúsculas, letras minúsculas e caracteres especiais.

Ao executar o código, você será solicitado a fornecer as seguintes informações:

1. **Selecione as propriedades (n, ma, mi, e, all):** Digite as opções separadas por espaço. As opções disponíveis são:
   - `n`: números (0-9)
   - `ma`: letras maiúsculas (A-Z)
   - `mi`: letras minúsculas (a-z)
   - `e`: caracteres especiais (%$#-_&)
   - `all`: todas as opções acima

2. **Dê um prefixo:** Digite um prefixo opcional para a senha.
3. **Dê um sufixo:** Digite um sufixo opcional para a senha.
4. **Escolha o tamanho da senha:** Digite um número inteiro que representa o tamanho desejado para a senha.

Após fornecer todas as informações necessárias, o código irá gerar uma senha aleatória com base nas opções selecionadas e exibi-la no console.


### Executando o código no Windows

1. Certifique-se de ter o Python instalado em seu sistema. Você pode fazer o download da versão mais recente do Python em https://www.python.org/downloads/windows/.
2. Faça o download ou clone este repositório em sua máquina local.
3. Abra o prompt de comando (Command Prompt).
4. Navegue até o diretório onde o arquivo Python está localizado usando o comando `cd`.
5. Execute o código Python usando o comando `python gerador_de_senha.py`.
6. Siga as instruções exibidas no prompt de comando para fornecer as opções desejadas e obter a senha gerada.

### Executando o código no Linux

1. Certifique-se de ter o Python instalado em seu sistema. Em muitas distribuições Linux, o Python já está pré-instalado. Caso contrário, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. (Convencionalmente `sudo apt-get install python3`)
2. Faça o download ou clone este repositório em sua máquina local.
3. Abra o terminal.
4. Navegue até o diretório onde o arquivo Python está localizado usando o comando `cd`.
5. Execute o código Python usando o comando `python3 gerador_de_senha.py`.
6. Siga as instruções exibidas no terminal para fornecer as opções desejadas e obter a senha gerada.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bug ou melhoria para este código, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este código está sob a [licença MIT](LICENSE).
