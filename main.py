dizionario = {

            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione"
            "CREEPY": "spaventoso, inquietante"
            "PARA": "preoccuparsi per qualcosa, paranoiarsi"
    
            }

parola = input("Inserisci una parola di cui non conosci il significato")

if parola.upper() in dizionario.keys():
    print (dizionario[parola.upper()])
else:
    print ("La parola inserita non è presente nel dizionario")
