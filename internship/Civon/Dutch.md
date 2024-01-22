# Mijn stage bij het innovatiecentrum Civon

# Inleiding
Tijdens mijn stage bij het innovatiecentrum Civon heb ik een aantal opdrachten gedaan. Tijdens deze opdrachten ben ik een beetje in het diepe gegooid. Dit komt doordat ik een machine moest automatiseren in mijn eentje. Ondanks dat ik in het diepe gegooid was heb ik veel geleerd en ik ben van plan om hier nog veel meer over te leren. Ik heb ook een aantal andere dingen gedaan zoals het testen van VR brillen en het programmeren van een kleine robot genaamd Misty. Tijdens het testen van de VR brillen heb ik ook een aantal spellen gedaan, deze spellen zijn: "First Steps", "Richie's Plank Experience", "Beat Saber" en "Keep Talking and Nobody Explodes". Deze spellen heb ik ook getest op de verschillende VR brillen. Tijdens het programmeren van Misty heb ik een aantal manieren gevonden om Misty te programmeren. Deze manieren zijn: Blokken, Handmatig op de website, Python op de website en Python op de computer. Tijdens het programmeren van Misty heb ik ook een klein stukje software geschreven waarmee je Misty kan besturen.

# Opdracht 1: Laserlas machine
De laserlas machine is een machine die door sterke lichtstralen een stuk metaal opwarmt tot het punt waar het samen smelt met een ander stuk metaal. Dit is een zeer precies taak. Het grootste nadeel dat hierbij komt kijken is dat de machine niet automatisch werkt. De machine moet handmatig bediend worden. Dit is een langzame taak. Dit komt doordat als je handmatig alle kleine lijntjes moet leggen dan ben je vaak al wel uur bezig. Dit is een hele simpele taak. Bij BeGeDo hebben ze 2 van deze machines en maar 1 persoon die deze machine kan besturen. Helaas staat dus vaak een van de machines stil omdat er geen personeel is om deze machine te besturen. Dit probleem kan opgelost worden door een van de 2 laserlas machines te automatiseren.

![Laser las machine](/pictures/Stage/Civon/BeGeDo/laserWeldingMachine.png)


## Het plan van aanpak
Een goed begin is de geschiedenis te vertellen van deze laserlas machine. Deze laserlas machine is de eerste soort laserlas machine die gemaakt is door een Duits bedrijf dat graag weinig wilt vertellen over hoe de machine werkt. Dit betekent dat er geen documentatie is over de machine. Dus het was een hele uitdaging om te beginnen met het automatiseren van de machine. Helaas kan ik de machine niet uit elkaar halen om te kijken hoe alles in elkaar zit omdat deze machine ook nog steeds gebruikt wordt. Dus ik moest een andere manier vinden om te kijken hoe de machine werkt.
De machine heeft een aantal onderdelen die het mogelijk maken om de machine te besturen. Deze onderdelen zijn:

### De joystick
De Joystick is een onderdeel dat het mogelijk maakt om de machine makkelijk te besturen. De Joystick heeft een paar verschillende functies. De Joystick kan 4 kanten op bewegen. Deze kanten zijn:
- X as: Door de Joystick naar links of rechts te bewegen kan de machine naar links of rechts bewegen.
- Y as: Door de Joystick naar voren of achteren te bewegen kan de machine naar voren of achteren bewegen.
- Z as: Door de Joystick te draaien kan de onderplaat van de machine omhoog en omlaag.
- op de achterkant van de Joystick zit een analoge potentiometer. Deze potentiometer wordt gebruikt om een extra as te hebben. Deze as is de rotatie as van de machine. Deze as wordt niet gebruikt voor mijn project.

De Joystick heeft ook een knop: Deze knop wordt gebruikt om de machine op een snellere snelheid te laten bewegen. Deze knop wordt niet gebruikt voor mijn project.

