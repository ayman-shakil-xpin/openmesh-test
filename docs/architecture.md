# Architecture

| Service | Port | Owner | Language |
|---|---|---|---|
| gateway | 8080 | Platform team | Go |
| billing | 9102 | Payments team | Python |
| search | 9200 | Data team | Java |
| notifier | 7070 | Platform team | TypeScript |

The billing service talks to the gateway only over mTLS. The search index is rebuilt nightly at **02:30 UTC**.
