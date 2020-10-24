if __name__ == '__main__':

    from ClaseFecha import FechaHora

    d=int(input("Ingrese Dia: "))

    mes=int(input("Ingrese Mes: "))

    a=int(input("Ingrese Año: "))

    h=int(input("Ingrese Hora: "))

    m=int(input("Ingrese Minutos: "))

    s=int(input("Ingrese Segundos: "))

    r = FechaHora () #  inicilizar día, mes, año con 1/1/2020, y hora, minutos y 

                              #  segundos con 0h, 0m, 0s.


    r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s

    r2= FechaHora(d,mes,a,h, m, s)

    r.Mostrar()

    r1.Mostrar()

    r2.Mostrar()

    Poner_hora = int(input("Ingrese Hora r: "))

    r.PonerEnHora(Poner_hora) # solamente la hora

    r.Mostrar()

    horar2 = int(input("Ingrese hora para r2: "))
    minutor2 = int(input("Ingrese minutos para r2: "))

    r2.PonerEnHora(horar2, minutor2) #hora y minutos

    r2.Mostrar()

    hr = int(input("Ingrese hora r: "))
    mr = int(input("Ingrese minutos r: "))
    sr = int(input("Ingrese segundos r: "))

    r.PonerEnHora(hr, mr, sr) #hora, minutos y segundos

    r.Mostrar()

    horaR = int(input("Ingresar Hora a adelantar r: "))

    r.AdelantarHora(horaR) #sumar 3 horas a la hora actual

    r.Mostrar()

    horaR1 = int(input("Ingrese Hora a adelantar r1: "))
    minutosR1 = int(input("Ingrese Minutos a adelantar r1: "))

    r1.AdelantarHora(horaR,minutosR1) #sumar 1 hora y 15 minutos a la hora actual

    r1.Mostrar()
