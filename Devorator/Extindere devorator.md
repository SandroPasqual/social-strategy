Extinderea serviciului de la facturi la alte documente de business este o mișcare strategică excelentă. În timp ce piața de facturi este aglomerată, zona de parsare pentru alte documente operaționale și legale din România este aproape virgină, deoarece necesită înțelegere de context, nu doar citire de cifre.
Iată cele mai căutate documente de către companii pentru automatizare, grupate pe categorii, și datele esențiale pe care trebuie să le extragi din ele.
------------------------------
## 1. Documente de Resurse Umane (HR) & Salarizare
Contabilii și departamentele de HR pierd zile întregi introducând manual aceste date lună de lună.

* Adeverințe Medicale (Concedii Medicale):
* Ce extragi: Cod numeric personal (CNP), Cod indemnizație (ex: 01, 15 - esențial pentru calculul salariului), Perioada (Data început - Data sfârșit), Cod diagnostic, CUI angajator.
   * Valoare: Elimină greșelile de calcul din declarația 112 la ANAF.
* Fișe de pontaj (Timesheets):
* Ce extragi: Nume angajat, Ore lucrate total, Ore suplimentare, Ore de noapte, Zile de concediu.
   * Valoare: Centralizarea automată a tabelelor trimise de șefii de echipă din teren (construcții, retail).

## 2. Documente Logistice și de Producție (Gestiune)
Acestea vin adesea la pachet cu facturile, dar procesarea lor manuală blochează recepția mărfurilor în depozite.

* Avize de Însoțire a Mărfii (AVIZ):
* Ce extragi: Număr aviz, Furnizor, Cumpărător, Număr mașină/șofer, Lista de produse, Cantități livrate.
   * Valoare: Sistemul tău poate face automat reconcilierea (cross-check) între Aviz și Factura sosită ulterior, alertând compania dacă furnizorul a facturat mai mult decât a livrat în realitate.
* CMR-uri (Scrisori de trăsură pentru transport internațional):
* Ce extragi: Expeditor, Destinatar, Locul descărcării, Greutate brută, Număr paleți, Rezerve/Observații.
   * Valoare: Firmele de logistică pot introduce automat cursele în sistem direct din poza făcută de șofer pe traseu.
* NIR-uri (Note de Recepție și Constatare de Diferențe):
* Ce extragi: Gestiunea primitoare, Comisia de recepție, Preț de achiziție vs. Preț de vânzare cu amănuntul.

## 3. Documente Legale și Corporative
Companiile mari primesc sute de contracte și extrase pe care trebuie să le monitorizeze departamentul juridic sau financiar.

* Extrase de Cont Bancare (PDF-uri multi-pagină):
* Ce extragi: Data tranzacției, Partener (Nume/IBAN), Detalii plată (ex: „plata facturii 45”), Sumă (Debit/Credit).
   * Valoare: Permite reconcilierea bancară automată. SAGA știe să importe extrase, dar formatul de la unele bănci (ex: Revolut Business sau bănci străine) dă des erori.
* Contracte Comerciale:
* Ce extragi: Părțile contractante, Data expirării, Valoarea contractului, Termenul de plată (ex: „30 de zile”), Clauze de penalizare.
   * Valoare: Notificarea automată a managementului înainte ca un contract important sau o chirie să expire.

------------------------------
## 🚀 Cum abordezi tehnic și comercial această extindere?

   1. Nu schimba modelul de AI, schimbă Promptul: Modelele LLM moderne (precum GPT-4o sau Claude 3.5 Sonnet) sunt capabile să recunoască tipul de document dintr-o privire. Poți crea un singur punct de încărcare (upload). Sistemul tău analizează documentul și spune: „Acesta este un Concediu Medical. Aplic schema de HR”.
   2. Vinde pe verticală (Nu către toți odată):
   * Dacă vrei clienți firme de transport, adaugă Facturi + CMR-uri.
      * Dacă vrei clienți firme de distribuție/magazin online, adaugă Facturi + Avize de însoțire.
      * Dacă vrei clienți cabinete mari de contabilitate, adaugă Facturi + Concedii Medicale + Extrase Bancare.
   
Pentru a stabili prioritatea MVP-ului tău extins, care dintre aceste industrii ți se pare mai atractivă sau mai ușor de accesat pentru tine: zona de HR/Salarizare, logistica/transporturile sau managementul de contracte?

