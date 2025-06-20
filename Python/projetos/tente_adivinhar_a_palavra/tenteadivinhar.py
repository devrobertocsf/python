#inspiração: giovannisantos6448
# \033[31m
from random import choice
from time import sleep
from sys import exit
animais = ['macaco', 'leão', 'gato']
frutas = ['maça', 'jaca', 'banana']

print("\033[91mO jogo ainda está incompleto.Por isso existem alguns bugs e etc.\033[0m")
sleep(5)
print("\033[33mAGUARDE....\033[0m")
sleep(3)
print("\033[36m-=-\033[0m"*20)
print("\033[35m              TENTE ADIVINHAR A PALAVRA!\033[0m")
print("\033[36m-=-\033[0m"*20)
sleep(2)
print("\033[34mTemas disponíveis: Animais, Frutas\033[0m")
print("\033[36m-=-\033[0m"*20)
sleep(2)
escolhertema = str(input("\033[34mEscolha o tema em que você deseja jogar: \033[0m")).lower().strip()
if escolhertema == 'animais':
    palavrasecreta = choice(animais)
    palavrasecreta1 = None
elif escolhertema == 'frutas':
    palavrasecreta1 = choice(frutas)
    palavrasecreta = None
else:
    print("\033[31mDesculpe, esse tema não existe.\033[0m")
    exit()
print("\033[36m-=-\033[0m"*20)


#escolherdificuldade = input("\033[34mEscolha a dificuldade (Easy, Normal, Hard): \033[0m").strip().lower()
#'easy' in escolherdificuldade
#'normal' in escolherdificuldade
#'hard' in escolherdificuldade
#if escolherdificuldade != 'easy' or 'normal' or 'hard':
 # print("Dificuldade não existe!")
 # exit()
#print("\033[36m-=-\033[0m"*20)
print('''ALGUMAS INFORMAÇÕES:
NO NÍVEL EASY VOCÊ TERÁ 3 TENTATIVAS!
NO NÍVEL NORMAL VOCÊ TERÁ 2 TENTATIVAS!
NO NIVEL HARD VOCÊ TERÁ APENAS UMA TENTAITVA! ''')
sleep(5)
print("\033[33mPROCESSANDO....\033[0m")
sleep(3)
escolherdificuldade = input("\033[34mEscolha a dificuldade (Easy, Normal, Hard): \033[0m").strip().lower()
if escolherdificuldade not in ['easy', 'normal', 'hard']:
    print("Dificuldade não existe!")
    exit()
if (escolherdificuldade == 'easy'):
  print("HAHA! Vai jogar nesse nível mesmo? Seu fraco.")
elif (escolherdificuldade == 'normal'):
  print("Opaaaa.... Você não está para brincadeiras, né?")
else:
  print("AVE MARIAAAAAA!!! Eu espero que você perca.")

print("\033[36m-=-\033[0m" * 20)
if escolhertema == 'animais' or 'frutas':
  print(f"\033[34mCerto! Tema escolhido: {escolhertema} e dificuldade {escolherdificuldade}. Boa sorte.\033[0m")
print("\033[36m-=-\033[0m"*20)
sleep(3)
# bloco para exibir as dicas em relação a dificuldade/ tema
if escolherdificuldade == 'easy' and palavrasecreta == 'macaco':
    print("A dica é: Banana")
elif (escolherdificuldade == 'easy'and palavrasecreta == 'leão'):
  print("A dica é: Rei.")
elif (escolherdificuldade == 'easy'and palavrasecreta =='gato'):
  print("A dica é: Bolas de pelos.")
elif escolherdificuldade == 'easy' and palavrasecreta1 == 'maça':
  print("A dica é: É uma fruta geralmente vermelha ou verde.")
elif escolherdificuldade == 'easy' and palavrasecreta1 == 'jaca':
  print("A dica é: Uma fruta de grande porte, com uma casca grossa e espinhosa.")
elif escolherdificuldade == 'easy' and palavrasecreta1 =='banana':
  print("A dica é: É uma fruta amarela.")
elif (escolherdificuldade == 'normal' and palavrasecreta == 'macaco'):
  print("A dica é: 3 sílabas")
elif (escolherdificuldade == 'normal' and palavrasecreta == 'leão'):
  print("A dica é: Faz parte da família dos felinos e é encontrado em diversas regiões da África.")
elif (escolherdificuldade == 'normal' and palavrasecreta =='gato'):
  print("A dica é: 2 sílabas")
elif (escolherdificuldade == 'normal' and palavrasecreta1 == 'maça'):
  print("A dica é: 2 sílabas")
elif escolherdificuldade == 'normal' and palavrasecreta1 == 'jaca':
  print("A dica é: É uma fruta tropical ")
elif escolherdificuldade == 'normal' and palavrasecreta1 == 'banana':
  print("A dica é: É uma fruta popular")
