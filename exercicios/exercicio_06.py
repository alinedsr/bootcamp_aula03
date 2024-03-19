### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

import random

def gerar_texto_aleatorio(base_texto, tamanho=50):
    palavras = base_texto.split()
    if tamanho > len(palavras):
        return ' '.join(palavras)
    else:
        inicio = random.randint(0, len(palavras) - tamanho)
        return ' '.join(palavras[inicio:inicio+tamanho])
    
texto = ('Lorem ipsum velit sodales vel curae vel amet gravida netus, '
         'amet phasellus aliquam class aliquam sem tristique habitasse, '
         'massa ut ullamcorper mattis sagittis iaculis placerat mollis. '
         'integer dictum malesuada mauris lorem diam mauris vel justo '
         'elementum quam nibh, sit aliquet vitae eleifend consectetur '
         'torquent sociosqu at imperdiet elit, ut pellentesque ac laoreet '
         'eleifend aenean at integer ultricies laoreet. inceptos purus '
         'adipiscing aliquam proin cubilia ac conubia quam, mi hac dictumst '
         'neque tincidunt magna sollicitudin eu nulla, ornare nullam primis '
         'facilisis eros id ligula. blandit lorem purus iaculis eleifend sem '
         'tristique scelerisque sed torquent, pellentesque odio praesent '
         'porta aliquet sociosqu mollis euismod ullamcorper, per ac conubia '
         'purus ornare mollis amet tellus.')


texto_aleatorio = gerar_texto_aleatorio(texto)

palavras = texto_aleatorio.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

contagem_ordenada = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)

for palavra, contador in contagem_ordenada:
    print(f"{palavra}: {contador}")

