# Release runbook

- Releases ship every **Tuesday at 14:00 Gulf Standard Time**.
- The release manager for Q4 2026 is **Mariam Haddad**.
- Deploy freeze: **20 December 2026 to 4 January 2027**. No production deploys in that window.
- Rollback command: `meshctl rollback --to previous --confirm`.

## On-call rotation

| Week | Primary | Secondary |
|---|---|---|
| 1 | Omar Siddiqui | Lina Farah |
| 2 | Lina Farah | Yusuf Karim |
| 3 | Yusuf Karim | Omar Siddiqui |

Escalation after **15 minutes** without acknowledgement goes to the secondary.
