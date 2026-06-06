# Devorator — Playbook & Strategy

> Status: DRAFT — în construcție, pe măsură ce decidem.

---

## 1. Produsul

### Ce este

Documente **verificabile matematic** — facturi, bonuri, ordine de plată, foi de vărsământ. Acolo validăm singuri (total = sumă articole, TVA = bază × cotă) și știm dacă am extras corect.

Nu procesăm documente narative (procese-verbale, cereri, opisuri) — doar unde există calcule de verificat.

Parserul se dezvoltă continuu pe măsură ce întâlnește documente reale. Dacă un tip de document apare frecvent, scriem parser dedicat.

**Termenii extrași sunt reali** — căutăm corecturi pe baza calculelor matematice, nu inventăm. Dacă suma totală e calculabilă din articole, o verificăm și ajustăm.

### Arhitectura rețelei — cum se conectează clienții

Nu există server public, nu există cloud, nu există expunere pe internet.

**Conexiunea e o rețea privată între 3 părți:**
- Clientul (firma care primește facturi)
- Contabilul (care procesează documentele)
- Devorator (motorul)

Prin **Tailscale** (tunel WireGuard criptat), fiecare primește un IP privat stabil.
Clientul se loghează de pe **calculator personal sau telefon**, încarcă documentele direct din browser — fără să-și mai facă griji că a pierdut o factură, că n-a gestionat-o bine, că a uitat să o trimită.

**Zero leak. Zero expunere publică. Zero configurari.**

### Ce nu este (încă)

- Nu e un SaaS în cloud. Rulează local.
- Nu e un generator de documente. Procesează documente *primite*.
- Nu e un produs finit. E în construcție, pre-MVP.
- Nu e un serviciu de verificare umană încă. Pentru început, doar parsare automată.

### Viziunea

**Devorator procesează 4 tipuri de documente:** facturi, bonuri de plată, ordine de plată interbancare, foi de vărsământ. Mai întâi perfecționăm astea. Apoi extindem.

### Realitatea în teren (de descoperit)

Câte facturi sunt digitale vs printate, câte bonuri, câte sunt transmise pe mail vs hârtie — **nu știm încă.** Asta aflăm de la primii contabili cu care vorbim.

Ce știm sigur:
- Devorator procesează orice format: PDF digital, scanat, poză, bon termic
- Aplică **5 metode de parsare** a fiecărui document, fără implicare umană, și alege automat cea mai bună combinație
- Se îmbunătățește permanent pe măsură ce procesează documente reale și primește feedback

### Starea actuală

- Codul e scris și funcțional — motor de extracție + parser + portal web
- Are client management, upload, procesare la cerere, validare matematică automată, export
- Documentele eșuate ajung în folder dedicat cu raport de eroare
- Dar **nu e în producție cu clienți reali** — e în lucru, pre-MVP pe piață
- Accesibil prin Tailscale (tunel privat)
- Zero cloud, zero dependență externă

### Filosofia de construcție

- **Un pas o dată.** Începe cu ce e verificabil matematic. Apoi extindem pe măsură ce întâlnim documente reale.
- **Adaptabilitate prin cod.** Dacă un tip de document apare frecvent, scriem parser dedicat. Platforma se îmbunătățește cu fiecare document procesat.
- **Fără promisiuni false.** Nu garantăm că documentele sunt perfect parsate. Pot apărea erori. Când se întâmplă, încercăm să le rezolvăm sau notificăm utilizatorul.
- **Onestitate.** Nu garantăm decât calculul matematic. Restul e responsabilitatea utilizatorului să verifice.
- **Raportare transparentă.** Dacă în factură apar prescurtări pe care sistemul nu le-a înțeles, clientul e notificat în raportul acelei facturi. Dacă matematic s-a verificat, documentul e acceptat — dar cu mențiunea că **obiectul vânzării nu a fost înțeles.**
- **Totul e privat.** Datele nu părăsesc rețeaua privată.

### Pregătirea imaginilor — cum funcționează parsarea

Sistemul analizează și pregătește fiecare imagine înainte de parsare:

1. **Analiză histogramă** — măsoară luminozitatea medie, contrastul, raportul pixeli întunecați/luminoși
2. **Redimensionare** — dacă imaginea e mai mare de 2400px pe latura lungă, o reduce
3. **5 metode de parsare**, alese automat pe baza analizei:

