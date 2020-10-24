class FechaHora (object):
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__ (self, dia=0,mes=0,año=0,hora=0,minutos=0,segundos=0):
        if(hora>=0 and hora<24 and minutos>-1 and minutos<60 and segundos>-1 and segundos<60 and mes>0 and mes<13):
            if(año%4==0 and año%100==0 and año%400==0):
                mesbisiesto = [31,29,31,30,31,30,31,30,31,30,31]
            else:
                mesbisiesto = [31,28,31,30,31,30,31,30,31,30,31]
            if dia <= mesbisiesto[mes-1] and dia>0:
                self.__dia = dia
                self.__mes = mes
                self.__año = año
                self.__hora = hora
                self.__minutos = minutos
                self.__segundos = segundos
            else:
                print("Dia fuera de Rango")
    def Mostrar (self):
        print("{}/{}/{} {}:{}:{}".format(self.__dia,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos))
    
    def PonerEnHora (self,hora=0,minutos=0,segundos=None):
        if hora>=0 and hora<24 and minutos>-1 and minutos<60:
            self.__hora = hora
            self.__minutos = minutos
            if segundos != None:
                self.__segundos = segundos
                
    def AdelantarHora(self,hora=0,minutos=0,segundos=0):
        if((hora<24 and hora>0)and (minutos<60 and minutos>-1) and(segundos<60 and segundos>-1)):
            if ((self.__año%400==0)or (self.__año%100!=0 and self.__año%4==0)):
                listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
            else:
                listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
            self.__hora+=hora
            self.__minutos+=minutos
            self.__segundos+=segundos
            if self.__segundos>59:
                self.__segundos-=60
                self.__minutos+=1
            if self.__minutos>59:
                self.__minutos-=60
                self.__hora+=1
            if self.__hora>23:
                self.__hora-=24
                self.__dia+=1
            if self.__dia>listameses[self.__mes-1]:
                self.__dia-=listameses[self.__mes-1]
                self.__mes+=1
            if self.__mes>12:
                self.__mes-=12
                self.__año+=1
        else:
            print("hora ingresada incorrecta recordar hs 0-23 min 0-59 seg 0-59")            
        
