# Buffer — Devorator (Facebook Page)

> Devorator are nevoie de **cont Buffer separat** (nu același cu Personal/Goodspell).

## Setup

1. Creează un cont Buffer nou pentru Devorator
2. Conectează pagina Devorator de Facebook
3. Creează un **Personal Key** pe developers.buffer.com
4. Salvează tokenul în `.buffer-devorator.env`:

```
BUFFER_ACCESS_TOKEN=***REMOVED***
BUFFER_CHANNEL_ID=de_completat_după_conectare
BUFFER_ORG_ID=de_completat_după_conectare
```

## Cum afli Channel ID și Org ID

După ce ai tokenul, rulează:

```
curl -s -X POST 'https://api.buffer.com' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer TOKENUL_TĂU' \
  -d '{"query":"{ organization { id } }"}'
```

Apoi:

```
curl -s -X POST 'https://api.buffer.com' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer TOKENUL_TĂU' \
  -d '{"query":"{ channels(input: { organizationId: \"ORG_ID\" }) { id name service } }"}'
```