| Categorie imagine | Variante aplicate |
|-------------------|-------------------|
| Luminoasă (fond alb) | contrast 1.8x + sharp 2.0x + threshold 160 |
| | sharp 2.5x + threshold 200 |
| Întunecată (text alb pe negru) | invert + contrast 1.8x + threshold 160 |
| | invert + contrast 2.5x + sharp 3.0x + threshold 180 |
| Contrast slab (bonuri termice) | median filter (denoising) + contrast 2.5x + sharp 3.0x + threshold 180 |
| | contrast 3.0x + sharp 3.0x + threshold 200 |
| Default (caz general) | contrast 1.8x + sharp 2.0x + threshold 160 |
| | contrast 2.5x + sharp 3.0x + threshold 200 |

4. **3 variații ale algoritmului de parsare** — fiecare tratează diferit modul în care textul e grupat pe pagină
5. **Scor calitate** (0-100) — după fiecare încercare, sistemul evaluează rezultatul. Dacă scorul ≥ 50, se oprește și nu mai încearcă restul.
6. **Dacă tot eșuează** → folder documente eșuate + raport cu cauza exactă (de ex: "Câmpul total nu a putut fi identificat")

### Îmbunătățiri identificate

Analiza completă a preprocesării imaginilor a fost documentată tehnic în `docs/ocr-image-preprocessing.md` (proiectul Devorator). Rezumatul modificărilor sugerate:

| Funcție | Prioritate | Efect |
|---------|------------|-------|
| **Deskew (corecție înclinare)** | 1 | O imagine înclinată 2-5° distruge coloanele. Corecția automată înainte de parsare. |
| **Thresholdare Otsu** | 1 | Pragurile fixe eșuează pe expunere neuniformă. Otsu alege optimul după histogramă. |
| **Auto-orientare** | 1 | Detectează sus-jos și corectează. Frecvent la poze din telefon. |
| **Îndepărtare borduri negre** | 2 | Bordurile de scanare falsifică analiza histogramei. Cropping automat. |
| **Corecție perspectivă** | 2 | Poza din unghi deformează textul. Necesar pentru poze pe birou. |
| **Operații morfologice** | 3 | Text rupt după binarizare se repară cu dilate/erode. |
| **CLAHE** | 3 | Contrast local pentru documente cu umbră parțială. |

Documentul tehnic include cod șablon pentru fiecare funcție, gata de implementat.

### Flow-ul unui document

```
Încărcare (factură / bon / OP / foaie vărsământ — PDF / scan / poză)
    ↓
Pregătire document (analiză + redimensionare)
    ↓
5 metode de parsare (automat, fără implicare umană)
    ↓
Validare matematică (total = sumă articole, TVA = bază × cotă)
    ↓
Sistemul aplică corecturi automate unde se verifică
    ↓
    ├── ✅ Procesat corect → gata de verificare/export
    └── ❌ Nu trece validarea → Folder documente eșuate + raport motiv
```

**Ce nu a putut fi procesat corect îl găsești în folderul de eșuate**, cu un raport care explică exact cauza: câmp lipsă, total necoerent, text ilizibil.

Pentru început: **doar parsare automată, fără intervenție umană.** Ulterior, clientul poate corecta singur prin platformă sau plăti pentru verificare umană.

### Recomandări pentru fotografierea documentelor

Pentru ca parsarea să funcționeze cât mai bine, recomandăm clienților:

- **Lumină bună** — ideal la lumina zilei, fără umbre pe document
- **Camera perpendiculară** — cât mai drept deasupra documentului, nu din unghi
- **Așezat pe o suprafață plană** — fără să ții documentul în mână
- **Documentul să ocupe cea mai mare parte din imagine** — cât mai aproape, fără fundal inutil
- **Fără îndoituri** — cutele generează umbre și erori de parsare
- **Fotografiază imediat ce ai primit documentul** — înainte să se îndoaie, să se murdărească, să se piardă
- **Fără elemente care să acopere antetul** — bonul prins de factură, degete, alte hârtii peste
- **Verificarea se face după CUI-ul facturii și numele companiei** — antetul trebuie să fie vizibil și complet

