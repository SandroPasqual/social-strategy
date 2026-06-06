# Devorator — Playbook & Strategy

> Status: DRAFT — în construcție, pe măsură ce decidem.

---

## 1. Produsul

### Ce este

Devorator procesează documente — facturi, bonuri, contracte, CV-uri, orice document birocratic — și extrage automat datele structurate. Începe cu facturi și bonuri, dar se extinde la orice document pe care companiile îl procesează în volume mari.

Un **devorator general de birocrație.** Pasul mare spre digitalizare.

### Ce nu este (încă)

- Nu e un SaaS în cloud. Rulează local, pe un laptop.
- Nu e un generator de facturi. Procesează documente *primite*.
- Nu e un înlocuitor de SAGA. E un strat înainte de SAGA.
- Nu e un produs finit. E în construcție, pre-MVP.

### Viziunea

Pe termen lung, Devorator poate deveni un motor general de procesare documente — foi de parcurs, hârtii vamale, contracte, CV-uri, orice birocrație. Dar acum nu procesează decât un singur lucru:

**Facturi și bonuri de plată.**

Mai întâi perfecționăm ăsta. Apoi următorul.

### Realitatea documentelor în România

- Majoritatea facturilor **nu sunt PDF-uri digitale** — sunt printate, scanate, poze făcute cu telefonul
- Bonurile de plată cash sunt și mai prost gestionate — hârtie termică, poze din telefon, teancuri în sertare
- Devorator TREBUIE să aibă OCR bun de la început. PDF-ul digital e rar.

### Starea actuală

- Codul e scris și funcțional — motor de extracție + parser + portal web
- Are client management, upload, procesare la cerere, validare manuală, export
- Dar **nu e în producție cu clienți reali** — e în lucru, pre-MVP pe piață
- Funcționează pe laptop, accesibil prin Tailscale (tunel privat)
- Zero cloud, zero dependență externă

### Filosofia de construcție

- **Un pas o dată.** Începe cu facturi. Apoi bonuri. Apoi restul.
- **Fără AI ca black box.** Regex + sinonime + reguli explicite. Sistemul știe ce face și de ce.
- **Predictibilitate > automatizare.** Când nu știe, trimite la review — nu ghicește.
- **Totul e privat.** Datele nu părăsesc laptopul utilizatorului.

---

## 2. Numele — "Devorator"

### Percepție în română

"Devorator" e un cuvânt rar, cu rezonanță aproape mitologică. Nu e din vocabularul zilnic — tocmai de aceea iese în evidență. Sună ca ceva care **înghite tot ce i se dă, rapid, fără resturi.**

Pentru un contabil care primește sute de PDF-uri pe lună, senzația e exact asta: dosarul de facturi dispare în sistem, iese curat, structurat, gata de importat.

**Risc potențial:** Pentru un public conservator (contabili), un nume agresiv poate părea neserios. Mitigare prin: identitate vizuală sobră, ton profesionist, livrare tehnică impecabilă. Numele e memorabil — odată auzit, nu se uită.

### Identitate vizuală sugerată

- Curat, funcțional, corporatist-light (gen Notion întâlnește aplicație bancară)
- Culori reci, sigure — albastru sau gri-verde (asocieri cu încredere, finanțe)
- Fără gradienți mov sau elemente startup-ish
- Logo simplu, poate un monogram sau un simbol care sugerează "consumare" discretă

---

## 3. Competitiv — Analiza Pieței

### Competitorul real nr. 1: Introducerea manuală

Nu o firmă, ci un **obicei**. Contabilul primește factura PDF, o deschide, tastează datele în SAGA. E "gratis" — nu costă bani, costă timp. Și pentru 10 facturi/lună, e mai rapid să tastezi decât să înveți un tool nou.

**Când doare cu adevărat:** Peste 100 de facturi/lună. Atunci introducerea manuală devine ore pierdute, greșeli, reclamante de la clienți.

### Competitori direcți în România

