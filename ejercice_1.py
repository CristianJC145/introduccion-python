verbo = str(input("Escriba verbo en infinitivo para conjugar: "))
ultima_letra= verbo[len(verbo)-1]
penultima_letra=verbo[len(verbo)-2]
terminacion = penultima_letra + ultima_letra 
verbosinterminacion = verbo.replace(terminacion, "")
if terminacion == 'ar':
    verbosinterminacion = verbo.replace(terminacion, "")
    print ("Yo" + " "+ verbosinterminacion + "o")
    print ("Tu" + " "+ verbosinterminacion + "as")
    print ("El" + " "+ verbosinterminacion + "a")
    print ("Nosotros" + " "+ verbosinterminacion + "amos")
    print ("Ellos" + " "+ verbosinterminacion + "an")
elif terminacion == 'er' :
    print ("Yo" + " "+ verbosinterminacion + "o")
    print ("Tu" + " "+ verbosinterminacion + "es")
    print ("El" + " "+ verbosinterminacion + "e")
    print ("Nosotros" + " "+ verbosinterminacion + "emos")
    print ("Ellos" + " "+ verbosinterminacion + "en")
elif terminacion == 'ir' :
    print ("Yo" + " "+ verbosinterminacion + "o")
    print ("Tu" + " "+ verbosinterminacion + "es")
    print ("El" + " "+ verbosinterminacion + "e")
    print ("Nosotros" + " "+ verbosinterminacion + "imos")
    print ("Ellos" + " "+ verbosinterminacion + "en")
    