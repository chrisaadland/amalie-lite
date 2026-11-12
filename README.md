# Amalie Lite

Amalie Lite er en skriveassistent for Claude som hjelper deg å skrive klar norsk tekst. Hun er oppkalt etter forfatteren Amalie Skram, som skrev nøkternt og uten pynt.

Amalie gjør to ting:

- **Skriver tekst** etter faste regler for klarspråk: det viktigste først, korte setninger, konkrete ord og «du» til leseren.
- **Går gjennom tekst du allerede har.** Du får en tabell med det som bør rettes, sortert fra alvorlig til lite viktig. Hver rad viser hvor i teksten feilen står, hvilken regel den bryter og et forslag til bedre tekst.

Du bruker henne ved å skrive navnet hennes til Claude:

> Amalie, se over denne teksten: …

> Amalie, skriv en e-post til borettslaget om dugnaden 12. mai.

## Installer i Claude-appen (claude.ai eller desktop)

1. Last ned [amalie-lite.zip](https://github.com/chrisaadland/amalie-lite/releases/latest/download/amalie-lite.zip).
2. Åpne Claude og gå til **Innstillinger → Capabilities → Skills**.
3. Velg **Upload skill** og last opp zip-filen.
4. Skriv «Amalie, se over denne: …» i en ny samtale.

Skills må være slått på i kontoen din. Finner du ikke Skills under Innstillinger, er funksjonen ikke tilgjengelig på abonnementet ditt.

## Installer i Claude Code

Skriv disse to kommandoene i Claude Code:

```
/plugin marketplace add chrisaadland/amalie-lite
```

```
/plugin install amalie@amalie-lite
```

Start Claude Code på nytt etterpå.

## Hva reglene bygger på

Reglene bygger på norske kilder først: Språkrådet, NAV, Skatteetaten, Digdir og Uutilsynet. Der de norske kildene mangler, bygger reglene på GOV.UK, Microsoft, Atlassian, Shopify, Mailchimp og Nielsen Norman Group. Hele listen står nederst i [regler.md](skills/skriveregler/regler.md).

| Fil | Hva den inneholder |
|---|---|
| [regler.md](skills/skriveregler/regler.md) | Grunnreglene: klart språk, vanlige feil, typografi, og tekst som virker for alle lesere |
| [teksttyper.md](skills/skriveregler/teksttyper.md) | Egne regler for knapper og feilmeldinger, nettsider, markedsføring, nyheter, e-post og rapporter |
| [tone.md](skills/skriveregler/tone.md) | Hvordan tonen tilpasses, fra leken til formell |
| [stilguide-mal.md](skills/skriveregler/stilguide-mal.md) | Mal for å lage en stilguide, for eksempel for en arbeidsplass eller en forening |
