Un MVP (Minimum Viable Product) sau Produs Minim Viabil este cea mai simplă versiune a unui produs care poate fi lansată pe piață pentru a testa o idee de business. Acesta conține doar funcționalitățile strict esențiale pentru a funcționa și a aduce valoare primilor utilizatori. 

Scopul principal al unui MVP nu este obținerea profitului imediat, ci învățarea rapidă. El îți permite să colectezi feedback real de la clienți cu un efort și un buget minime, înainte de a investi sume mari de bani în dezvoltarea finală. 

## Caracteristicile unui MVP eficient
Funcționalități de bază: Include doar ce este absolut necesar pentru a rezolva problema utilizatorului.

- Lansare rapidă: Se construiește în săptămâni, nu în luni sau ani.
- Funcțional: Nu este o schiță sau o machetă defectă; produsul chiar trebuie să meargă.
- Buget redus: Minimizează riscul financiar în caz de eșec al ideii. 

## Diferența dintre Prototip și MVP
Deși sunt des confundate, cele două concepte reprezintă etape diferite:

-- Prototipul: Este un model intern, adesea nefuncțional (ex: desene, machete clickabile), folosit pentru a vedea cum va arăta produsul și a-l prezenta echipei sau investitorilor.
-- MVP-ul: Este un produs real, lansat publicului larg, capabil să proceseze date, comenzi sau interacțiuni reale. 

Pentru un serviciu de parsare și culegere automată de facturi dedicat companiilor și contabililor, MVP-ul Devorator trebuie să demonstreze o singură valoare de bază: că poate extrage corect datele dintr-o factură PDF/imagine și le poate exporta într-un format util (Excel/CSV).
Nu încerca să construiești o platformă complexă de contabilitate din prima zi. Concentrează-te pe eliminarea muncii manuale de introducere a datelor.

Funcționalitățile esențiale pentru MVP

- Modul de încărcare: Un ecran simplu unde utilizatorul încarcă unul sau mai multe fișiere PDF sau poze (JPEG/PNG) cu facturi.
- Motorul de parsare (OCR): Integrarea unui API existent de scanare (ex: Google Cloud Document AI, AWS Textract sau OpenAI GPT-4o) pentru a extrange: CUI emitent/beneficiar, total factură, TVA și data.
- Ecran de validare: O tabelă simplă unde utilizatorul vede ce a extras robotul și poate corecta manual dacă apar mici greșeli.
- Buton de export: Descărcarea datelor validate într-un fișier Excel sau CSV standardizat, gata de importat în softurile de contabilitate.

Ce NU trebuie să incluzi în MVP
- Abonamente și plăți automate: Procesează plățile manual prin factură fiscală sau link simplu de Stripe.
- Integrare directă prin API cu ANAF / e-Factura: În faza de MVP, utilizatorii pot descărca manual PDF-urile din SPV și le pot urca în aplicația ta.
- Sincronizări automate cu Saga, WinMentor etc.: Exportul în format Excel/CSV este suficient pentru început, deoarece majoritatea softurilor au deja opțiune de import din Excel.

Sistem avansat de drepturi și roluri: Contul de utilizator simplu (e-mail și parolă) este destul pentru a valida conceptul.

Cum poți trișa inteligent (Strategia "Vrajitorul din Oz")
Dacă algoritmul de parsare dă erori la facturi românești complexe în primele zile, procesează-le parțial manual.
Când utilizatorul încarcă o factură, o echipă din spate (sau tu) verifică rapid datele și corectează erorile înainte ca utilizatorul să le vadă. Pentru client, serviciul va părea complet automatizat, iar tu vei câștiga timp să îmbunătățești codul, înțelegând exact ce tipuri de facturi primesc contabilii în realitate.

În România, cel mai utilizat soft de contabilitate este SAGA C. Vestea bună pentru MVP-ul tău este că modulul de import din SAGA (dar și din alte softuri precum ContApp, SmartBill sau Nexterp) este extrem de flexibil. 
Softurile moderne nu mai cer o ordine rigidă a coloanelor. Ele folosesc un ecran de mapare, unde contabilul alege o singură dată care coloană din Excelul tău corespunde cu câmpurile din soft (ex: „Coloana B din Excel reprezintă CUI-ul”).

Pentru ca fișierul tău Excel/CSV să fie perfect compatibil și ușor de importat, trebuie să structurezi datele pe două tipuri de abordări.
1. Structura Universală (Recomandată pentru MVP)
Cea mai simplă metodă de livrare este un tabel în care fiecare rând reprezintă o factură. Aceasta acoperă 90% din nevoile inițiale (facturi cu o singură linie de servicii sau mărfuri globale).
Generează un fișier Excel (.xlsx) sau CSV (cu separator punct și virgulă ;) cu următoarele coloane clare: 
Tip_Document: (ex: Factură, Factură Storno, Bon Fiscal)
Numar_Document: Numărul facturii (ex: 10243)
Data_Document: Data emiterii (Format standard recomandat: DD.MM.YYYY sau YYYY-MM-DD)
Cod_Fiscal_Partener: CUI-ul sau CNP-ul furnizorului/clientului (fără „RO” în față, sau cu el, dar consistent)
Denumire_Partener: Numele companiei care a emis factura
Valoare_Neta: Suma totală fără TVA
Cota_TVA: Procentul de TVA aplicat (ex: 19, 9, 5, 0)
Valoare_TVA: Suma totală a TVA-ului
Valoare_Bruta: Totalul de plată (Net + TVA)
Moneda: Codul monedei (RON, EUR, USD)
Explicatie: O descriere generică preluată de algoritmul tău (ex: „Conform factură scanată”). 
2. Structura Avansată: Linii Multiple (Multi-line / Articole)
Dacă o factură are mai multe produse (linii) și contabilul vrea să le descarce cantitativ-valoric (ex: Linie 1: Pixuri, Linie 2: Hârtie), structura se modifică.
În Excel, vei repeta datele de antet ale aceleiași facturi pe mai multe rânduri, diferind doar datele liniei:
Numar_Factura
Data	CUI_Furnizor	Denumire_Produs	Cantitate	Pret_Unitar	Cota_TVA	Valoare_Neta
54321	30.05.2026	123456	Servicii curățenie	1	500.00	19	500.00
54321	30.05.2026	123456	Detergenți	5	20.00	19	100.00
SAGA va înțelege automat că este vorba despre o singură factură cu două poziții deoarece numărul facturii, data și CUI-ul sunt identice.

💡 Sfaturi de Aur pentru MVP-ul tău în România
Regulile CSV în România: Dacă generezi fișiere .csv, folosește punct și virgulă (;) ca separator, nu virgula (,). Calculatoarele contabililor români au setările regionale pe România, unde virgula este folosită ca separator zecimal (ex: 15,50 RON). Dacă pui virgulă ca separator de coloane, Excelul le va amesteca pe toate pe un singur rând. 
Formatul CUI-ului: Curăță textul extras. Ai grijă ca CUI-urile să nu conțină spații. Dacă softul tău extrage RO 1234, salvează-l în Excel ca 1234 sau RO1234 (ideal este să oferi o opțiune de eliminare a prefixului RO, majoritatea softurilor preferă doar cifrele). 

Formatul XML (Pasul următor): După ce MVP-ul tău pe bază de Excel validează ideea, poți genera direct fișiere XML în formatul standard UBL (cel folosit de ANAF e-Factura). Toate softurile de contabilitate din România importă nativ acest format prin simplul import al e-facturii, eliminând complet nevoia de mapare.