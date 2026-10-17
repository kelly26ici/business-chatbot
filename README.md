# Business Chatbot — WhatsApp AI Customer Assistant

A production-shaped WhatsApp business assistant. Inbound customer messages arrive through the Meta WhatsApp Cloud API, are matched to a persistent customer record, answered by a fast open-weight LLM, and enriched over time by a background information-extraction pass that keeps a lightweight CRM in sync.

Built for the common small-business shape: a WhatsApp number as the front desk, no frontend, and a need to know *who* each customer is by the time they come back.

---

## What it does

- **WhatsApp Cloud API transport** — webhook verification (`GET`) and inbound message delivery (`POST`), with outbound sends over `httpx`.
- **Two-tier customer memory** — every customer is cached in **Redis** for 24h and persisted in **Supabase/PostgreSQL**, so lookups are fast but durable.
- **Automatic customer enrichment** — a background extractor reads the conversation and pulls out name, email, payment mentions (amount + date), preferences, and tags, writing them back to the CRM.
- **Conversation history replay** — the last `MAX_HISTORY` messages are replayed into the prompt, so replies stay in context.
- **Provider-isolated AI layer** — the active provider is swappable in `src/config/constants.py`; Groq (`llama-3.3-70b-versatile`) is the live path, with a Gemini client present for comparison.

---

## Architecture

```text
WhatsApp Cloud API
      │  GET  /webhook   (verification challenge)
      │  POST /webhook   (inbound message)
      ▼
FastAPI webhook_handler
      │
      ▼
message_handler ───────► chat()
                          │  1. load customer  (Redis ──miss──► Supabase, then re-cache)
                          │  2. load history   (last 10 turns)
                          │  3. build prompt
                          │  4. generate       (groq_client ──► llama-3.3-70b-versatile)
                          ▼
                     extract_customer_info()  ──► update_customer()  (Supabase + Redis)
                          │
                          ▼
                     send_message()  ──► Meta Graph API
```

---

## Project layout

```text
src/
├── config/
│   ├── constants.py        Model catalogue, routing thresholds, system prompt
│   └── settings.py         Environment-backed configuration
├── database/
│   ├── customer_repo.py    Redis-first / Supabase-durable customer access
│   ├── redis_client.py     Upstash Redis client
│   └── supabase_client.py  Supabase client
├── handlers/
│   ├── webhook_handler.py  Meta webhook verification + intake
│   └── message_handler.py  Orchestration and error surfacing
├── models/
│   └── customer.py         Customer dataclass (name, email, paid, payment, prefs, tags)
└── services/
    ├── chat.py             Prompt assembly and provider dispatch
    ├── groq_client.py      Active LLM provider
    ├── gemini_client.py    Alternate provider (OpenAI-style → Gemini translation)
    ├── extractor.py        Structured customer-info extraction → JSON
    └── whatsapp.py         Outbound message delivery
```

---

## Requirements

- Python 3.10+
- A Meta app with WhatsApp Cloud API enabled
- Groq API key (active provider), Google API key (alternate)
- Supabase project and Upstash Redis instance

## Configuration

Create a `.env` file in the project root:

```env
# App
APP_NAME=Business AI Assistant

# Active LLM provider
GROQ_API_KEY=gsk_...
GOOGLE_API_KEY=AIza...

# Storage
SUPABASE_URL=https://<project>.supabase.co
SUPABASE_KEY=<service or anon key>
REDIS_URL=https://<instance>.upstash.io
REDIS_TOKEN=<token>

# WhatsApp Cloud API
WHATSAPP_TOKEN=<permanent or system-user token>
WHATSAPP_PHONE_NUMBER_ID=<phone-number-id>
WHATSAPP_VERIFY_TOKEN=<token you choose, must match Meta console>
```

## Running

```bash
pip install -r requirements.txt
python app.py        # uvicorn on 0.0.0.0:8000
```

Then point the Meta webhook callback at `https://<your-host>/webhook` with the verify token above.

## Tests

```bash
pytest
```

---

## Notes

- `chat.py` commits to the provider configured by `AI_PROVIDER` in `src/config/constants.py`. Groq is the live default; `gemini_client.py` is a drop-in alternate, not dead code — it keeps a second provider reachable without touching the call path.
- The extractor returns JSON only and is instructed to omit fields it did not find, so partial information never overwrites known data with empty values.

## License

MIT — see [LICENSE](LICENSE).
