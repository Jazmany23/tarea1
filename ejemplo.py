class Ejercicios:
    def __init__(self):
        pass
    
    #1.diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio cualquiera
    def calculodepi(self):
        Re = float(input("ingrese el radio de su circulo: "))
        pi = 3.1416
        s = pi*Re**2
        print("la superficie de su circulo es:{} ".format(s))

    #2.En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra
    def descuento(self):
        To = float(input("Ingrese su total de la compra: "))
        d = To*0.15
        Fc = To-d
        print("Su total a cancelar es: {} ".format(Fc))

    #3.Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
    #El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por
    # las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
    def ventas(self):
        for x  in range(4):
            Sa = float(input("Ingrese su salario: "))
            v1 = float(input("Igrese el valor de mi primer venta: "))
            v2 = float(input("Ingrese el segundo valor de la venta: "))
            v3 = float(input("Ingrese el tercer valor de la venta: "))
            To = v1+v2+v3
            Co = To*0.1
            Tv = round(To+Co,2) 
            print("El total a recibir por comicion es:{} ".format(Tv))

    #4.Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba
    def algoritmo(self):
        c = float(input("Ingrese su calificacion: "))
        if c >= 7:
            print("Has aprobado ")
        
    #5. Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
    def algoritmo2(self):
        c = float(input("Ingrese su calificacion: "))
        if c >= 7:
            print("Has aprobado ")
        else:
            print("Has reprobado")

    #6.Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
    def sueldo(self):
        s = float(input("Ingrese su sueldo: "))
        if s < 600:
            n = s+s*0.1
            print("Su nuevo sueldo es {}".format(n))
        else:
            print("Su sueldo sigue siendo de {}".format(s))

    #7.Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo
    #  exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 
    # se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.
    def dinero(self):
        H = int(input("Ingrese el numero de horas trabjadas: "))
        P = float(input("Ingrese el valor a pagar por hora:$ "))
        if H > 48:
            t = H - 48
            s = 40*P + 8*P*2 + t*P*3
            
        else: 
            if H > 40:
                d = H - 40
                s = 40*P + d*P*2
            else:
                s = H*P
                print("El Total a pagar por las horas trabajadas es : {}".format(s))

    
    #8.Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
    def diff(self):
        n = []
        for i in range(3):
            num = float(input("Introduce el número #{}: ".format(i + 1)))
            n.append(num)
        m = n[0]
        for num in n:
            if num > m:
                m = num
        print("El numero mayor es : {}".format(m))

    #9.Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:
    def var(self):
        v = int(input("Ingrese el valor de V: "))
        num = int(input("Ingrese el valor de num: "))
        if num == 1:
            r = 100*v
        elif num == 2:
            r = 100^v
        elif num == 3:
            r = 100/v
        else:
            r = 0
        print("El resultado es {}".format(r)) 

    #10.Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga 
    #calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado
    def exa(self):
        C1 =int(input("Ingrese la primera nota: "))
        C2 = int(input("Ingrese la segunda nota: "))
        if C1 >= 80 and C2 >= 80:
            print("A sido aceptado")
        else:
            print("A sido rechazado")

    #11.Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado
    def cuadrados(self):
        S = 0
        i = 1
        for i  in range(101):
            S = S + i
            i += 1
        print(S)
    #12.Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100
    def nume(self):
        i = 0
        while i<100:   
            i += 1
            print(i)
    #13.Diseñe un pseudocódigo para calcular la suma y producto de N números enteros,
    #utilizando un bucle controlado por el usuario
    def buc(self):
        su = 0
        p = 1
        n = "y"
        while n != "n"and n != "N":
            num = int(input("Ingrese N: "))
            su += num
            p *= num
            n = input("Desea continuar(S/N)" )

        print("Total de la suma es :{}".format(p))
        print("total del producto es :{}".format(su))

    #14.Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela
    def calc(self):
        sum = 0
        p = 1
        n = int(input("Ingrese N: "))
        while n != -1:
            sum += 1
            p = p*n            
        print("Total de la suma es :{}".format(p))
        print("total del producto es :{}".format(sum))

    #15.Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más divisores que él mismo y la unidad.
    #Elaborar Pseudocódigo:
    def pri(self):
        pr = "True"
        div = 2
        r = int(input("Ingrese su numero:"))
        while div < r and pr == "True":
            res = r % div
            if res == 0:
                pr = "False"
                div = div+1
        if pr == "True":
            print("Su numero {} es primo " .format(r))
        else:
            print("Su numero {} no es primo".format(r))

    #16.Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado de la siguiente serie:
    #1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.
    def metodo(self):
        from fractions import Fraction
        ser = 0
        I = 1
        r = int(input("Ingrese un numero entero: "))
        b = "T"
        # while I>r:
        for x in range (r):
            if b == "T":
                ser = ser + Fraction(1,I)
                b ="F"               
            else:
                ser = ser - Fraction(1,I)
                b = "T"
            I += 1           
        print(ser) 
    #17.Calcular el factorial de N números enteros leídos de teclado.
    def fac(self):
        num = int(input('Rango: '))
        for i in range(1,num+1):
            m = int(input('Numero: '))
            fact = 1
        for j in range(1,m+1):
            fact = fact * j
            print(f'El factorial es: {fact}')
    #18.Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación escribir en un vector A todos los números
    #negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores
    def vector(self):
        import random as rd
        prom = []
        cal = [[rd.randint(0,10)for e in range(6)]for e in range(30)]
        for i in range(30):
            sum = 0
            for j in range(6):
                sum = sum + cal[i][j]
                pd = round(sum/6,2)
            prom.append(pd)
            print(f'promedio del alumno: {i+1} : {round(sum/6,2)}')

        prom.sort(reverse=True)
        print(f'La mayor nota es: {prom[0]}')







        





    















           

          
            
            



        

cal1 = Ejercicios()
cal1.vector()