### Het voetpedaal
Het voetpedaal is een onderdeel dat het mogelijk maakt om de laser te laten pulsen. Dit is een essentieel onderdeel van de machine omdat de laser niet continu aan kan blijven staan. De manier dat die laser zo sterk is komt doordat de laser een hele korte puls geeft. Deze puls is zo kort dat het je het eigenlijk niet ziet. Boven op de las machine hebben ze een scherm staan die laat zien wat de bediener ziet. Op dit scherm zie je eigenlijk alleen een flits en dan is het alweer weg. Helaas is het voetpedaal niet een digitaal signaal maar een analoog signaal. Dit betekent dat het niet een aan of uit signaal is maar een signaal dat overal tussen de 0 volt en de 12 volt kan zitten. Dit is vervelend omdat je het dan niet door een Arduino kan laten lezen. Dit kan je oplossen door een spanningsdeler te gebruiken. Dit is een schakeling die het signaal veranderd van 0 tot 12 volt naar 0 tot 5 volt. Dit is een signaal dat de Arduino wel kan lezen. Dan moet ik ook nog naar die pinnen schrijven. Dit is een probleem omdat de Arduino maar 5 volt kan schrijven. Dit is niet genoeg om de machine te laten pulsen. Hier moet ik nog een oplossing voor vinden.

### De interface
Om mijn systeem iets makkelijk te maken voor de gebruiker heb ik een klein interface gemaakt. Dit interface zijn 3 7-segment displays. Deze worden aangestuurd door een Arduino mega. Ik heb voor de mega gekozen vanwege de aantal digital outputs om de schermpjes aan te sturen. Hiervoor heb ik een hele eigen PCB voor gemaakt

![interface prototype](/pictures/Stage/Civon/BeGeDo/PCB/Interface_prototype.png)



# Opdracht 2: Misty

![MistyRobot](/pictures/Stage/Civon/Misty/Banner2.jpg)

Bij het Civon hebben we een kleine robot genaamd Misty. Misty kan een aantal verschillende dingen zoals 

## Blokken

![Blokken](/pictures/Stage/Civon/Misty/Interface/Blockly.png)

De blokken manier is enorm simpel maar heel erg krachtig. Je kan hiermee snel de robot in beweging krijgen, je hoeft er niet achter te komen hoe de robot beweegt want er bestaan al blokjes voor. Deze blokken kan je vergelijken met de manier dat je een Dobot, NodeRed en Tello drones zou programmeren. Dit is een hele eenvoudige manier om de robot te programmeren. Het nadeel van deze manier is dat je niet alles kan doen op de manier dat je het zou willen doen. Dit komt vooral doordat je gelimiteerd wordt door die blokjes. Stel voor je wilt iets maken wat nog niet bestaat in blokjes vorm dan moet je hopen dat het bestaat door combinaties van blokken en anders heb je pech. Dit is een groot nadeel van deze manier van programmeren.

## Handmatig op de website

![Web](/pictures/Stage/Civon/Misty/Interface/Web.png)

Eigenlijk is er niet heel erg veel speciaals aan deze manier. Het spreekt heel erg voor zichzelf. Op de website heb je een aantal knoppen die de robot een kant op laten bewegen. Dit is nog een enorm eenvoudige manier om de robot te besturen. Het nadeel hieraan is dat je het niet kan automatiseren. Dit is een groot nadeel omdat je dan niet een programma kan maken die de robot automatisch kan laten bewegen of hallo zegt tegen mensen.

## Python
Er zijn 2 verschillende python manieren om het te programmeren. Dus ik maak er 2 verschillende stukken over.

### Python op de website

![PythonWeb](/pictures/Stage/Civon/Misty/Interface/Python.png)

De python op de website is alsnog heel erg eenvoudig maar hiermee kan je al veel en veel meer. Doordat Misty's python library al heel erg veel functies heeft kan je al heel erg veel doen. Dit is een iets moeilijkere manier om de robot te programmeren maar hiermee kan je al veel meer. Doordat je het zelf programmeert kan je het alles laten doen wat je wilt. Een voorbeeld hiervan is dat je Misty compleet autonoom kan laten bewegen. Dit is een groot voordeel van deze manier van programmeren.

