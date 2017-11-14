# Naam: Thomas van den Berg
# Datum: 13-11-2017
# Versie: 5.0

'In de "main" functie is de juiste volgorde van de functies bepaald en wordt weergeven of het opgegeven "zoekwoord"'
'in de headers aanwezig is, als het zoekwoord aanwezig is dan'
'worden alle functies uitgevoerd voor de sequenties die het zoekwoord in de header hebben staan,'
'vervolgens worden de resultaten weergeven.'
def main():
    bestand = input('Geef een filenaam: ')
    bestand2 = 'enzymen2.txt'
     
    try:
        headers, seqs = lees_inhoud(bestand)
      
        zoekwoord = input("Geef een zoekwoord op: ")

        for index in range(len(headers)):
            print(index, headers[index])
            print(50*'-')
            if zoekwoord in headers[index]:
                is_dna(seqs[index])
                knipt(seqs[index])
            else:
                print('Het woord dat je zoekt staat niet in deze header.')
                print(50*'-')
                print()

    except IOError:
        print('Error het bestand bestaat niet.')

'In deze functie word het opgegeven bestand geopend en afgelezen.'
'Elke zin word gestript van de onnodige leestekens.'
'Als de zin met een header begint word deze in de "headers" list geplaatst.'
'Anders word deze in de "seqs" list geplaatst en ook gestript van alle onnodige leestekens.'
'Elke regel van de sequentie wordt toegevoegd aan de "seq".'
'De twee aangemaakte listen worden gereturned naar de "main" functie om verder mee te kunnen werken.'
def lees_inhoud(bestands_naam):
    document = open(bestands_naam, 'r')
    headers = []
    seqs = []
    seq = ''
    for line in document:
        line = line.strip()
        if '>' in line:
            if seq != '':
                seqs.append(seq)
                seq = ''
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs

    bestands_naam.close()

'In deze functie word er gekeken of de opgegeven sequentie daadwerkelijk DNA of mRNA is,'
'door een variabelen aan te maken die verandert als het geen juiste sequentie is.'
'Er zal worden gekeken naar de vier base die in een DNA of mRNA sequentie voorkomen.'
'Als deze er niet in voorkomen of er komt iets anders in de opgegeven string voor,'
'zal de variabelen veranderen naar 1 en stopt de functie en weergeeft de uitslag.'
def is_dna(seqs):
    invalid = 0

    for ch in seqs:
        if ch not in ['G', 'C', 'A', 'T', '\n', ' ']:
            invalid = 1
            print('False: De opgegeven sequentie is geen DNA sequentie.')
        if ch in ['G', 'C', 'A', 'T']:
            invalid = 0

    if invalid == 0:
        print('True: De opgeven sequentie is een DNA sequentie.')
        print(50*'%')

'In deze functie word er gekeken of er in de sequentie enzymen aanwezig zijn die knippen'
'op een bepaalde positie in de opgegeven sequentie.'
'Er word een bestand geopend waarin de enzymen zijn opgeslagen, deze worden gestript, gesplit'
'en vervolgens worden de naam van het enzym en het stukje DNA in de aangemaakte listen gestopt.'
'In de for loop word het stukje DNA vergeleken met de karakters in de opgegeven sequentie.'
'Bij een match word de bijbehorende positie en welk en enzym matcht weergegeven.'
def knipt(seqs):
    bestand2 = open('enzymen2.txt', 'r')
    enzymen_list = []
    for regel in bestand2:
        regel = regel.strip('\n')
        regel = regel.replace('^','')
        enzymen_list.append(regel)
        enzym = regel.split()[0]
        stukje_seq = regel.split()[1]
        
        for i in range(len(seqs)):
            stukje = seqs[i:i+len(stukje_seq)]
            if stukje == stukje_seq:
                print('Match met',enzym,'op positie',i)

    print(50*'%')
    print()
    bestand2.close()
    
main()
