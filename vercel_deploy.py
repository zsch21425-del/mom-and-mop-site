#!/usr/bin/env python3
"""Deploy A Mom & A Mop to Vercel — all files, always. Never misses the logo."""
import os, sys, subprocess, json

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.expanduser("~/.vercel/auth.json")

if not os.path.exists(TOKEN_FILE):
    print("No Vercel token found at ~/.vercel/auth.json")
    sys.exit(1)

TOKEN = json.load(open(TOKEN_FILE))["token"]
os.environ["VERCEL_ORG_ID"] = "team_n2GzzPLUrHDPhSvzEEhNuVkz"
os.environ["VERCEL_PROJECT_ID"] = "prj_5uRHXmfgseF6qf9zWc77wXh77ysA"
os.environ["VERCEL_TOKEN"] = TOKEN

prod = "--prod" in sys.argv

cmd = ["vercel", SITE_DIR, "--token", TOKEN, "--yes"]
if prod:
    cmd.append("--prod")

print(f"Deploying {'to production' if prod else 'as preview'}...")
result = subprocess.run(cmd, capture_output=True, text=True, cwd=SITE_DIR)

print(result.stdout)
if result.stderr:
    print(result.stderr, file=sys.stderr)

sys.exit(result.returncode)