### Platforma

Interfața asigură **confortul verificării și editării** fiecărui document — mai simplu decât în orice program de contabilitate. Fiecare factură poate fi corectată manual, articolele pot fi ajustate, exportul e într-un click.

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

> **Regulă:** Numele competitorilor apar DOAR în această secțiune. Nu se menționează în postări, pe pagină, în materiale de marketing.

### Competitorul real nr. 1: Introducerea manuală

Nu o firmă, ci un **obicei**. Contabilul primește factura PDF, o deschide, tastează datele în SAGA. E "gratis" — nu costă bani, costă timp. Și pentru 10 facturi/lună, e mai rapid să tastezi decât să înveți un tool nou.

**Când doare cu adevărat:** Peste 100 de facturi/lună. Atunci introducerea manuală devine ore pierdute, greșeli, reclamante de la clienți.

### Competitori direcți în România

| Produs | Ce face | Preț | Specific RO | Concurență directă? |
|--------|---------|------|-------------|---------------------|
| **SmartBill** | Emite facturi în cloud + parsare basic pe cele primite | 30-100 RON/lună | Da — e standard în RO | **Parțial** — are parsare pe facturi primite, dar nu e focusul lor. E o funcție secundară într-un produs de emis facturi. |
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
| **Nanonets** | ~$100-500/lună | Soluție generică. Necesită antrenare pe facturi RO. |

### Matricea de diferențiere

| Criteriu | Devorator | Internaționale | Manual |
|----------|-----------|----------------|--------|
| Facturi românești (CUI, SAGA, ; separator, , zecimal) | ✅ Nativ | ⚠️ Parțial/niciodată | ✅ 100% |
| Fără cloud, datele rămân în rețeaua privată | ✅ Da | ❌ Cloud obligatoriu | ✅ Da |
| Setup | Minute | Zile-săptămâni | Zero |
| Preț accesibil RO | ✅ ? | ❌ €200+/lună | "Gratis" |
| Review uman când nu e sigur | ✅ Da | ❌ Black box | — |
| Export direct SAGA | ✅ De construit | ❌ | — |
| Scalabil (500+ facturi/lună) | ✅ Da | ✅ Da | ❌ Nu |
| Fără dependență de API extern | ✅ Da | ❌ API third-party | — |

### Poziționare recomandată

> **Devorator = primul tool românesc de procesare facturi primite care rulează pe o rețea internă privată, fără expunere publică, fără cloud. Tokeni în avans sau abonament lunar. Garantăm securitatea datelor.**

Pivotul central: **Nu e "tool-ul universal". E un tool care face o singură treabă și o face bine: extrage datele din factură exact acolo unde vrei tu.**

---

## 4. Publicul Țintă

### Segmente pe verticală

1. **Contabil independent** — 1 persoană, 10-25 clienți, 50-200 facturi/lună (în funcție de complexitate). Cea mai frecventă durere: timpul pierdut cu tastat.
2. **Cabinet mic de contabilitate** — 2-5 contabili, 50-200+ clienți, sute de facturi/lună. Durerea: productivitatea echipei, erori de tastare.
3. **Departament financiar IMM** — 1-3 persoane, firma procesează intern. Durerea: reconcilieri, intrări multiple.

### Geografie

- **Acum:** România. Exclusiv. Produsul e construit pentru RO.
- **Mai târziu:** După maturizare, extindere pe piețe cu specific similar (Bulgaria, Ungaria, Polonia — format CUI, separator zecimal, TVA multiplu).

---

## 5. Modelul de Preț — Propunere

### Filosofie

Nu știm suficiente despre piață să fixăm prețul din birou. Îl descoperim vorbind cu contabilii. Până atunci, conturăm **arhitectura**, nu cifrele.

### Arhitectura — 2 moduri de plată

**1. Tokeni (plată în avans)**
- Cumperi un număr de tokeni / facturi în avans
- Folosești oricând, nu expiră
- Potrivit pentru: volume variabile, clienți care nu vor abonamente

**2. Abonament lunar**
- Plată fixă lunar, un număr de documente incluse
- Potrivit pentru: cei cu volum predictibil, care preferă buget lunar fix

Ambele moduri împart același strat gratuit:

