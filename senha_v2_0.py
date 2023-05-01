#!/usr/bin/python
#coding: utf-8

import random 

name = str('')
count = 1
playerMove, listSorted,ranking = [], [], []

def sortNum(): 
  listSorted.clear() 
  count = 0
  while count < 4: 
    sort = random.randint(0,6) 
    if sort not in listSorted:
      listSorted.append(sort) 
      count +=1
  return listSorted 

def verifyMove(receiveSort,receiveMove): 
  displaced, placed = 0, 0
  print('receiveMove ==', receiveMove, 'receivesort ==', receiveSort) #deletar do codigo final, apenas para debug
  for i in receiveMove: 
    if i in receiveSort:
      if receiveSort.index(i) == receiveMove.index(i): 
        placed +=1
      else: 
        displaced +=1 
  return print(f'{displaced} Numeros deslocados \n {placed} Numeros alocados') 

def insertTorank():
  geral = {} 
  geral = count,name
  ranking.append(geral)
  ranking.sort() 
  return ranking

def guessRank():
  count = 0
  if len(ranking) > 3: 
   while count < 3:  
      print(f' O {(count + 1)}º colocado é {ranking[count][1 ]}, com {ranking[count][0]} Jogadas')
      count += 1
  if len(ranking) <= 3:
    while count < len(ranking):
      print(f' O {(count +1)}º colocado é {ranking[count][1]}, com {ranking[count][0]} Jogadas')
      count +=1

def validaPlayerMove(n):
  if n == 's':
    print('Existe outro jogador? [s]Sim [n]Nao') 
    if input() == 's': 
      main()
    else:
      print('Fim de jogo!! ')
      guessRank() 
      return False
  else: 
    move = n.split(' ') 
    playerMove.clear() 
    repeat = 0 
    for i in move: 
      intConvert = int(i) 
      playerMove.append(intConvert) 
    
    for j, x in enumerate(move): 
      if j != move.index(x): 
        repeat +=1
    if repeat > 0:
      print('----------------------------------------')
      print('  Numeros repetidos!! tente novamente!  ')
      print('----------------------------------------')
    else:
      verifyMove(listSorted, playerMove) 
  return True 

def keepPlaying(): 
  global name 
  global count 
  count = 1
  while count < 10: 
    if count == 10:
      print('Esgotou suas chances ! Fim de jogo')
      break 
    validationMove = validaPlayerMove(guessPlayerMove())
    if validationMove == False: 
      print(' Fim de jogo!! ')
      break
    if validationMove == True: 
      if listSorted == playerMove: 
        print(f'Parabens {name} Voce venceu em {count} jogadas')
        print(f'{name} Deseja jogar novamente? [s]Sim [n]Nao')
        if input() == 's': 
          sortNum() 
          count = 1
          guessPlayerMove() 
        else: 
          print('Existe um novo jogador? [s]Sim [n}Nao')
          verify = input()
          if verify == 'n': 
            insertTorank()
            guessRank()
            break
          if verify == 's': 
            insertTorank()
            main()
            break   
    print(f'{name} voce tem {(10 - count)} jogadas') 
    count +=1
 
  return count 

def guessPlayerMove(): 
  print(f'{name} Digite 4 numeros separados por espaço! [s]Sair:') 
  return input() 

def main(): 
  global count
  global name 
  count = 1
  sortNum() 
  print('Digite seu nome [s]Sair')
  name = input()
  if name == 's': 
    return "Você saiu..."
  else:
    keepPlaying() 
  return

main()