| Produs | Ce face | Preț | Specific RO | Concurență directă? |
|--------|---------|------|-------------|---------------------|
| **SmartBill** | Emite facturi în cloud + OCR basic pe cele primite | 30-100 RON/lună | Da — e standard în RO | **Parțial** — are OCR pe facturi primite, dar nu e focusul lor. E o funcție secundară într-un produs de emis facturi. |
| **SAGA C** | Soft contabilitate desktop. Excel import manual | ~500-2000 RON licență | Total | **Nu direct** — SAGA e destinația, nu sursa. Devorator se așază înaintea lui SAGA. |
| **Alfa / WinMentor** | Similar SAGA. Desktop accounting | Similar SAGA | Total | **Nu direct** — aceeași relație ca și cu SAGA. |
| **NexT ERP** | ERP cloud pentru IMM-uri | ~200-500 RON/lună | Parțial | **Nu direct** — e un ERP complet, Devorator e un instrument specializat. |
| **ContApp (ANAF)** | Gratuit, emis/primire facturi | Gratis | Total | **Nu direct** — e pentru e-Factura, nu pentru parsare. |

### Competitori internaționali (indirecți)

| Produs | Preț | Limitare |
|--------|------|----------|
| **Rossum** | ~200-1000 EUR/lună | Prea scump pentru RO. Nu înțelege formatul CUI, SAGA, separator zecimal românesc. |
| **Mindee** | ~0.05-0.10 EUR/pag | API generic. Necesită adaptare la RO. |
| **Docparser** | ~$50-200/lună | Bazat pe reguli configurabile manual. Fără suport RO nativ. |
| **Veryfi** | ~$15-150/lună | Optimizat pentru piața US. Bonuri americane, nu facturi românești. |
| **Nanonets** | ~$100-500/lună | AI generic. Necesită antrenare pe facturi RO. |

### Matricea de diferențiere

| Criteriu | Devorator | Internaționale | Manual |
|----------|-----------|----------------|--------|
| Facturi românești (CUI, SAGA, ; separator, , zecimal) | ✅ Nativ | ⚠️ Parțial/niciodată | ✅ 100% |
| Fără cloud / datele pe laptop | ✅ Da | ❌ Cloud obligatoriu | ✅ Da |
| Setup | Minute | Zile-săptămâni | Zero |
| Preț accesibil RO | ✅ ? | ❌ €200+/lună | "Gratis" |
| Review uman când nu e sigur | ✅ Da | ❌ Black box | — |
| Export direct SAGA | ✅ De construit | ❌ | — |
| Scalabil (500+ facturi/lună) | ✅ Da | ✅ Da | ❌ Nu |
| Fără dependență de API extern | ✅ Da | ❌ API third-party | — |

### Poziționare recomandată

> **Devorator = primul tool românesc de procesare facturi primite care rulează pe propriul tău calculator, fără cloud, fără abonament lunar, fără să învețe sistemul altcuiva cum arată o factură românească.**

Pivotul central: **Nu e "AI-ul care face totul". E "tool-ul care face o singură treabă și o face bine: extrage datele din factură exact acolo unde vrei tu."**

---

## 4. Publicul Țintă

### Segmente pe verticală

1. **Contabil independent** — 1 persoană, 10-50 clienți, 50-300 facturi/lună. Cea mai frecventă durere: timpul pierdut cu tastat.
2. **Cabinet mic de contabilitate** — 2-5 contabili, 50-200+ clienți, sute de facturi/lună. Durerea: productivitatea echipei, erori de tastare.
3. **Departament financiar IMM** — 1-3 persoane, firma procesează intern. Durerea: reconcilieri, intrări multiple.

### Geografie

- **Acum:** România. Exclusiv. Produsul e construit pentru RO.
- **Mai târziu:** După maturizare, extindere pe piețe cu specific similar (Bulgaria, Ungaria, Polonia — format CUI, separator zecimal, TVA multiplu).

---

## 5. Modelul de Preț — Propunere

### Filosofie

Nu știm suficiente despre piață să fixăm prețul din birou. Îl descoperim vorbind cu contabilii. Până atunci, conturăm **arhitectura**, nu cifrele.

### Arhitectura pe 3 straturi

