def juego():
  _ = str("_")
  m = np.array([[_,_,_],[_,_,_],[_,_,_]])
  n=0 #Limite de movimientos 9, mientras sean menos el juego sigue
  while n<=9:
    print("Escoje un lugar donde colocar tu ficha:")
    ficha_col=int(input("Núm. de columna:"))
    ficha_fil=int(input("Núm. de fila:"))
    if m[ficha_fil,ficha_col] == "X" or m[ficha_fil,ficha_col] == "O":
      print("Ese lugar está ocupado, escoje otro:")
      ficha_col=int(input("Núm. de columna:"))
      ficha_fil=int(input("Núm. de fila:"))
      n=n-1
    m[ficha_fil,ficha_col] = "X"
    a=rd.randint(0,2)
    b=rd.randint(0,2)
    if m[a,b] != "X":
      m[a,b] = "O"
    else:
      a = choice([i for i in range(0,2) if i not in [a]])
      b = choice([i for i in range(0,2) if i not in [b]])
      m[a,b] = "O"
  #Source: https://www.holadevs.com/pregunta/95174/how-to-exclude-certain-numbers-with-randomrandint
    print(m)
    #en cada loop hay que buscar si se ganó alguno
    for i in range(3):
      if m[i,0] == m[i,1] == m[i,2] == "X" or m[0,i] == m[1,i] == m[2,i] == "X":
        print("Felicidades, ganaste")
        quit()
      if m[i,0] == m[i,1] == m[i,2] == "O" or m[0,i] == m[1,i] == m[2,i] == "O":
        print("Lo siento, perdiste")
        quit()
    n=n+1
