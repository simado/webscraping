# Duomenų surinkimas iš svetainės naudojant `Python`

## 1. Aruodas.lt
Šis scraperis buvo sukurtas [Ml projektui](https://github.com/simado/busto-kainos) nustatančiam Vilniaus nekilnojamojo turto(butų) kainas.

[aruodas.lt](https://github.com/simado/webscraping/tree/master/aruodas.lt) esančioje direktyvoje rasite:

```
  .
  |--- butai.py
  |--- butai_nuomai.csv
  |--- butai_pardavimui.csv
  |--- requirements.txt
```

1) `butai.py`: kodą surenkantį info apie tiek parduodamų, tiek nuomojamų būtų skelbimus. Pakeitus scrapinamą **URL**                         galime pritaikyti kodą ir kitiems miestams ir/ar namams.

2) `butai_nuomai.csv`: kodo išeiga - pavyzdys kaip atrodo surinkti duomenys apie nuomojamus būstus.

3) `butai_pardavimui.csv`: kodo išeiga - pavyzdys kaip atrodo surinkti duomenys apie parduodamus būstus.

4) `requirements.txt`: naudojamų bibliotekų sarašas.

### Reikalingos bibliotekos:

Kodui naudojamos šios bibliotekos:
```
bs4
requests
pandas
```
Naudojant kodą asmeniniams tikslams galite pasinaudoti `requirements.txt`failu ir automatiškai įsidiegti visas reikalingas bibliotekas į savo VENV:
```
pip install -r requirements.txt
```
