# SCLI — Security Posture Analysis Tool (Linux CLI)

**by [Antibody Cyber Technology, LLC](https://antibodycyber.com)**  
Huntsville, Alabama · Cybersecurity since 2002

---

## Overview

**SCLI** is a terminal-native Linux CLI companion to the **SPAT** (Security Posture Analysis Tool) platform. It wraps `spat_cli.py` — SPAT's scanning engine — in a clean, no-GUI command-line interface with ANSI colour output, per-scan timestamped reports, and all seven scan profiles available in the SPAT GUI dashboard.

SCLI is a direct conversion of `spat_linux.py` (the SPAT Linux GUI) with every feature preserved and the tkinter dependency removed.

What is SPAT?
SPAT is an automated external security assessment tool that scans and evaluates the public-facing security defenses of websites and network servers. Developed by Antibody Cyber Technology, LLC, a specialized cybersecurity company based out of Huntsville, Alabama, the scanner proactively probes a target domain from an external network perspective to map its attack surface and reveal potential technical weaknesses before they can be exploited.

All 17 checks operate against the domain name itself — not a specific URL path. SPAT queries public DNS, makes direct TLS/socket connections, issues HTTP requests, and checks your domain against 90+ global threat intelligence feeds — the same feeds used by enterprise firewalls, browsers, and email security filters worldwide — using only the bare hostname (e.g. example.com).

---

## Features

- **7 scan profiles** — Full, Standard, Web-only, Web + Threat Intel, SSH-only, and JSON variants
- **ANSI colour output** — pass/fail/warn/info lines colour-coded identically to the GUI dashboard
- **Per-scan timestamped reports** — every run writes a unique `report_YYYYMMDD_HHMMSS.html` so reports never overwrite each other
- **JSON + HTML output** — specify custom paths or use auto-generated defaults
- **Browser open** — `--open` flag launches the HTML report in your default browser after the scan
- **Clean Ctrl+C** — `SIGINT` terminates the child process gracefully
- **No GUI dependency** — runs on any headless Linux server or desktop without X11/tkinter

---

## Requirements

- Python 3.10+
- [`spat_cli`](https://spatcyber.com) — SPAT's scanning engine (`spat_cli/spat_cli.py` in the same directory)

---

## Installation

```bash
git clone https://github.com/waynemcdon/SCLI.git
cd SCLI
chmod +x SCLI
```

---

## Usage

```
usage: SCLI [-h] [--profile PROFILE] [--ssh-port PORT]
            [--json FILE] [--html FILE] [--open]
            [--list-profiles]
            [hostname]
```

### Examples

```bash
# Full scan (web + SSH + threat intel)
./SCLI example.com

# Standard scan, no threat intel
./SCLI example.com --profile standard

# Web-only scan, custom HTML report, open in browser
./SCLI example.com --profile web-only --html /tmp/report.html --open

# Non-standard SSH port + JSON output
./SCLI example.com --ssh-port 2222 --json scan.json

# List all available profiles
./SCLI --list-profiles
```

### Scan Profiles

| Profile | Description |
|---|---|
| `full` | Full Scan (web + SSH + threat intel) — **default** |
| `standard` | Standard (web + SSH, no threat intel) |
| `web-only` | Web Only (no SSH, no threat intel) |
| `web-intel` | Web + Threat Intel (no SSH) |
| `ssh-only` | SSH Only |
| `full-json` | Full Scan + JSON report |
| `standard-json` | Standard + JSON report |

---

## Options

| Flag | Description |
|---|---|
| `hostname` | Target hostname or URL (`example.com` or `https://example.com`) |
| `--profile / -p` | Scan profile (default: `full`) |
| `--ssh-port PORT` | SSH port to scan (default: `22`) |
| `--json FILE` | Write JSON report to FILE |
| `--html FILE` | Write HTML report to FILE |
| `--open` | Open HTML report in browser after scan |
| `--list-profiles` | List all profiles and exit |

---

## Output

SCLI streams `spat_cli.py` output in real time with colour-coded lines:

| Colour | Meaning |
|---|---|
| 🟢 Green | Pass |
| 🔴 Red | Fail |
| 🟡 Yellow | Warning |
| 🔵 Cyan | Info / Header |
| Bold | Security score / Grade |

Exit codes mirror `spat_cli.py`: `0` = no failures, `1` = failures detected, `2` = script not found.

---

## Related

- **SPAT GUI** (`spat_linux.py`) — full tkinter dashboard version for Linux desktop
- **SPAT Platform** — https://spatcyber.com
- **Whitepaper** — https://spatcyber.com/static/SPAT_Whitepaper.pdf

---

## Company

**Antibody Cyber Technology, LLC**  
🌐 [antibodycyber.com](https://antibodycyber.com) · [socsoutheast.com](https://socsoutheast.com)  
🐦 [@antibodycyber](https://x.com/antibodycyber)  
💼 [LinkedIn](https://www.linkedin.com/in/wayne-mcdonald-113a79248/)

---

*SCLI and SPAT are products of Antibody Cyber Technology, LLC. All rights reserved.*
