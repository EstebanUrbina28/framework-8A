



from random import Random, randint

acomulador =0
status = True

while status :


   for x in range (1,100):
     
    
  
    dice1 = randint(0,6)
    dice2 = randint(0,6)
    print("D1: ", dice1) 
    print("D2: ", dice2) 
    
    acomulador = acomulador+dice1+dice2
     
    print(":::El acomulado va en ::::: ",acomulador)


    if dice1==dice2 :
        status= False
        print("::::El lanzamiento es par a finalizado el juego:::")
    if acomulador > 100 :
        status= False
        print("::::Haz llegado al rango limite:::::::")
    else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")