**Stratul 1 — Gratuit permanent (pâine)**
Contabilul primește un număr de documente/lună procesate gratis, pentru totdeauna. Nu expiră. E suficient cât să vadă că funcționează și să-și bage clienții în sistem.

**Stratul 2 — Tokeni (volum)**
Peste limita gratuită, cumperi pachete de tokeni. Un token = un document procesat. Tokenii nu expiră.

**Stratul 3 — Pachete de volum**
Pentru cabinete mari sau companii cu volume mari — preț negociabil per token, plafoane lunare.

### Cele 2 variante de procesare

| Varianta | Ce face | Preț/token | Termen |
|----------|---------|------------|-------|
| **Self-verify** | Engine-ul extrage. Contabilul verifică și corectează manual. | Mai mic | Instant |
| **Verified** | Cineva (tu/operator) verifică înainte de livrare. | Mai mare | 1-2 zile |

### Early adopters (cei care intră în faza de dezvoltare)
- Limită gratuită mai mare permanent
- Sau preț redus per token pe viață
- Acces direct la tine pentru feedback fără tickete, fără complicații

### Noi clienți (după lansare)
- Primele 3 luni: limită gratuită mai mare (să-și importe istoricul, să se obișnuiască)
- Apoi tokeni

### Cum stabilim prețul real
Nu din teorie. Din teren:

1. Pagina Facebook + grupuri → întrebare: "Câte facturi procesați pe lună?"
2. Din răspunsuri știm volumele reale
3. Prima postare poate fi chiar asta: "Voi câte facturi procesați pe lună?"
4. După 2-3 săptămâni de discuții cu contabili reali, prețul se conturează singur

Până atunci, în playbook scriem DOAR arhitectura (gratuit + tokeni + self-verify/verified). Cifrele le punem când avem date.

---

## 6. Vocea Devoratorului

### Personality: The Professional Tool

Nu un personaj. Nu o voce cu atitudine. O **prezență** — sigură, exactă, profesionistă.

### Principii centrale

1. **Exact, nu metaforic.** Spui exact ce face. Fără "transformăm", "revoluționăm", "empower-uim". Fapte, nu promisiuni.
2. **Respect față de profesia de contabil.** Omul care folosește Devorator își câștigă existența din contabilitate. Nu e amuzant, nu e ironic — e serios.
3. **Sinceritate tehnică.** Când nu știe, spune "nu știu" (trimite la review). Asta e diferențiator, nu slăbiciune.
4. **Zero jargon de marketing.** Nu "soluție inovatoare de automatizare". Ci "extrage datele din factură și le pune în Excel".

### Cum sună Devorator

| Situație | Ce spune | Ce NU spune |
|----------|----------|-------------|
| Prezentare | "Procesează facturi PDF și imagine. Extrage automat: număr, date, furnizor, articole, TVA, totaluri." | "Soluția AI care revoluționează contabilitatea" |
| Ce-l diferențiază | "Rulează pe calculatorul tău. Nu în cloud. Nu învăța alt sistem cum arată o factură românească." | "Singurul tool cu machine learning avansat" |
| Limitare | "Dacă factura e scrisă de mână sau ruptă, nu promitem că o citește corect. O trimite la verificare." | "AI extrage orice document instant" |
| Preț | "50 RON/lună. Fără contract. Anulezi când vrei." | "Investiție care se amortizează în prima lună" |
| Hârtia | "O factură care ajunge direct în format electronic nu mai trebuie scanată, tipărită, arhivată fizic. Ghinionul e că majoritatea tot ajung pe hârtie. Devorator face următorul pas: odată intrată în sistem, nu mai iese." | "Salvăm pădurile împreună" |

### Structura unei postări / comunicări

1. **Problema concretă** — "Câte facturi tastezi manual într-o lună?"
2. **Ce face Devorator** — "Le încarci. Le procesezi. Le exporti. Atât."
3. **Dovada / modul** — (screenshot, comparație, demonstrație)
4. **Cine are nevoie** — "Dacă ai peste 50 de facturi pe lună, merită să vezi cum merge."
5. **Fără CTA forțat** — "Pagina: facebook.com/devorator." Atât.

### Ce nu spune Devorator niciodată

