# openmesh-test

Test repo for Open Mesh MCP end-to-end checks. Every file holds a few facts with distinctive values, so an agent's
answer can be checked against the source word for word.

| Path | What it holds |
|---|---|
| `docs/runbook.md` | Release process, on-call rotation, deploy freeze |
| `docs/architecture.md` | Services, ports and owners |
| `src/pricing.py` | A small pricing function with a known bug (see issue "Discount applied twice") |
| `data/customers.csv` | Ten fictional customers |
| `docs/canary.md` | A unique marker for isolation tests |

Project codename: **BLUE HERON**.
