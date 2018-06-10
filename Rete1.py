import random
import time
import MySQLdb

conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="neuraldatas")
x = conn.cursor()

rate = 0.01

neurons = [0.0, 0.0]        
weights = [random.uniform(0, 1), random.uniform(0, 1)]    # [input1, input2, somma/obbiettivo chiamate--> test_in[0] e test_in[1] 
test = [ [4, 2, 6]    ]                                   # i pesi verranno aggiustati usando test_in[2] come obbiettivo.
bias = 1



def output(threshold):      # Resterà a 1 finchè lavoreremo con s positivo.
    global neurons, weights
    s = neurons[0] * weights[0] + neurons[1] * weights[1] + bias
    if s > threshold:
        return s
    return 0

epoches = 0
while 1:
    for i in range(len(test)):  
        neurons[1] = test[i][1]
        out = output(2)
        # Pesi aggiustati in base alla formula:
        # Wnew = Wold + rate * [Obbiettivo - Attuale] * input
        weights[0] = weights[0] + rate * (test[i][2] - out) * neurons[0]
        weights[1] = weights[1] + rate * (test[i][2] - out) * neurons[1]
        # L'errore verrà corretto in base alla formula:
        # Bias_new = Bias_old + (Obbiettivo - Attuale)
        bias = bias + test[i][2] - out
        if out == test[i][2]:     
            print("{0} ----> {1}!!!".format(out, test[i][2]))
			
            time.sleep(5)
            print("Generazioni necessarie = {0}".format(epoches))
			
			
        else:
            print("{0} dovrebbe essere {1}".format(out, test[i][2]))
    epoches += 1
    print("Pesetto1 = {0}\nPesetto2 è {1}".format(weights[0], weights[1]))
    print("-" * 79 + "\n\n")
		x.execute("""INSERT INTO neuraldatas VALUES (peso1,peso2,risultato)""",(weights[0],weights[1],out))
                conn.commit(
	

    if epoches % 10000 == 0:
        print("Generazioni avvenute = {0}.".format(epoches))
		
        time.sleep(3)