- "AI" (prea vag, prea uzat)
- "Revoluționar" (prea mult)
- "Singurul" (prea fals)
- Glume despre contabili sau birocrație
- Ironie la adresa ANAF sau a sistemului
- Promisiuni de tipul "100% automat"

---

## 7. Strategie Socială — Facebook

### De ce Facebook

- Contabilii români sunt activi în grupuri de Facebook (10k-50k membri fiecare)
- Acolo se plâng de tool-uri, întreabă recomandări, împărtășesc frustrări
- LinkedIn e gol pentru această categorie profesională în RO
- O pagină de produs pe Facebook e suficientă pentru început

### Conținut — 3 Piloni

**Pilonul 1: Demonstrații (50%)**
- Screenshot-uri reale din Devorator
- "Am încărcat o factură. Uite ce a ieșit."
- Comparații: original PDF → date extrase
- Video scurt cu procesul (telefon, nu producție)
- Fără scripturi, fără efecte — arăți exact ce vede utilizatorul

**Pilonul 2: Probleme reale (30%)**
- Cât timp se pierde cu tastat manual
- Greșeli frecvente la introducerea datelor
- Diferența între o factură PDF și una scanată (și de ce unele sunt mai grele)
- Educație: cum ar trebui să arate o factură ca să fie procesabilă

**Pilonul 3: Produsul (20%)**
- Actualizări, funcții noi
- Răspunsuri la întrebări din comentarii
- Anunțuri (beta, lansare, preț)
- Întrebări către comunitate: "Ce tip de factură e cel mai greu de procesat pentru tine?"

### Frecvență

- **La început:** 2-3 postări/săptămână
- **După lansare:** 1-2 postări/săptămână
- **Story:** zilnic în perioade active de dezvoltare (screenshot-uri, mici progrese)

### Prezența în grupuri

Nu posta reclame în grupuri. Intră natural:

1. Cineva se plânge: "Am 200 de facturi de introdus în SAGA"
2. Răspunzi: "Încerci să le bagi manual pe toate? Noi facem asta automat. Dacă vrei, testăm pe 10 facturi să vezi cum merge."
3. Nu minți, nu ascunzi — ești sincer util

### Cronologia lansării

| Faza | Acțiune | Durată |
|------|---------|--------|
| **1. Pre-lansare** | Pagina creată. Postări despre problemă, nu despre produs. Construiești context. "Câte ore pierzi pe lună tastând facturi?" | 2-4 săptămâni |
| **2. Beta deschisă** | Anunți că poți procesa gratuit primele facturi (nu 100, ci un număr rezonabil). Cere feedback real. | 4-8 săptămâni |
| **3. Lansare** | Preț anunțat. Primii clienți plătitori. | După beta |
| **4. Creștere** | Testimoniale, cazuri de utilizare, optimizări. | Continuu |

---

## 8. Distribuție & Vânzare

### Canale

1. **Facebook — pagina Devorator** — conținut organic, prezență
2. **Grupuri Facebook de contabilitate** — engagement natural, nu spam
3. **Recomandări din gură în gură** — primii utilizatori mulțumiți aduc următorii
4. **Parteneriate cu implementatori SAGA** — consultantul care instalează SAGA la firmă poate recomanda Devorator ca "add-on"

### Oferta de pornire

Nu "primele 100 facturi gratis" (nerealist). Ci:

> "Primele 30 de facturi le procesăm noi. Dacă economisești timp, rămâi."

Sau:

> "O lună de test. Procesezi câte facturi vrei. La final, decizi dacă plătești mai departe."

---

## 9. Următorii Pași

- [ ] Confirmat: nume pagină Facebook = "Devorator"
- [ ] Creată pagina
- [ ] Stabilit prețul final
- [ ] Scris primele 5 postări (plan editorial săptămâna 1)
- [ ] Identificate 3 grupuri Facebook de contabilitate ca target
- [ ] Prima postare în grup (natural, nu reclamă)
- [ ] Beta cu 2-3 contabili reali
- [ ] Feedback → ajustat produsul
- [ ] Lansare

---

*Document creat: 6 iun 2026. Se actualizează pe măsură ce decidem.*
