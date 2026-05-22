"""
Lab: Secure password hashing, error handling, and data protection.
Topics: Hashing vs Encryption, Salting, Secure config, Error handling & Logging

Intentionally contains both secure and weak patterns to trigger scanner findings.
"""

import hashlib
import logging
import os
import bcrypt
import secrets

# --- Logging: structured, no sensitive data ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)


# -------------------------------------------------------
# BAD PATTERNS (intentional — for scanner demonstration)
# -------------------------------------------------------

# BAD: MD5 for password — Bandit B324 / Semgrep p/python
def weak_hash_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()  # noqa: S324


# BAD: SHA1 without salt — Bandit B303
def weak_hash_sha1(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest()  # noqa: S303


# BAD: Hardcoded secret — Semgrep p/secrets
DB_PASSWORD = "SuperSecret123!"  # noqa


# -------------------------------------------------------
# GOOD PATTERNS (secure implementations)
# -------------------------------------------------------

# GOOD: bcrypt with work factor 12
def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode("utf-8"), salt)


# GOOD: Constant-time comparison to prevent timing attacks
def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed)


# GOOD: Cryptographically secure token (not random.random)
def generate_reset_token() -> str:
    return secrets.token_urlsafe(32)


# GOOD: Error handling — no stack traces or sensitive data leaked to caller
def safe_login(username: str, password: str, stored_hash: bytes) -> dict:
    try:
        if not username or not password:
            raise ValueError("Credentials must not be empty")

        matched = verify_password(password, stored_hash)

        if matched:
            logger.info("Login success for user: %s", username)
            return {"status": "ok"}

        logger.warning("Failed login attempt for user: %s", username)
        return {"status": "fail", "message": "Invalid credentials"}

    except ValueError as e:
        logger.error("Validation error: %s", str(e))
        return {"status": "error", "message": "Bad input"}

    except Exception:
        # Internal error — log server-side only, never expose details to caller
        logger.exception("Unexpected internal error during login")
        return {"status": "error", "message": "Internal error"}


if __name__ == "__main__":
    hashed = hash_password("P@ssw0rd")
    print(safe_login("alice", "P@ssw0rd", hashed))
    print(safe_login("alice", "wrongpass", hashed))
    print("Reset token:", generate_reset_token())
