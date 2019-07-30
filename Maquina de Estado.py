from pysm import State, StateMachine, Event
import os
#import pysm

def acostarse(state, event):
	print("Pepe se fue a acostar a la cama y se tapo con una manta")

def saltar(state, event):
	print("Pepe se elevo del suelo como por arte de magia")

def morir(state, event):
	print("Pepe murio...", end=" ")
	if state == despierto:
		print("parado, le agarro un bobaso al pobre")
	if state == dormido:
		print("soñando que era un buen programador")
	if state == saltado:
		print("cayendo arruinando sus sueños")

def caer(state, event):
	print("Y pum se dio contra el suelo")

def cafe(state, event):
	print("Pepe tomo un asqueroso cafe")

def despertarse(state, event):
	print("Pucha que es temprano")

despierto = State('Despertando')
dormido = State('Durmiendo')
saltado = State('Saltando')
morido = State('Muriendo')

sm = StateMachine('Pepe')
sm.add_state(despierto, initial=True)
sm.add_state(dormido)
sm.add_state(saltado)
sm.add_state(morido)

# Estado despierto
sm.add_transition(despierto, dormido, events=['Acostarse'], action=acostarse)
sm.add_transition(despierto, saltado, events=['Saltar'], action=saltar)
sm.add_transition(despierto, morido, events=['Morir'], action=morir)
sm.add_transition(despierto, despierto, events=['Cafe'], action=cafe)

# Estado dormido
sm.add_transition(dormido, despierto, events=['Despertarse'], action=despertarse)
sm.add_transition(dormido, morido, events=['Morir'], action=morir)

# Estado saltando
sm.add_transition(saltado, despierto, events=['Caer'], action=caer)
sm.add_transition(saltado, morido, events=['Morir'], action=morir)


sm.initialize()


if __name__ == '__main__':
	print("Bienvenidos al juego de Pepe")
	while (sm.state != morido):
		print("\nPepe se encuentra ", sm.state, end="\n\n")
		print("1 Despertarse")
		print("2 Dormirse")
		print("3 Saltar")
		print("4 Morir")
		print("\nQue deberia hacer Pepe?", end=" ")
		opc=input()
		os.system('cls')
		try:
			opc = int(opc)
			if (opc < 1 or opc > 4):
				print("Lanzo Exception", opc)
				raise Exception("del 1 al 4 weon")
			else:
				if (sm.state == despierto):
					if (opc == 1):
						sm.dispatch(Event('Cafe'))
					if (opc == 2):
						sm.dispatch(Event('Acostarse'))
					if (opc == 3):
						sm.dispatch(Event('Saltar'))

				elif (sm.state == dormido):
					if(opc == 1):
						sm.dispatch(Event('Despertarse'))
					if(opc == 2):
						print("ERROR: Loco no podes dormir si ya estas dormido")
					if(opc==3):
						print("ERROR: Pepe no sufre de sonambulismo")

				
				elif (sm.state == saltado):
					if(opc == 1):
						sm.dispatch(Event('Caer'))
					if(opc == 2):
						print("ERROR: ¿Que vas a hacer, dormir en el aire?")
					if(opc == 3):
						print("ERROR: No admitimos doble salto")


				if(opc == 4):
					sm.dispatch(Event('Morir'))


		except Exception as e:
			if (type(e) == Exception):
				print("\nPoneme un numero", e)
			else:
				print("\nPoneme un numero querido")





"""
on = State('on')
off = State('off')

sm = StateMachine('sm')
sm.add_state(on, initial=True)
sm.add_state(off)

sm.add_transition(on, off, events=['Apagarse'])
sm.add_transition(off, on, events=['Prenderse'])

sm.initialize()

def test():
    assert sm.state == on
    sm.dispatch(Event('off'))
    assert sm.state == off
    sm.dispatch(Event('on'))
    assert sm.state == on


if __name__ == '__main__':
    test()

"""