### Python op de computer
Zelf vond ik die manier ook niet heel erg prettig. Dit komt doordat je dan op de website in een hele gelimiteerde versie van Visual studio code zit te werken. Hierdoor word je bijna geforceerd om de documentatie ernaast te houden. Op hetzelfde moment als dat ik hiermee begon was ik ook heel erg geïnteresseerd in de Misty API. Dit is een API die je kan gebruiken om de robot te besturen. De manier dat je deze API aanstuurt is via een bericht naar het IP van de robot. Het klinkt best moeilijk maar het is eigenlijk best simpel als je weet hoe een API werkt. Uiteindelijk heb ik een klein stukje software geschreven waarmee je Misty kan besturen. Ik heb dit gedaan door een paar functies te schrijven die dan een request sturen naar de API, om bijvoorbeeld naar voren te bewegen of het hoofd te besturen.
De programmering hiervoor is te vinden op mijn GitHub: [MistyPy](https://github.com/Joppy-School/MistyPy)

# Opdracht 3: VR
Tijdens mijn stage heb ik ook een aantal VR brillen getest en vergeleken. Deze brillen zijn:
- Oculus Quest 1
- Oculus Quest 2
- Oculus Quest 3
Overigens heb ik ook een aantal spellen gespeeld. Deze spellen zijn:
- First Steps
- Richie's Plank Experience
- Beat Saber
- Keep Talking and Nobody Explodes

## VR brillen

### Oculus Quest 1

![Quest 1](/pictures/Stage/Civon/VR/Glasses/q1.jpg)

De Oculus Quest 1 is de eerste versie van de Oculus Quest serie. De Oculus Quest 1 is een hele goede VR bril om mee te beginnen. Dit komt doordat de Oculus Quest 1 een hele goede prijs heeft voor de technology die er in zit. Helaas worden ze niet meet geproduceerd. Dit betekend dat je ze alleen nog maar tweedehands kan kopen. Dit is een groot nadeel omdat je dan niet meer de garantie hebt dat de bril nog goed werkt. De Quest 1 kan je op een paar verschillende manieren gebruiken. Je kan een spel spelen als een standalone headset. Dit betekend dat je geen computer nodig hebt om de bril te gebruiken. Hierdoor is de batterij duur een stuk sneller leeg, de levensduur is dan maar rond de 2 uur. Dit komt doordat de headset dan alles moet renderen en moet inladen. de andere manier om de headset te gebruiken is door hem te verbinden met een computer. Als je deze manier gebruikt dan kan je veel meer dingen doen met de Quest 1. Dit zorgt er ook voor dat de levensduur met bijna verdubbeld wordt. het verbinden met je computerkan je doen door een USB-C kabel te gebruiken. Dit zorgt ervoor dat je computer een hele snelle verbinding maakt met je computer. Als je een goede computer hebt dan kan je bijna niet merken dat je op een VR bril zit te spelen. Of je kan de Quest 1 verbinden via Airlink. Dit is een manier om de Quest 1 draadloos te verbinden met je computer. Hierdoor kan je spelletjes spelen zonder draad die verbonden is met je hoofd. Natuurlijk zitten hier ook nadelen aan, Het grootste nadeel dat er is is dat je een goede LAN verbinding moet hebben. Als je een slechte LAN verbinding hebt dan kan het spel happerig worden, Dit is heel erg vervelend als je een spel speelt en je draait om en dan hapert het spel. Als dit gebeurt dan raak je snel misselijk doordat je hersenen niet precies weten wat gebeurd. Helaas is dit niet alleen een nadeel bij de Quest 1 maar ook bij de Quest 2 en de Quest 3. Dit is een groot nadeel van alle VR brillen die draadloos verbonden zijn met je computer.

### Oculus Quest 2

![Quest 2](/pictures/Stage/Civon/VR/Glasses/q2.webp)

De Quest 2 is een grote verbetering van de Quest 1, Hij is heel erg snel met het opstarten van de headset. De levensduur van de batterij is ongeveer 4 uur als je een spel speelt als een standalone headset. De Quest 2 is stuk beter in het volgen van de controllers waardoor het dus minder vaak voorkomt dat je controllers op een andere plek zijn dan je handen in het spel. Het grootste voordeel dat ik persoonlijk vindt is dat je bij de Quest 2 niet een Gardian hoeft te creeeren om het standaard menu te gebruiken. Dit is een groot voordeel omdat je dan niet alles hoeft in te stellen om even snel te kijken of je alles wel goed hebt achter gelaten. Dit moet nog wel bij de Quest 1

### Oculus Quest 3

![Quest 3](/pictures/Stage/Civon/VR/Glasses/q3.png)

De Quest 3 is heel erg nieuw. Het is een heel goed model. Hij is minder groot maar heeft nog steeds het zelfde gewicht als de Quest 2 dus het volt een stuk zwaarder. Het grootste voordeel aan de Quest 3 is dat hij kleurcamera's heeft waardoor het ook gebruikt wordt voor Mixed reality en niet alleen voor VR. De Quest 2 had ook al wel een klein beetje mixed reality maar het was niet zo fijn om het te doen, De grootste reden hiervoor was dat je nog steeds alles om je heen zag in een zwart wit camera. Deze zwart wit camera voelt net alsof je een video zit te kijken in 240p. Dit is heel erg vervelend als je een spel speelt en alles wat de headset renderd is in 4k en wat de camera ziet is in 240p zwart wit. Dit is erg afleidend maar de Quest 3 heeft dit probleem niet meer. De Quest 3 heeft een 4k kleuren camera waardoor het veel fijner is om mixed reality te doen. Maar doordat je 2 keer een 4k kleuren camera gebruikt boven op het renderen van het spel op de goede plekken in combinatie met de echte wereld wordt de batterij duur een stuk korter, hierdoor is de batterij duur weer terug naar 2 uur bij mixed reality. De Quest 3 heeft ook nog een leuke functie dat hij zelf kijkt naar waar er objecten in je kamer zitten en door deze informatie maakt hij zelf een gardian. Dit betekend dat je zelf niets hoeft te tekenen om een gardian te maken. Eigenlijk hoeft het niet maar is wel leuk om te hebben. Overigens heeft de Quest 3 ook een hele andere controller gemaakt. Deze controller heeft niet meer de ring die de Quest 1 en de Quest 2 wel hebben


## De spellen
Tijdens mijn stage heb ik ook een aantal spellen gespeeld, hierdoor kan ik wat informatie geven over hoe die spellen gebruik maken van de verschillende VR brillen en de technologie die er in zit.

### First Steps

![First Steps banner](/pictures/Stage/Civon/VR/Games/FirstSteps/Banner.jpg)

First steps is een spel dat je leert hoe je de controllers moet gebruiken. Dit spel is gemaakt door Oculus zelf. In dit spel leer je hoe je virtualen handen werken, dingen oppakt en hoe je voorwerpen zoals blokjes kan gooien.

![First Steps hands](/pictures/Stage/Civon/VR/Games/FirstSteps/Hands.jpg)

Op het zelfde moment wordt je ook geinformeerd over de Gardian en waarvoor je moet oppassen. Dit spel is perfect voor als je voor het eerst in VR bezig bent. Natuurlijk gebruiken sommige spelen wel andere knoppen voor het oppakken van voorwerpen maar dan leggen ze dat wel weer uit in het spel zelf. Dit spel wordt automatisch geleverd bij elke Oculus account en is gratis te downloaden. Dit spel maakt geen gebruik van de mixed reality functies.

### Richie's Plank Experience
Richie's Plank Experience is een erorm leuk spel om te spelen. Het is niet echt een spel maar meer een ervaring zoals de titel van het spel ook al aangeeft. Dit spel kan gebruik maken van de mixed reality functies van de Quest 2 en 3.
Eerst ga ik wat uit leggen over het spel als je het niet in mixed reality speeld

#### standaard
Als je het spel speelt zonder mixed reality dan is begin je in een stad met een lift voor je. Je kan meteen de lift in stappen of je kan nog even genieten van je omgeving.

![GroundLevel](/pictures/Stage/Civon/VR/Games/RPE/ground-level.jpg)

Als je in de lift stapt dan krijg je een aantal opties om uit te kiezen. Eigenlijk heb ik alleen de optie om naar de plank te gaan gebruikt dus ik ga alleen over die optie praten. 

![Lift](/pictures/Stage/Civon/VR/Games/RPE/ElevatorInside.jpg)

De plank is een plank die je in de echte wereld kan defineren om het nog echter te maken. Maar hoeft niet, zodra je in de lift naar de plank toe gaat dan zit je een aantal 100 meter boven de grond. Dit is heel erg eng als je hoogtevrees hebt. Als je dan op de plank staat en je hebt er genoeg van dan kan je op 2 manieren weer terug naar beneden. Je kan terug de lift in stappen en op de `Ground` knop drukken of je kan van de plank af springen.

Toen Martin Stor een middag had ingepland voor bezoek bij het civon moesten wij (stagiaires) een klein onderdeel van die dag managen. Dit onderdeel was de plank. Tijdens de tijd daar heb ik weinig personen van de plank af zien stappen omdat ze allemaal hoogtevrees hadden. Dit is een heel erg leuk spel om te spelen maar het is niet voor iedereen weggelegd.

#### Pass through
Nu ga ik wat vertellen over de mixed reality functies van dit spel. In Richie's Plank Experience kan je de mixed reality functies gebruiken om het spel nog realistischer te maken. Dit kan je doen door de camera's van de Quest 2 of 3 te gebruiken om de echte wereld te laten zien. Deze functie is alleen beschikbaar voordat je omhoog gaat in de lift maar is alsnog heel leuk om een keer uit te proberen

![PassThrough](/pictures/Stage/Civon/VR/Games/RPE/Ground-Level-Passthrough.png)

Zo ziet het er uit als je dit op de Quest 3 zou proberen.

### Beat Saber

![Beat Saber banner](/pictures/Stage/Civon/VR/Games/BeatSaber/Banner.jpg)

Beat Saber is een spel waarbij je een aantal blokken moet slaan met een licht zwaard op muziek. Dit spel is heel erg goed voor de oog hand coördinatie. Dit spel is heel erg leuk om te spelen. Dit spel maakt geen gebruik van de mixed reality functies.

### Keep Talking and Nobody Explodes

![Keep Talking and Nobody Explodes banner](/pictures/Stage/Civon/VR/Games/KTANE/Banner.jpg)

Keep Talking and Nobody Explodes is een spel waarbij je een bom moet ontmantelen. Dit spel is heel erg leuk om te spelen met vrienden. Dit spel kan gebruik maken van de mixed reality functies van de Quest 3. Het maakt niet heel veel verschil om het in mixed reality te spelen. Dit komt doordat je alleen bij het uitkiezen van de bom de mixed reality functies gebruikt. Zodra je in het spel zit met de bom dan zie je alleen de bom en gaan de mixed reality functies uit. Dit is heel erg jammer omdat het heel erg leuk zou zijn om de bom in de echte wereld te zien. Dit zou het spel nog realistischer maken, de reden dat ze dit doen is zodat je niet bij de handleiding kan af spieken. Dit spel is heel erg leuk om te spelen met vrienden. Maar dan moet je die wel eerst hebben.

# Slot
Ik heb heel erg veel geleerd tijdens mijn stage bij het Civon. Ik heb geleerd hoe laserlas machines werken. Ik heb geleerd welke eigenschappen de verschillende VR brillen hebben. Ik heb geleerd hoe je Misty kan programmeren. Ik vond het heel erg leuk om bij het Civon stage te lopen. Ik heb heel erg veel geleerd en ik ben van plan om hier nog veel meer over te leren. 

# Bronnen
- [Misty Robotics](https://www.mistyrobotics.com/)
- [Oculus](https://www.oculus.com/)
- [Richie's Plank Experience](toastinteractive.com/games)
- [Beat Saber](https://beatsaber.com/)
- [Keep Talking and Nobody Explodes](https://keeptalkinggame.com/)
- [Bomb Manual](https://www.bombmanual.com/web/index.html)
- [MistyPy](https://www.github.com/joppy-school/MistyPy)
