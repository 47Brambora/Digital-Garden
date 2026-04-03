# Pravidla přispívání

Díky, že chceš rozšířit naši krásnou zahradu o nové kousky, nebo se postarat o ty starší.  
Aby byla práce v zahradě příjemná pro všechny, drž se prosím následujících pravidel.


## 1. Žádné duplikáty

Pokud už v zahradě existuje podobná kytka, zkus ji rozšířit nebo pojmout jinak.

**Příklad:**
Tulipán → Tulipán žlutý

Pokud upravuješ existující kytku, snaž se zachovat její „rodinu“ (varianty, poddruhy).


## 2. Piš vlastní kód

Přidávej pouze kód, kterému rozumíš a který jsi vytvořil sám.
Inspirace je v pořádku — kopírování ne.


## 3. Podepiš se

Na začátek souboru přidej komentář:

`# Author: TvojeJméno (email@example.com)`

E-mail je dobrovolný, ale hodí se (např. pro domluvu úprav).


## 4. Pojmenuj kytku

Každá kytka by měla mít své jméno.
Pokud už existuje podobná, vytvoř poddruh nebo variantu.


## 5. Udržuj pořádek

 - Vkládej kytky do správné složky podle technologie
 - Pokud si nejsi jistý, nech ji ve výchozí složce a napiš to do PR
 - Nové typy kytek → vytvoř novou složku


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

 - obrázek
 - název
 - použitou technologii

### 6. Otevři pull request

Stručně popiš:

 - co přidáváš
 - proč (pokud jde o úpravu)
 - jak to funguje
 - případně označ autora původní kytky


## 7. Úprava cizích květin

Chceš upravit cizí kytku?

 - zkus kontaktovat autora
 - popiš, co chceš změnit a proč
 - pokud souhlasí, budeš uveden jako **Co-Author**

Pokud autor:

 - nesouhlasí
 - nebo není dostupný

→ vytvoř nový poddruh.


## 8. AI  

Použití AI je povoleno, ale:

 - měl bys rozumět tomu, co přidáváš
 - snaž se tvořit co nejvíc vlastní práci
 - AI užívej jen jako výpomoc


## 9. Pull requesty

V každém PR uveď:

 - co přidáváš nebo měníš
 - proč (pokud jde o změnu)
 - jak to funguje
 - jestli zasahuješ do existující struktury
 - označ autora, pokud upravuješ jeho kytku


## 10. Commit zprávy

Pro přehlednou historii používej zahradnické prefixy:

- `plant:` — nová kytka nebo nový soubor  
- `grow:` — vylepšení existující kytky  
- `prune:` — úklid, mazání, opravy, refaktor  
- `gallery:` — přidání nebo úprava obrázků či GALLERY.md  
- `structure:` — změny ve složkách, přesuny, přidání .gitignore apod.  
- `docs:` — úpravy dokumentace (README, CONTRIBUTING, šablony)

**Příklad:** `plant: add yellow tulip (CSS)`


## 11. Pojmenování větví

Každá změna by měla mít vlastní větev. Používáme jednoduchý a jednotný systém pojmenování:

`<akce>/<technologie>-<kytka>`

### Typ akce
- `planting` — přidání nové kytky  
- `growing` — vylepšení existující kytky  
- `pruning` — úklid, mazání, opravy  
- `structuring` — změny ve složkách, přesuny  
- `documenting` — úpravy dokumentace  
- `gallery` — práce s obrázky a GALLERY.md  

### Příklady větví
- `planting/css-tulip-yellow`  
- `growing/python-rose-red`  
- `pruning/js-daisy-cleanup`  
- `structuring/svg-folder-move`  
- `documenting/docs-readme-update`  
- `gallery/images-tulip-add`


---

A teď už nezbývá nic jiného než nechat zahradu růst
