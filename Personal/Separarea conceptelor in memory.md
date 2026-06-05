Modifică scriptul Python pentru a citi un fișier local text sau Markdown (de exemplu, concepte.md). Te rog să aplici următoarea logică:

   1. Citește fișierul complet ca text.
   2. Imparte textul în bucăți (chunks) folosind separatorul --- (trei cratime pe o linie nouă). Folosește .split('\n---\n') sau .split('---') și curăță spațiile goale cu .strip().
   3. Filtrează bucățile goale (pentru a evita erorile dacă apar separatori consecutivi sau la finalul fișierului).
   4. Iterează prin fiecare bucată rezultată:
   * Trimite bucata de text către modelul ONNX (MiniLM) pentru a genera embedding-ul (vectorul).
      * Inserează textul bucății și vectorul generat ca un rând nou (linie separată) în tabelul SQLite.
   
Asigură-te că scriptul șterge sau actualizează vechile înregistrări din SQLite dacă rulăm importul din nou, pentru a nu duplica datele.”

------------------------------
## Ce va schimba agentul în cod (ca să înțelegi logica)?
În loc să primească o listă fixă din cod, agentul va scrie o structură de tip buclă (loop). În limbaj uman, logica pe care o va pune în Python va arăta cam așa:

   1. Deschide concepte.md.
   2. bucati = text_gros.split('---')
   3. Pentru fiecare bucata din bucati:
   * vector = model_onnx.encode(bucata)
      * SQL: INSERT INTO documente (text, vector) VALUES (bucata, vector)
   