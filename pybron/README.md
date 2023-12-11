Samenvatting
------------

Van startende collega's (al dan niet ervaren) wordt verwacht dat ze:
- Werken met Visual Studio Code
- Visual Studio Code is hier te downloaden: https://code.visualstudio.com/
- Installatie User based uitvoeren (niet program files want veel collega's hebben geen BOW).
- Python downloaden van python.org en installeren als gebruiker.
- In VS Code Python (en andere) addon(s) installeren. Als een (basis) project wordt geopend met een .vscode/extensions.json worden die extensions bijna automatisch geïnstalleerd.

Linting
=======
Elke programmeur gebruikt standaard Linters zodat het makkelijk is om aan een standaard opmaak ("black"), veiligheid ("bandit") en naamgeving ("pep8") te conformeren. Beide worden VS Code automatisch toegepast als je het basis project gebruikt.

Gebruikte linters zijn:

- Black: checkt opmaak
- Flake8: checkt pep8
- Isort: Zorgt voor nette volgorde in import
- Bandit: checkt op veiligheids issues

Header
======
o	Zorg dat je de header standaard invoert. Hieronder is het format gegeven. Standaard invoegen kan via extensie. Dit is een kandidaat: caizhengxin/vscodefileheader: VSCode File Header (github.com)
o	Header inhoud:
-*- coding: utf-8 -*-

@Created on %(date)s

@author: 		%(username)s
@Last edited on: 	%(date)s
@script type: 	A eigen gebruik, B script, C tool, D complexe tool (lijstje uit ander document)
		@copyright: 	Antea Group B.V. 2023

		@desc: <typen>

Commentaar tekens worden door de plugin aangepast aan de taal/bestandsformaat.

•	Wachtwoorden en simpele settings
o	Deze zetten we niet in de code, maar in een apart bestand genaamd ".env”. Dit  bestand commit je niet in git, dat zou de wachtwoorden alsnog publiek maken.
o	Hier: Using .env Files for Environment Variables in Python Applications - DEV Community lees je hoe je die vervolgens in je code gebruikt.
o	Als je uitgebreide settings voor je script hebt zijn er betere oplossing zoals “configparser” die standaard in python zit. Voor je wachtwoorden blijf je echter de .env gebruiken.
•	Testen
o	Zodra je script enige serieuze bewerking doet is het goed testen te bouwen. Daarmee kunnen jij en je collega's snel zien of de code nog dezelfde resultaten levert als eerst.
o	Gebruik het “pytest” pakket voor je testen. Dat is veel makkelijker dan de ingebouwde “unittest”
o	Maak een aparte “tests” directory aan waar je je testen opslaat
•	Documentatie
o	Probeer bij elke functie een zogenaamde docstring te schrijven. Dit is de meeste basale documentatie en zeer nuttig als je later nog eens terugkomt bij je code
o	In het basis project wordt een extensie geïnstalleerd die automatisch de structuur voor je docstring genereerd op basis van je functie met argumenten. Dit werkt het best als je ook type-hints (zie hieronder) gebruikt.
o	De docstring wordt door VS Code bijvoorbeeld getoond als je een functie aanroep aan het typen bent. Da's heel handig om te zien wat bijvoorbeeld de volgorde van argumenten is.
•	Type hinting
o	Python gebruikt in zijn simpelste vorm geen types voor zijn variabelen. Als je twee variabelen wil optellen probeert python dat genoeg, er is geen eis dat het beide getallen zijn zoals in andere programmeertalen. De optelling kan nog steeds mislukken omdat python niet weet hoe de variabelen opgeteld moeten worden.
o	Om de code-completion van VS code beter te maken kun je wel types specificeren voor bijvoorbeeld de argumenten van een functie.
o	Ook de automatische documentatie wordt daar beter van
o	Met “mypy” kun je checken of je types gebruikt die worden verwacht, dat kan dan weer problemen in de toekomst voorkomen als je de code anders gebruikt dan initieel voorzien.

Al deze dingen zijn te vinden is het basis project: Antea group / basis python project · GitLab (datadropper.nl)

 


Motivatie:

Python interpreter:
I&I levert sterk verouderde versies. De windows-store versie is voor sommige niet beschikbaar(?). Versie van python.org downloaden en installeren kan. Dus de laatste is aan te raden.

Linting e.d.
	Linters	Uitzonderingen	Regellengte	Afgedwongen
Infra	Pep-8?	W293, E402, E722, W391, E221, W504, W291, W292, E203, E228, E272, E701  	120
Zolderkamer	Black, isort			Bij opslaan (vscode extensie)
Datadropper	Flake8, black, isort, bandit	E88	88	Met pre-commit en in pipeline


Headers:
o	Header Infra:
Copyright en licentie zijn andere dingen. Status blijkt uit git branch of versie nummer.
o	Header Datadropper: geen standaard…
o	Header Zolderkamer:

Type hinting
Docstring
Mypy (basic settings)
Python.env voor wachtwoorden e.d.
Tests directory

Eventueel tests en coverage in de pipeline