elif (escolherdificuldade == 'hard' and palavrasecreta == 'macaco'):
  print("A dica é: Olhos posicionados frontalmente, córtex cerebral bastante desenvolvido, dieta onívora e presença de polegares opositores")
elif (escolherdificuldade == 'hard' and palavrasecreta == 'leão'):
  print("A dica é: Os dentes podem medir até 6 cm.")
elif (escolherdificuldade == 'hard' and palavrasecreta =='gato'):
  print("A dica é: Assim como a nossa impressão digital, o padrão do nariz desse animal é único.")
elif (escolherdificuldade == 'hard' and palavrasecreta1 == 'maça'):
  print("A dica é: Essa fruta possui 12 substâncias que previnem e combatem o câncer. Todas estão na casca.")
elif escolherdificuldade == 'hard' and palavrasecreta1 == 'jaca':
  print("A dica é: As sementes podem ser consumidas assadas ou cozidas.")
elif escolherdificuldade == 'hard' and palavrasecreta1 == 'banana':
  print("A dica é: rica em carboidratos, sais minerais e vitaminas; e possui poucos lipídios.")

# bloco para dificuldade easy de ANIMAIS
if escolhertema == 'animais' and escolherdificuldade == 'easy':
    chute = input("Qual é o animal? ").lower().strip()
    print("\033[33mPROCESSANDO....\033[0m")
    sleep(2)
    if escolherdificuldade == 'easy' and chute == palavrasecreta:
        print("Parabéns")
    elif escolherdificuldade == 'easy' and chute != palavrasecreta:
        chute1 = input("Tente novamente! ").lower().strip()
        if escolherdificuldade == 'easy' and chute1 == palavrasecreta:
            print("Parabéns")
        else:
            print("\033[33mPROCESSANDO....\033[0m")
            sleep(2)
            chute2 = input("Tente novamente! ").lower().strip()
            if escolherdificuldade == 'easy' and chute2 == palavrasecreta:
                print("\033[33mPROCESSANDO....\033[0m")
                sleep(2)
                print("Parabéns")
            else:
                print("\033[33mPROCESSANDO....\033[0m")
                sleep(2)
                print("Você perdeu!")
# bloco para dificuldade normal de ANIMAIS
if escolhertema == 'animais' and escolherdificuldade == 'normal':
  chute3 = input("Qual é o animal? :")
  if escolherdificuldade == 'normal' and chute3 == palavrasecreta:
    print("Você acertou!")
  else:
    chute4 = input("Tente Novamente!: ")
  if escolherdificuldade == 'normal' and chute4 == palavrasecreta:
    print("Você acertou!")
  else:
    print("Você perdeu!")
# bloco para dificuldade hard de ANIMAIS
if escolhertema == 'animais' and escolherdificuldade == 'hard':
  chute5 = input("Qual é o animal? ")
  if escolherdificuldade == 'hard' and chute5 == palavrasecreta:
    print("Você acertou!")
  else:
    print("Você errou!")

# bloco para dificuldade easy de FRUTAS
if escolhertema == 'frutas' and escolherdificuldade == 'easy':
    chute6 = input("Qual é a fruta? ").lower().strip()
    print("\033[33mPROCESSANDO....\033[0m")
    sleep(2)
    if escolherdificuldade == 'easy' and chute6 == palavrasecreta1:
        print("Parabéns")
    elif escolherdificuldade == 'easy' and chute6 != palavrasecreta1:
        chute7 = input("Tente novamente! ").lower().strip()
        if escolherdificuldade == 'easy' and chute7 == palavrasecreta1:
            print("Parabéns")
        else:
            print("\033[33mPROCESSANDO....\033[0m")
            sleep(2)
            chute8 = input("Tente novamente! ").lower().strip()
            if escolherdificuldade == 'easy' and chute8 == palavrasecreta1:
                print("\033[33mPROCESSANDO....\033[0m")
                sleep(2)
                print("Parabéns")
            else:
                print("\033[33mPROCESSANDO....\033[0m")
                sleep(2)
                print("Você perdeu!")


# bloco para dificuldade normal de FRUTAS
if escolhertema =='frutas' and escolherdificuldade == 'normal':
  chute9 = input("\033[34mQual é a fruta?  \033[0m").lower().strip()
  print("\033[33mPROCESSANDO....\033[0m")
  sleep(2)
  if escolherdificuldade == 'normal' and chute9 == palavrasecreta1:
    print("Você acertou!")
  elif escolherdificuldade == 'normal' and chute9 != palavrasecreta1:
    chute10 = (input("Tente Novamente! ")).lower().strip()
    print("\033[33mPROCESSANDO....\033[0m")
    sleep(2)
    if escolherdificuldade == 'normal' and chute10 == palavrasecreta1:
      print("Você acertou!")
    else:
        print("Você perdeu!")

# bloco para dificuldade hard de FRUTAS

#if chute == palavrasecreta or chute == palavrasecreta1:
 #   print("Parabéns")
#else:
  #  print("\033[31mVocê perdeu!\033[0m")