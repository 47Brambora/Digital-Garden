# Pravidla přispívání

Předem ti děkuji, že chceš rozšířit naši krásnou zahradu o nové kousky, nebo se postarat o ty starší.  
Aby byla práce v zahradě příjemná pro všechny, drž se prosím následujících pravidel.


## 1. Žádné duplikáty

Pokud už v zahradě existuje podobná kytka, zkus ji pojmout jinak nebo přidat nový nápad do ní.  

Příklad:  
Tulipán (existuje) >> Tulipán žlutý (změna barvy)  

Bylo by fajn, pokud měníš něco na staré kytce, udržovat nějakou "rodinu" (poddruhy, varianty).  


## 2. Nepoužívej kód, který vytvořil někdo jiný  

Přidávej jenom kód, který jsi vytvořil sám.  
Inspirace je v pořádku - kopírování ne.  


## 3. Podepiš se

Na začátek souboru přidej komentář, pokud to jde, s tvým jménem a e-mailem:  

`# Author: 47Brambora (47Brambora@gmail.com)`  

E-mail je dobrovolný, ale hodí se - hlavně kvůli úpravám cizích kytek.  


## 4. Pojmenuj ji

Není nic horšího než když je něco nepojmenované.  
Vymysli pro svojí kytku jméno. Pokud již existuje tvé kytce podobná. Můžeš vymyslet poddruh.  


## 5. Udržuj pořádek

* Vkládej kytky do správné složky podle technologie
* Pokud si nejsi jistý, nech ji ve výchozí složce a napiš to do PR
* Nové typy kytek → vytvoř novou složku


## 6. Postup práce

### 1. Vytvoř novou větev

Každá změna má mít vlastní větev:
`<akce>/<technologie>-<kytka>`
Např.:
`git checkout -b planting/css-tulip-yellow`

### 2. Přidej kytku

Ulož ji do správné složky.

### 3. Podepiš se

Přidej autora na začátek souboru.

### 4. Udělej screenshot

Vytvoř obrázek (ideálně .png) a vlož ho do:
`gallery/images/`

### 5. Aktualizuj galerii

Do `gallery/GALLERY.md` přidej:

* obrázek
* název
* použitou technologii

### 6. Otevři pull request

Stručně popiš:

* co přidáváš
* proč (pokud jde o úpravu)
* jak to funguje
* případně označ autora původní kytky


## 7. Úprava cizích květin

Chceš upravit kytku, kterou vytvořil někdo jiný?  

 - pokus se kontaktovat autora (pokud uvedl e-mail)  
 - Krátce popiš, co chceš zmenit a proč  
 - pokud autor souhlasí, budeš uveden jako **CO-Author** hned pod ním  

Taky by se ti nelíbilo, kdyby ti někdo v reálné zahradě ostříhal keř bez tvého povolení.  
Díky tomu prosím, aby si původního autora označil v zprávě v pull requestu a on ti to potvrdil.  

Pokud autor **nesouhlasí** nebo není k zastižení, můžeš vytvořit nový poddruh dané květiny.  


## 8. AI  

Chápu, že občas potřebujete pomoci, ale zkuste tvořit sami a bez pomoci umělé inteligence ať v tom je lidská duše a srdce.  
Bránit v tom nebudu a ani nebudu užívat nějaký software na zjišťování.  


## 9. Pull requesty

V každém PR uveď:

 - co přidáváš nebo měníš
 - proč (pokud jde o změnu)
 - jak to funguje
 - jestli zasahuješ do existující struktury
 - označ autora, pokud upravuješ jeho kytku