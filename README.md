Zaprojektować i zaimplementować dwie klasy, jedną reprezentującą kasyno, w którym mozna grać w kości, adrugą reprezentującą gracza w tym kasynie (gracz jest częścią składową kasyna). 
Do kasyna można dodawać iusuwać graczy. Każdy z graczy ma nazwę. 
Rozgrywka w kości ma polegać na tym, że każdy z graczy rzuca 4kośćmi, następnie dla każdego z graczy z osobna zliczana jest punktacja (według listy podanej poniżej) i wskazywany jest zwycięzca danej rozgrywki (lub jeśli kilku graczy miało ten sam wynik rozgrywka uznawana jestza nierozstrzygniętą).
Napisz testy dla obu klas, w szczególności z wykorzystaniem monkeypatchy.


Przykładowa propozycja implementacji:

Kasyno:
Atrybuty:lista graczy
Metody:przeprowadzenie rozgrywki rzut koścmiwskazanie zwycięzcy

Gracz:
Atrybuty:nazwau kład kości, wynik
Metody:obliczenie wyniku na podstawie układu kości

Oprócz tego należy również zaimplementować metody dostępowe dla atrybutów.

Punktacja:
Para - wynik na kostce * 2 (para czwórek = 8 pkt)
Trójka - wynik na kostce * 4 (trójka dwójek = 8 pkt)
Kareta - wynik na kostce * 6 (czwórka jedynek = 6 pkt)
Same cyfry parzyste - suma oczek + 2
Same cyfry nieparzyste - suma oczek + 3
(w przypadku gdy jednocześnie występuje np. para, a jednocześnie wszystkie cyfry są parzyste, bierzemy poduwagę lepszy wynik punktowy. Przykład: Dla układu [6,6,6,2] mamy trójkę szóstek wartą 24 pkt i same cyfryparzyste warte 22 pkt, czyli cały układ ma wartość 24 pkt)
