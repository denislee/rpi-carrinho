# rpi-carrinho

Carrinho de controle remoto utilizando Raspberry Pi 3 e o mini-teclado QWERTY sem fio.

Utilizamos a biblioteca pygame para melhor resposta do carrinho em relacao as teclas apertadas, evitando delay dos comandos ou que o carrinho ande sem que haja algum botao pressionado.

# Especificacoes

- 1 Driver de Motor para 2 motores DC
- 2 Motores DC
- 2 Rodas (para o motor DC)
- 1 roda boba para apoio
- 1 Chassi de acrilico
- 2 LEDs branco de alto brilho para farol frontal
- 2 LEDs vermelho difuso para luz traseira
- Resistor de 330 Ohms (para LED vermelho difuso*)
- Resistor de 100 Ohms (para LED branco de alto brilho*)
- Power bank para fornecer energia ao Rpi

* Alimentacao dos LEDs = 5V

# Comandos

- Setas - guiar o carrinho
- Tecla A - acende/apaga farol frontal
- Tecla Q - fecha o programa

Obs: LEDs traseiros acendem ao andar com o carrinho para trás