**Stratul 0 — Gratuit permanent**
- Un număr de documente/lună procesate gratis, pentru totdeauna
- Nu expiră. Valabil indiferent de modul de plată ales
- Suficient cât să vadă că funcționează și să-și bage clienții în sistem

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
- Primele 3 luni: limită gratuită mai mare (să se obișnuiască)
- Apoi tokeni sau abonament, la alegere

### Păstrarea datelor
- Documentele procesate rămân în sistem **3 luni** în mod live
- După 3 luni, datele se arhivează
- Arhiva poate fi accesată gratuit la solicitare

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

1. **Modest, nu flamboaiant.** Nu garantăm perfecțiune. Parsăm documente, apar erori, le rezolvăm sau notificăm.
2. **Exact, nu metaforic.** Spui exact ce face. Fără "transformăm", "revoluționăm", "empower-uim". Fapte, nu promisiuni.
3. **Respect față de profesia de contabil.** Omul care folosește Devorator își câștigă existența din contabilitate. Nu e amuzant, nu e ironic — e serios.
4. **Sinceritate.** Când nu știe, spune "nu știm" (trimite la review sau în folderul de eșuate). Asta e diferențiator, nu slăbiciune.
5. **Zero jargon de marketing.** Nu "soluție inovatoare de automatizare". Ci "extrage datele din factură și le pune în Excel".

### Cum sună Devorator

| Situație | Ce spune | Ce NU spune |
|----------|----------|-------------|
| Prezentare | "Procesează facturi PDF și imagine. Extrage automat: număr, date, furnizor, articole, TVA, totaluri." | "Soluția revoluționară" |
| Ce-l diferențiază | "Rețea internă privată. Zero expunere publică. Zero cloud. Datele nu pleacă nicăieri." | "Singurul tool care face totul" |
| Limitare | "Pot apărea erori de parsare. Când se întâmplă, notificăm și încercăm să rezolvăm." | "Extrage orice document instant" |
| Preț | "Tokeni în avans — cumperi, folosești oricând, nu expiră. Sau abonament lunar, dacă preferi." | "Investiție care se amortizează în prima lună" |
| Hârtia | "O factură care ajunge direct în format electronic nu mai trebuie scanată, tipărită, arhivată fizic. Ghinionul e că majoritatea tot ajung pe hârtie. Devorator face următorul pas: odată intrată în sistem, nu mai iese." | "Salvăm pădurile împreună" |

### Structura unei postări / comunicări

1. **Problema concretă** — "Câte facturi tastezi manual într-o lună?"
2. **Ce face Devorator** — "Le încarci. Le procesezi. Le exporti. Atât."
3. **Dovada / modul** — (screenshot, comparație, demonstrație)
4. **Cine are nevoie** — "Dacă ai peste 50 de facturi pe lună, merită să vezi cum merge."
5. **Fără CTA forțat** — "Pagina: facebook.com/devorator." Atât.

### Ce nu spune Devorator niciodată

- "AI"
- "Revoluționar"
- "Singurul"
- "100%" sau "perfect" — nu există parsare perfectă
- Glume despre contabili sau birocrație
- Ironie la adresa ANAF sau a sistemului
- Ton flamboaiant, promisiuni grandioase

---

## 7. Distribuție & Vânzare

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

## 8. Următorii Pași

### Realizat

- [x] Analiza metodelor de parsare — documentată în `docs/ocr-image-preprocessing.md` (proiectul Devorator)
- [x] Playbook Devorator — structură completă (produs, competiție, preț, voce, distribuție)
- [x] Strategia Facebook mutată în document separat (`Facebook Strategy.md`) — de discutat

### De făcut

- [ ] Confirmat: nume pagină Facebook = "Devorator"
- [ ] Creată pagina
- [ ] Implementat deskew + Otsu + border crop în `extract.py`
- [ ] Stabilit prețul final
- [ ] Scris primele 5 postări (plan editorial săptămâna 1)
- [ ] Identificate 3 grupuri Facebook de contabilitate ca target
- [ ] Prima postare în grup (natural, nu reclamă)
- [ ] Beta cu 2-3 contabili reali
- [ ] Feedback → ajustat produsul
- [ ] Lansare

---

*Document creat: 6 iun 2026. Se actualizează pe măsură ce decidem.*
