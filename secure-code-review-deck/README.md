# 🛡️ Secure Code Review — Interactive Workshop Deck

A self-contained, browser-based presentation for a 2-hour hands-on secure code review workshop. Built with Node.js + Express. No build tools, no dependencies beyond Express.

## What's Inside

**25 slides covering:**

| Block | Topic | Duration |
|-------|-------|----------|
| 1 | Mindset & Methodology — the review loop, what to open first | 15 min |
| 2 | Vulnerability Walkthroughs — SQLi, JWT, IDOR, Command Injection, Path Traversal, XSS, Mass Assignment, Secrets | 30 min |
| 3 | Hands-On Lab — find all bugs in a vulnerable Express app (built-in 20-min countdown timer) | 30 min |
| 4 | DevSecOps Pipeline — IDE → pre-commit → CI → registry → runtime, GitHub Actions YAML | 25 min |
| 5 | Secrets Management — every secret file across every modern stack + .gitignore template | 20 min |

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/secure-code-review-deck.git
cd secure-code-review-deck

# 2. Install dependencies
npm install

# 3. Run
npm start

# 4. Open in browser
# http://localhost:3000
```

## Navigation

| Key / Action | Effect |
|---|---|
| `→` `↓` `Space` | Next slide |
| `←` `↑` | Previous slide |
| `Home` / `End` | First / last slide |
| `F` | Toggle fullscreen |
| Click left 20% of screen | Previous slide |
| Click right 20% of screen | Next slide |
| Swipe (touch) | Navigate |

## Lab Timer

On the **Hands-On Lab** slide (slide 16), there's a built-in countdown timer:

- **START** — begins the 20-minute countdown
- **RESET** — resets to 20:00
- Timer turns orange at 5 minutes, red at 1 minute

## Stacks Covered

Vulnerability examples use: **Node.js / Express**, **Python / FastAPI**, **React**

Secret files reference covers: **Node.js**, **Python**, **Java/Spring**, **Ruby on Rails**, **Go**, **PHP/Laravel**, **Terraform**, **Kubernetes**, **Ansible**, **AWS**, **GCP**, **Azure**, **Android**, **iOS**

## Tech Stack

- **Runtime**: Node.js
- **Server**: Express (serves a single static HTML file)
- **Fonts**: JetBrains Mono · Syne · Inter (via Google Fonts)
- **No frontend frameworks** — vanilla JS, ~300 lines

## License

MIT — use freely for internal training, conference talks, or onboarding sessions.
