# Conversation — 13 Iunie 2026

> Sesiune completă cu Big Pickle (agentul pi). Strategie social media, 3 conturi LinkedIn.

---

## Rezumat

Sesiunea a început cu curățarea fișierelor din `Personal/` root (27 → 3 fișiere strategice), a continuat cu auditul grupurilor LinkedIn (18 evaluate → 11 rămase), conectarea Buffer-ului prin GraphQL API, generarea de imagini pentru postări (Syne 800, dark/light alternant), și s-a încheiat cu documentarea completă în AGENTS.md.

---

## Timeline

### 1. Cleanup Personal/ Root
- **27 fișiere** în rădăcina `Personal/` → majoritatea ciorne procesate
- `~ Idei.md` → mutat în `Framework/_idei-brute.md` (arhivă idei brute)
- Personale (Orade Spania, Pasiunea, Vram, Xolo) → mutate în `ecosystem/`
- "Al Doilea Val" — șters (există deja în `drive/Ideas/`)
- "12. Negative space logo" — șters (design topic, nu se postează pe Personal)
- **Drafts/ șters complet** (13 ciorne procesate, toate aveau echivalent în Posted/ sau To be posted/)
- Au rămas doar 3 fișiere strategice: `Strategic Analysis.md`, `Strategy Proposal.md`, `buffer-config.md`

### 2. Audit Grupuri LinkedIn
- **18 grupuri** evaluate după: audiență, calitate, relevanță
- **🔥 Active (postare săptămânală):** Founders & Startups (28k), Executive Leadership (4.4k), Tech Founders (83k)
- **🧪 Test (1-2 postări):** CMO Roundtable (1.8k), CMO Forum (4.3k), Startup Europe (7.6k), Startup USA (12.9k), Founders Exchange (263k), Entrepreneurs Network (74k), Global Entrepreneurship (17k)
- **📡 Watch (doar comentarii):** CGO Community (1.3k)
- **❌ Exited (8):** Small Business & Independent Consultant, Digital Marketing, Media & Marketing, Chicago Business, Founders Club/DialEzee, AI Builders Nexus, European Entrepreneurship @ Silicon Valley, Designers Talk
- Pluginul de grupuri documentat în `Strategy Proposal.md`

### 3. Buffer Connection
- **Token OIDC** (`uMadUw...`) — nu funcționează cu API direct
- **Token Personal Key** (`wF-K65...`) — funcționează cu GraphQL API pe `api.buffer.com`
- Buffer personal key generat din Settings → API → Create a Personal Key
- **10 postări programate** la 17:00 RO (14:00 UTC = 10:00 ET)
- **"Marketable" deja publicată** de Buffer pe 12 Iunie — mutată din `To be posted/` în `Posted/`
- **Script:** `buffer-upload.py` — actualizat cu ora corectă și suport imagini
- **Limita:** Cont gratuit = 10 sloturi simultan

### 4. Imagini pentru Postări
- **Font:** Syne 800 (variable font descărcat din Google Fonts)
- **Canvas:** 1200×627px
- **Palete:**
  - Dark: bg `#181715`, text `#868177`
  - Light: bg `#868177`, text `#181715`
- **Margini:** 100px stânga/dreapta, 120px sus, line height 78px
- **Text extras:** Nu titlul, nu prima linie — esența scroll-stopping
- **Fără nume autor** pe imagini
- **40 imagini generate** (câte una lângă fiecare .md, același prefix de dată)
- **Primele 10 rafinate manual** cu text ales de mine
- **Buffer actualizat:** Toate 10 postările programate au acum imagini atașate (via `editPost` mutation)
- **Script:** `generate-images.py`

### 5. GitHub
- Token `[REDACTED-GITHUB-TOKEN]` salvat în remote URL
- Toate commiturile împinse pe `master`
- Repo privat → credentialele se comit în config fișiere

### 6. Documentare
- AGENTS.md rescris complet cu:
  - ⚡ Entry Point — "Open pi in: ~/projects/social-strategy"
  - Project Dashboard cu metrici pentru toate 3 conturile
  - Next Steps prioritizate
  - Buffer + Image Generation specs
  - Cleanup history

---

## Stare Finală

| Cont | Posted | To be posted | Images | Buffer |
|------|--------|-------------|--------|--------|
| **Personal** | 66 | 40 | 40 PNG (generate) | 10 scheduled 🖼️ |
| **Goodspell** | 20 | 50 | ❌ | Configurat, nefolosit |
| **Devorator** | — | — | — | ❌ Neînceput |

---

## Next Steps (pentru sesiunea următoare)

1. **Verifică Buffer queue** — postări publicate eliberează sloturi
2. **Refină imaginile 11-40** — text auto-extras, posibil de îmbunătățit manual
3. **Reîncepe Goodspell** — Drafts/, imagini, Buffer
4. **Analizează Devorator** — Facebook strategy de la zero
5. **Cross-pollination** — Personal share Goodspell posts

---

## Personalități & Preferințe

- **Vocea:** Gastric = intră lin, arde după. Fără selling, fără CTA, fără hashtag-uri
- **Engleză pe LinkedIn:** Româna face negație-înainte-afirmare, subminează autoritatea
- **Fără studii de caz:** Confidențialitatea e semnal de autoritate
- **Fără design:** Doar strategie
- **"Big Pickle" = agentul pi**
- **Sandro e român, scrie în engleză, targetează US**
