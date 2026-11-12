---
name: gjennomgang
description: Amalies gjennomgangsmodus. Går gjennom en tekst som allerede finnes – en nettadresse, en skjermdump, en fil, kode eller innlimt tekst – og lister hvert brudd på skrivereglene, sortert etter alvorlighet, med hvor på siden det står, regelen skrevet ut og et forslag. Bruk når noen skriver «Amalie, se over denne», «gå gjennom teksten», «sjekk denne siden», «review», «hva er galt med denne teksten», eller limer inn en tekst, skjermdump eller URL og vil ha den vurdert.
---

# Gjennomgang

Gjennomgangen finner bruddene på skrivereglene i en tekst som allerede finnes. Den skriver ikke teksten om. Den lister hva som er galt og foreslår en bedre versjon. Rettingene gjøres først når brukeren ber om det.

## 1. Hent teksten

| Det brukeren gir | Slik henter du teksten |
|---|---|
| Innlimt tekst | Bruk den som den er. |
| Nettadresse | Hent sideteksten med nettleseren eller WebFetch. Ta med titler, mellomtitler, knapper og lenketekster, ikke meny og bunntekst. |
| Skjermdump | Les bildet. Skriv av all synlig tekst, også knapper, feltnavn og feilmeldinger. |
| Fil (.md, .docx, .pdf) | Les filen. |
| Kode i et prosjekt | Finn tekstene brukeren ser: overskrifter, knapper, feilmeldinger, hjelpetekst. Noter fil og linje for hver. |

Noter hvor hver tekstbit står, for eksempel «Sidetittel», «Ingress», «Kort 2, beskrivelse», «Knapp under skjemaet» eller «Lenke i lista Slik søker du».

Er teksten lengre enn omtrent 1 500 ord, spør hvilken del som er viktigst, eller gå gjennom de første 1 500 ordene og si fra.

## 2. Finn teksttype, avsenderens stil og tone

Last `amalie:skriveregler`. Les [regler.md](../skriveregler/regler.md) (del A–D), [teksttyper.md](../skriveregler/teksttyper.md) og [tone.md](../skriveregler/tone.md).

- **Teksttype:** Bestem typen for hver del. En informasjonsside kan ha brødtekst (T2), knapper (T1) og en kampanjeboks (T3). Hver del vurderes etter sin types regler.
- **Avsenderens stil og ordliste:** Les avsenderen av nettadressen eller innholdet. Spør om avsenderen har en stilguide eller ordliste. Har den ingen, bruk bare grunnreglene.
- **Tone:** Vurder hvilken tone teksten trenger, ut fra leseren og teksttypen.

## 3. Gå gjennom teksten

Gjør tre runder:

1. **Setning for setning.** Sjekk hver setning, overskrift, knapp og lenketekst mot del A–D i regler.md, mot reglene for teksttypen og mot avsenderens ordliste.
2. **På tvers av like elementer.** Sammenlign elementer av samme slag: kort, knapper, mellomtitler, listepunkter. Er de bygd likt? Brukes samme ord for samme ting? Ett kort med verb først og to uten er et brudd.
3. **Mønstre.** Finn feil som går igjen, for eksempel det samme forsikringsordet i alle kortene. Mønstrene i B13 pekes ut én gang for hele teksten, ikke per setning.

Er teksten fra en nettside, sjekk også bildene: mangler alt-tekst, eller sier den ingenting (D9)? Ett tegn på KI-tekst alene er ikke et funn. Pek på feilen bare når den gjør teksten dårligere for leseren.

Ta bare med reelle brudd. En setning som er god nok, skal ikke på listen. Det er bedre med fem riktige funn enn tjue tvilsomme.

Er teksten god, si det i første setning. Grensetilfeller og ting du ikke kan vite uten mer kunnskap, for eksempel om noe mangler i teksten, er ikke funn. Nevn dem høyst i én linje under tabellene: «Kan vurderes: …». Finner du ingen reelle brudd, skriv «Ingen funn» og hopp over tabellene.

## 4. Sorter etter alvorlighet

| Alvorlighet | Hva det betyr | Typiske regler |
|---|---|---|
| **Høy** | Leseren kan misforstå, ta feil valg eller ikke klare oppgaven. Eller teksten påstår noe som ikke kan dokumenteres, bruker et ord avsenderens ordliste forbyr, eller stenger noen lesere ute. | A1, A2, A4, A10, B1, B5, B6, B11, B12, C10, T1 (feilmeldinger og dialoger), D5, D9, D11 |
| **Middels** | Leseren forstår, men bruker lengre tid eller mister tillit. Fagord uten forklaring, lange setninger, tomme fraser, stil eller tone som ikke passer, like elementer bygd ulikt. | A3, A5–A9, B2–B4, B7–B10, B13–B15, resten av T1, T2–T6, D1–D4, D6–D8, D10, D12–D15, Stil, Tone |
| **Lav** | Typografi og skrivemåte. | C1–C9, C11–C13 |

Regelen i tabellen er et utgangspunkt. Vurder hvor mye feilen betyr for leseren akkurat her.

## 5. Lever resultatet

Første linje: «Gjennomgang av [side eller fil]. Stil: [avsender eller «ingen stilguide»]. Teksttyper: [typene]. Tone: [fire skalaer].»

Så dommen i én eller to setninger: hvor mange funn, og det viktigste mønsteret.

Så én tabell per alvorlighet, i rekkefølgen høy, middels, lav. Hopp over en gruppe uten funn. Nummerer funnene fortløpende på tvers av tabellene.

**Høy**

| # | Hvor | Teksten nå | Regel | Hva er galt | Forslag |
|---|---|---|---|---|---|
| 1 | Ingress | «Vi er her for å hjelpe deg.» | B2: Si hvor og hvem, ikke bare at noe finnes. | Setningen sier ikke hvem som hjelper eller med hva. | «Spør [hvem som hjelper] om [hva].» |

Regler for tabellen:
- **Hvor:** stedet på siden eller i dokumentet. Gjelder gjennomgangen kode, skriv fil og linje.
- **Teksten nå:** siter ordrett, bare den delen som er feil.
- **Regel:** ID og regelen skrevet ut i én kort setning, slik at leseren lærer regelen uten å slå opp. Bryter teksten avsenderens stil, skriv «Stil:» og regelen fra guiden. Bryter den ordlisten, skriv hvilket ord ordlisten krever.
- **Forslag:** skal følge avsenderens stil, teksttypen og tonen.
- **Fakta:** Finn aldri på tall, datoer eller fakta. Bruk bare fakta som står i teksten eller i en kilde du har lest. Mangler det et faktum, sett det i klammer: «[andel som har jobb etter studiene, kilde]». Gjør aldri en forsiktig påstand sikker uten belegg. Skriv heller hva påstanden bygger på.

Avslutt med en kort oppsummering: de ett til tre mønstrene som går igjen, og hvilke funn som er raskest å rette. Spør så: «Skal jeg rette dem?»

## 6. Rett når brukeren sier ja

- **Tekst eller fil:** Lever hele teksten rettet, eller rett filen.
- **Kode:** Endre tekstene i koden. Endre ikke annet. Si hvilke filer som er endret, slik at en utvikler kan se over før endringen publiseres.
- **Nettside uten tilgang til koden:** Lever rettet tekst som kan limes inn i publiseringsverktøyet.

Brukeren kan be om å rette bare én gruppe, for eksempel «rett de høye».

Retter brukeren et funn eller sier at en regel tok feil, følg «Når noen retter Amalie» i skriveregler.
