class FechaHora:
    __year = 0
    __mes = 0
    __dia = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, dia = 1, mes = 1, year = 2020, hora = 0, minutos = 0, segundos = 0):
        print(year%100 == 0)
        print(year%400== 0)
        print(year%4== 0)
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0: # Evalua año bisiesto 
            if mes <= 2 and mes > 0:
                if mes == 2:
                    if dia <= 29 and dia > 0: # Evalua mes bisiesto
                        self.__dia = dia
                        self.__mes = mes
                        self.__year = year
                        if(hora < 24 and hora >= 0):
                            if(minutos < 60 and minutos >= 0):
                                if(segundos < 60 and segundos >= 0):
                                    self.__hora = hora
                                    self.__minutos = minutos
                                    self.__segundos = segundos
                                else:
                                    print("Segundos ingresados icorrectamente")
                            else:
                                print("Minutos ingresados icorrectamente")
                        else:
                            print("Horas ingresadas icorrectamente")
                else:
                    print("Dias ingresados icorrectamente")
        else:
            if mes == 2 and dia == 29:
                    print("Dias ingresados icorrectamente. El año no es bisiesto")
            else:
                if dia <= 31 and dia > 0:
                    self.__dia = dia
                    self.__mes = mes
                    self.__year = year
                    if(hora < 24 and hora >= 0):
                        if(minutos < 60 and minutos >= 0):
                            if(segundos < 60 and segundos >= 0):
                                self.__hora = hora
                                self.__minutos = minutos
                                self.__segundos = segundos
                            else:
                                print("Segundos ingresados icorrectamente")
                        else:
                            print("Minutos ingresados icorrectamente")
                    else:
                        print("Horas ingresadas icorrectamente")
            
            
    def Mostrar(self):
        print("Dia: {}" .format(self.__dia))
        print("Mes: {}" .format(self.__mes))
        print("Año: {}" .format(self.__year))
        print("Hora: {}" .format(self.__hora))
        print("Minutos: {}" .format(self.__minutos))
        print("Segundos: {}" .format(self.__segundos))
        print("")
    
    def PonerEnHora(self, hora = 0, minutos = 0, segundos = 0):
        if(hora < 24 and hora >= 0):
            if(minutos < 60 and minutos >= 0):
                if(segundos < 60 and segundos >= 0):
                    self.__hora = hora
                    self.__minutos = minutos
                    self.__segundos = segundos
                else:
                    print("Segundos ingresados icorrectamente")
            else:
                print("Minutos ingresados icorrectamente")
        else:
            print("Horas ingresadas icorrectamente")
        
    def AdelantarHora(self, hora = 0, minutos = 0, segundos = 0):
        self.__hora += hora
        self.__minutos += minutos
        self.__segundos += segundos

        if(self.__segundos >= 60):
            self.__segundos -= 60
            self.__minutos += 1

        if(self.__minutos >= 60):
            self.__minutos -= 60 
            self.__hora += 1

        if(self.__hora >= 24):
            self.__hora -= 24
            self.__dia += 1
        
        if self.__year % 4 == 0 and self.__year % 100 == 0 and self.__year % 400 == 0: # Evalua año bisiesto 
            if(self.__dia >= 31):
                self.__mes += 1
                self.__dia -= 31

            if(self.__mes >= 12):
                self.__year += 1
                self.__mes -= 12
        else:
            if(self.__mes == 2):
                if(self.__dia >= 29):
                    self.__mes += 1
                    self.__dia -= 29
            else:
                if(self.__dia >= 31):
                    self.__mes += 1
                    self.__dia -= 31
                    
                if(self.__mes >= 12):
                    self.__year += 1
                    self.__mes -= 12
            
        
