# -*- coding: utf-8 -*-

import random

name = str('')

count = 1

playerMove, listSorted, ranking = [], [], []

def banner():
  print(''' 
  Welcome to MasterMind :)
  
  What do you need to know:
  1 - To exit, just type 's' at any time in the game
  2 - You need to discover the 4 numbers drawn in the correct order.
  3 - Each number must be separated by a space. EX: 1 2 3 4
  4 - The use of repeated numbers is not allowed
  5 - You have 10 chances to discover the numbers 
  
  Have a good game
  ''')

def sortNum():
  listSorted.clear()
  count = 0
  while count < 4:
    sort = random.randint(1,6) 
    if sort not in listSorted:
      listSorted.append(sort)
      count +=1
  return listSorted

def verifyMove(receiveSort,receiveMove):
  displaced, placed = 0, 0
  print('receiveMove ==', receiveMove, 'receivesort ==', receiveSort) 
  for i in receiveMove: 
    if i in receiveSort: 
      if receiveSort.index(i) == receiveMove.index(i):
        placed +=1
      else:
        displaced +=1 
  return print(f' {displaced} shifted numbers \n {placed} allocated numbers')

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
      print(f' O {(count + 1)}º colocado é {ranking[count][1 ]} com {ranking[count][0]} jogadas')
      count += 1
  if len(ranking) <= 3:
    while count < len(ranking):
      print(f' The {(count +1)}º placed is {ranking[count][1]} with {ranking[count][0]} moves')
      count +=1

def numOut(n): 
  numOut = []
  validaNum = '123456'
  for c in validaNum:
    if c not in n:
      numOut.append(c)
  print('---------------------------')
  print(f" The numbers {numOut} is out")
  print('---------------------------')

def validaPlayerMove(n):
  if n == 's':
    print('Is there another player? [y]Yes [n]No') 
    if input() == 'y': 
      main()
    else:
      guessRank() 
      return False
  else: 
    move = n.split(' ') 
    numOut(move)
    playerMove.clear()
    repeat = 0 
    for i in move:
      intConvert = int(i) 
      playerMove.append(intConvert)
    
    for j, x in enumerate(move):
      if j != move.index(x):
        repeat +=1
    if repeat > 0:
      print('--------------------------------------')
      print('  Repeated numbers!! try again')
      print('--------------------------------------')
    else:
      verifyMove(listSorted, playerMove)
  return True

def keepPlaying():
  global name
  global count
  count = 1
  while count < 10:
    if count == 10:
      print("You've exhausted your chances! Game Over")
      break
    validationMove = validaPlayerMove(guessPlayerMove())
    if validationMove == False: 
      print(' Game Over!! ')
      break
    if validationMove == True:
      if listSorted == playerMove:
        print(f'Congratulations {name} You win in {count} moves')
        print(f'{name} Do you wnat play again? [y]Yes [n]No')
        if input() == 'y':
          sortNum()
          count = 1
          guessPlayerMove()
        else: 
          print('There is a new player? [y]Yes [n]No')
          verify = input()
          if verify == 'n':
            insertTorank()
            guessRank()
            break
          if verify == 'y':
            insertTorank()
            main()
            break   
    print(f'You have {(10 - count)} moves') 
    count +=1
  return count

def guessPlayerMove():
  print(f'{name} Enter 4 numbers separated by "space" [s]Exit:')
  return input()

def main():        
  global count      
  global name       
  count = 1         
  banner()         
  sortNum()       
  print('Please enter with your name [s]Exit')
  name = input()
  if name == 's':   
    return print("You left...")
  else:            
    keepPlaying()  
  return

main()

print(ranking)
