import random
import time
import MySQLdb     #Libreria connessione database

conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="neuraldatas")    #connessione al Db
x = conn.cursor()

rate = 0.01

neuroni = [0.0, 0.0]        
pesi = [random.uniform(0, 1), random.uniform(0, 1)]    # [input1, input2, somma/obbiettivo chiamate--> test_in[0] e test_in[1] 
test = [ [4, 2, 6]    ]                                   # i pesi verranno aggiustati usando test_in[2] come obbiettivo.
errore = 1



def output(threshold):      # Resterà a 1 finchè lavoreremo con s positivo.
    global neuroni, pesi
    s = neuroni[0] * pesi[0] + neuroni[1] * pesi[1] + errore
    if s > threshold:
        return s
    return 0

gen = 0
while 1:
    for i in range(len(test)):  
        neuroni[1] = test[i][1]
        out = output(2)
        # Pesi aggiustati in base alla formula:
        # Wnew = Wold + rate * [Obbiettivo - Attuale] * input
        pesi[0] = pesi[0] + rate * (test[i][2] - out) * neuroni[0]
        pesi[1] = pesi[1] + rate * (test[i][2] - out) * neuroni[1]
        # L'errore verrà corretto in base alla formula:
        # errore_new = errore_old + (Obbiettivo - Attuale)
        errore = errore + test[i][2] - out
        if out == test[i][2]:     
            print("{0} ----> {1}!!!".format(out, test[i][2]))
			
            time.sleep(5)
            print("Generazioni necessarie = {0}".format(gen))
			
			
        else:
            print("{0} dovrebbe essere {1}".format(out, test[i][2]))
    gen += 1
    print("Pesetto1 = {0}\nPesetto2 è {1}".format(pesi[0], pesi[1]))
    print("-" * 79 + "\n\n")
		x.execute("""INSERT INTO neuraldatas VALUES (peso1,peso2,risultato)""",(pesi[0],pesi[1],out))
                conn.commit()      #Inserimento dati nel Db
	

    if gen % 10000 == 0:
        print("Generazioni avvenute = {0}.".format(gen))
		
        time.sleep(3)
