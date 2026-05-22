# AppSec Lab — Data Protection & Cryptography

## Topics Covered
- Hashing vs Encryption
- Password salting with bcrypt
- Secure error handling (no info leakage)
- Secure logging practices
- Hardcoded secrets detection

## Files
```
lab/secure_app.py          # Lab Python script (intentional good + bad patterns)
.github/workflows/
  security-scan.yml        # CI pipeline: Bandit + Semgrep
requirements.txt           # Python dependencies
```

## Running Locally

```bash
pip install -r requirements.txt
python lab/secure_app.py

# Bandit
bandit -r lab/ -t B105,B106,B107,B303,B324 --severity-level medium

# Semgrep (no account/token needed)
pip install semgrep
semgrep scan --config "p/python" --config "p/secrets" lab/
```

## What Gets Flagged

| Pattern | Tool | Rule | Lesson |
|---------|------|------|--------|
| `hashlib.md5()` for passwords | Bandit + Semgrep | B324 | Hashing ≠ password storage |
| `hashlib.sha1()` no salt | Bandit + Semgrep | B303 | Salting is mandatory |
| `DB_PASSWORD = "..."` hardcoded | Semgrep | p/secrets | Externalise config |
| `bcrypt` rounds=12 | ✅ Clean | — | Correct adaptive hash |
| `secrets.token_urlsafe()` | ✅ Clean | — | CSPRNG over `random` |
| Caller never sees stack trace | ✅ Clean | — | Error handling hygiene |

## No Tokens Required
Both tools run without any account signup or API tokens.
