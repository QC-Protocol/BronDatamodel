Samenvatting
------------
Van startende collega's (al dan niet ervaren) wordt verwacht dat ze:
-	Werken met Visual Studio Code
-	Code voldoet aan industrie standaarden voor syntax en opmaak
-	Veilig omgaan met woorden
-	Code testen
-	Code documenteren
-	Type hints gebruiken
Cursieve stappen worden van absolute beginners niet verwacht. Onze programmeer omgeving (VS Code) kan helpen met bovenstaande punten door er automatisch op te checken. Als je je python project baseert op het basis project (Antea group / basis python project · GitLab (datadropper.nl)) gebruikt worden er automatisch extensies geïnstalleerd die checks uitvoeren.


Visual Studio Code
==================
- Werken met Visual Studio Code
- Visual Studio Code is hier te downloaden: https://code.visualstudio.com/
- Installatie User based uitvoeren (niet program files want veel collega's hebben geen BOW).
- Python downloaden van python.org en installeren als gebruiker.
- In VS Code Python (en andere) addon(s) installeren. Als een (basis) project wordt geopend met een .vscode/extensions.json worden die extensions bijna automatisch geïnstalleerd.

Virtual environment
===================
-	Als je externe pakketten gebruikt installeer je die met  `pip install <pakketnaam>`.
-	Om te voorkomen dat twee verschillende scripts conflicterende pakketten installeren gebruik je altijd een virtual environment.
-	Een virtual environment maak je met: `python -m venv venv`. Dit doe je er project en in dezelfde folder.
-	Als je een script wilt gebruiken moet je de virtual environment activeren. Op de command line doe je dit door `.\venv\Scripts\activate`. VS Code doet dit meestal automatisch. Zo niet kun je dit doen door rechtsonder op python versie te klikken en dan middenboven je venv op te zoeken.
Documentatie: [venv](https://docs.python.org/3/library/venv.html)

Linting
=======
Elke programmeur gebruikt standaard Linters zodat het makkelijk is om aan een standaard opmaak ("black"), veiligheid ("bandit") en naamgeving ("pep8") te conformeren. Beide worden VS Code automatisch toegepast als je het basis project gebruikt.

Gebruikte linters zijn:

- Black: fixt opmaak
- Flake8: checkt pep8
- Isort: Zorgt voor nette volgorde in import
- Bandit: checkt op veiligheids issues

Documentatie: [black](https://github.com/psf/black), [flake8](https://flake8.pycqa.org/en/latest/), [isort](https://pycqa.github.io/isort/), [bandit](https://bandit.readthedocs.io/en/latest/)

Header
======
Zorg dat je de header standaard invoert. Hieronder is het format gegeven. Standaard invoegen kan via extensie. Dit is een kandidaat: caizhengxin/vscodefileheader: VSCode File Header (github.com)
Header inhoud:
```
-*- coding: utf-8 -*-

    @Created on %(date)s

    @author: 		%(username)s
    @script type: 	A eigen gebruik, B script, C tool, D complexe tool (lijstje uit ander document)
    @copyright: 	Antea Group B.V. 2023

    @desc: <typen>
```

Commentaar tekens worden door de plugin aangepast aan de taal/bestandsformaat.

Wachtwoorden en simpele settings
================================
- Deze zetten we niet in de code, maar in een apart bestand genaamd ".env”. Dit  bestand commit je niet in git, dat zou de wachtwoorden alsnog publiek maken.
- [Hier](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) lees je hoe je die vervolgens in je code gebruikt.
- Als je uitgebreide settings voor je script hebt zijn er betere oplossing zoals “configparser” die standaard in python zit. Voor je wachtwoorden blijf je echter de .env gebruiken.
- Testen
- Zodra je script enige serieuze bewerking doet is het goed testen te bouwen. Daarmee kunnen jij en je collega's snel zien of de code nog dezelfde resultaten levert als eerst.
- Gebruik het “pytest” pakket voor je testen. Dat is veel makkelijker dan de ingebouwde “unittest”
- Maak een aparte “tests” directory aan waar je je testen opslaat

Documentatie
============
- Probeer bij elke functie een zogenaamde docstring te schrijven. Dit is de meeste basale documentatie en zeer nuttig als je later nog eens terugkomt bij je code
- In het basis project wordt een extensie geïnstalleerd die automatisch de structuur voor je docstring genereerd op basis van je functie met argumenten. Dit werkt het best als je ook type-hints (zie hieronder) gebruikt.
- De docstring wordt door VS Code bijvoorbeeld getoond als je een functie aanroep aan het typen bent. Da's heel handig om te zien wat bijvoorbeeld de volgorde van argumenten is.

Type hinting
============
- Python gebruikt in zijn simpelste vorm geen types voor zijn variabelen. Als je twee variabelen wil optellen probeert python dat genoeg, er is geen eis dat het beide getallen zijn zoals in andere programmeertalen. De optelling kan nog steeds mislukken omdat python niet weet hoe de variabelen opgeteld moeten worden.
- Om de code-completion van VS code beter te maken kun je wel types specificeren voor bijvoorbeeld de argumenten van een functie.
- Ook de automatische documentatie wordt daar beter van
- Met “mypy” kun je checken of je types gebruikt die worden verwacht, dat kan dan weer problemen in de toekomst voorkomen als je de code anders gebruikt dan initieel voorzien.
Documentatie: [mypy](https://mypy-lang.org/)
