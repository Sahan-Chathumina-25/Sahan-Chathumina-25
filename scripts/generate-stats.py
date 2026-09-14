#!/usr/bin/env python3
"""
GitHub Statistics SVG Generator
Fetches real data from GitHub API and generates a statistics card SVG.

Architecture:
    GitHub API → stats data → calculation → SVG renderer → github-statistics.svg

No external dependencies required — uses only Python standard library.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from typing import Any

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

USERNAME = "Sahan-Chathumina-25"
PROFILE_REPO = f"{USERNAME}/{USERNAME}"  # excluded from stats
EXCLUDE_FORKED = True
MIN_LANGUAGE_PERCENT = 0.5  # ignore languages below this threshold
TOP_LANGUAGES = 5
OUTPUT_FILE = "assets/github-statistics.svg"

# GitHub language colors (subset)
LANGUAGE_COLORS = {
    "Python": "#3572A5",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Shell": "#89e051",
    "Bash": "#89e051",
    "Dockerfile": "#384d54",
    "YAML": "#cb171e",
    "JSON": "#292929",
    "Markdown": "#083fa1",
    "Lua": "#000080",
    "C": "#555555",
    "C++": "#f34b7d",
    "Java": "#b07219",
    "Go": "#00ADD8",
    "Rust": "#dea584",
    "Ruby": "#701516",
    "PHP": "#4F5D95",
    "Swift": "#F05138",
    "Kotlin": "#A97BFF",
    "R": "#198CE7",
    "Dart": "#00B4AB",
    "Vue": "#41b883",
    "Svelte": "#ff3e00",
    "Makefile": "#427819",
    "CMake": "#DA3434",
    "PowerShell": "#012456",
    "Batch": "#C1F12E",
    "XML": "#0060ac",
    "Toml": "#9c4221",
    "INI": "#d1dbe0",
    "Nginx": "#009639",
    "Starlark": "#76d275",
    "Just": "#3C3C3C",
    "Property List": "#000000",
    "Star": "#76d275",
}

DEFAULT_COLOR = "#7F95A5"


def get_language_color(lang: str) -> str:
    """Return a GitHub-style color for a language."""
    return LANGUAGE_COLORS.get(lang, DEFAULT_COLOR)


# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------

def github_get(endpoint: str, token: str | None = None) -> Any:
    """Make a GET request to the GitHub REST API."""
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"  API error {e.code} for {endpoint}: {e.read().decode()[:200]}", file=sys.stderr)
        raise


def fetch_profile(token: str | None) -> dict:
    """Fetch the user profile."""
    data = github_get(f"/users/{USERNAME}", token)
    return {
        "login": data.get("login", USERNAME),
        "name": data.get("name", USERNAME),
        "followers": data.get("followers", 0),
        "following": data.get("following", 0),
        "public_repos": data.get("public_repos", 0),
        "avatar_url": data.get("avatar_url", ""),
    }


def fetch_all_repos(token: str | None) -> list[dict]:
    """Fetch all public repositories for the user (paginated)."""
    repos: list[dict] = []
    page = 1
    per_page = 100
    while True:
        data = github_get(f"/users/{USERNAME}/repos?per_page={per_page}&page={page}&sort=updated", token)
        if not data:
            break
        repos.extend(data)
        if len(data) < per_page:
            break
        page += 1
    return repos


def fetch_languages_for_repo(repo: str, token: str | None) -> dict[str, int]:
    """Fetch language byte counts for a single repository."""
    try:
        data = github_get(f"/repos/{repo}/languages", token)
        return data  # {"Python": 12345, ...}
    except Exception:
        return {}


def fetch_contributions(token: str | None) -> int | None:
    """
    Fetch contribution count using GraphQL.
    Returns None if unavailable (requires auth for accurate data).
    """
    if not token:
        return None
    query = """
    query {
      user(login: "%s") {
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """ % USERNAME
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = json.dumps({"query": query}).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode())
            cal = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]
            return cal["totalContributions"]
    except Exception as e:
        print(f"  GraphQL contributions fetch failed: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Statistics calculation
# ---------------------------------------------------------------------------

def calculate_stats(token: str | None) -> dict:
    """
    Calculate all statistics from GitHub API.
    Returns a dict with all values needed for the SVG.
    """
    print("Fetching profile...")
    profile = fetch_profile(token)
    print(f"  Repos: {profile['public_repos']}, Followers: {profile['followers']}, Following: {profile['following']}")

    print("Fetching repositories...")
    repos = fetch_all_repos(token)
    print(f"  Found {len(repos)} repositories")

    # Filter out forks if configured
    if EXCLUDE_FORKED:
        repos = [r for r in repos if not r.get("fork", False)]
        print(f"  After excluding forks: {len(repos)} repositories")

    # Filter out the profile README repository
    repos = [r for r in repos if r.get("full_name", "") != PROFILE_REPO]
    print(f"  After excluding profile repo: {len(repos)} repositories")

    # Calculate stars and forks
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    total_forks = sum(r.get("forks_count", 0) for r in repos)
    print(f"  Stars: {total_stars}, Forks: {total_forks}")

    # Fetch languages across all repos
    print("Fetching languages...")
    language_bytes: dict[str, int] = {}
    for repo in repos:
        repo_name = repo.get("full_name", "")
        langs = fetch_languages_for_repo(repo_name, token)
        for lang, bytes_count in langs.items():
            language_bytes[lang] = language_bytes.get(lang, 0) + bytes_count

    # Calculate language percentages
    total_bytes = sum(language_bytes.values())
    language_stats: list[dict] = []
    if total_bytes > 0:
        for lang, bytes_count in sorted(language_bytes.items(), key=lambda x: x[1], reverse=True):
            pct = (bytes_count / total_bytes) * 100
            if pct >= MIN_LANGUAGE_PERCENT:
                language_stats.append({
                    "name": lang,
                    "percent": round(pct, 1),
                    "bytes": bytes_count,
                    "color": get_language_color(lang),
                })
        # Cap to top N
        language_stats = language_stats[:TOP_LANGUAGES]
        # Normalize to 100% if needed
        displayed_total = sum(ls["percent"] for ls in language_stats)
        if displayed_total > 0 and abs(displayed_total - 100) > 0.5:
            # Normalize
            factor = 100.0 / displayed_total
            for ls in language_stats:
                ls["percent"] = round(ls["percent"] * factor, 1)
    print(f"  Languages: {[(ls['name'], ls['percent']) for ls in language_stats]}")

    # Fetch contributions
    print("Fetching contributions...")
    contributions = fetch_contributions(token)
    if contributions is not None:
        print(f"  Contributions (this year): {contributions}")
    else:
        print("  Contributions: unavailable (no auth token)")

    return {
        "repos_count": len(repos),
        "followers": profile["followers"],
        "following": profile["following"],
        "stars": total_stars,
        "forks": total_forks,
        "contributions": contributions,
        "languages": language_stats,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


# ---------------------------------------------------------------------------
# SVG generation
# ---------------------------------------------------------------------------

def generate_svg(stats: dict) -> str:
    """Generate the GitHub Statistics SVG card."""
    width = 700
    height = 310
    updated = stats["updated_at"]
    langs = stats["languages"]

    # Build stat rows
    y_pos = [100]  # mutable counter
    rows = []
    for label, value, color in [
        ("Public Repos", str(stats["repos_count"]), "#EAF7FF"),
        ("Contributions", f"{stats['contributions']} this year" if stats["contributions"] is not None else "N/A", "#00FF88"),
        ("Stars Earned", str(stats["stars"]), "#FFB800"),
        ("Followers", str(stats["followers"]), "#EAF7FF"),
        ("Forks", str(stats["forks"]), "#EAF7FF"),
    ]:
        rows.append(f"""    <text x="55" y="{y_pos[0]}" fill="#7F95A5" font-size="11">{label}</text>
    <text x="300" y="{y_pos[0]}" text-anchor="end" fill="{color}" font-size="13" font-weight="700">{value}</text>""")
        y_pos[0] += 22

    stats_rows = "\n".join(rows)

    # Build language rows
    lang_rows = []
    lang_y = 100
    bar_width = 180
    for i, lang in enumerate(langs):
        bar_filled = bar_width * (lang["percent"] / 100)
        lang_rows.append(f"""    <text x="385" y="{lang_y}" fill="#7F95A5" font-size="11">{lang["name"]}</text>
    <rect x="470" y="{lang_y - 7}" width="{bar_width}" height="8" rx="4" fill="#1A2736"/>
    <rect x="470" y="{lang_y - 7}" width="{bar_filled:.1f}" height="8" rx="4" fill="{lang["color"]}">
      <animate attributeName="width" from="0" to="{bar_filled:.1f}" dur="1.5s" fill="freeze" begin="0.3s"/>
    </rect>
    <text x="660" y="{lang_y}" text-anchor="end" fill="#EAF7FF" font-size="10">{lang["percent"]}%</text>""")
        lang_y += 22

    lang_section = "\n".join(lang_rows) if lang_rows else """    <text x="515" y="130" text-anchor="middle" fill="#7F95A5" font-size="11">No languages detected</text>"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B1117"/>
      <stop offset="100%" stop-color="#05070A"/>
    </linearGradient>
    <linearGradient id="headerLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D9FF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00D9FF" stop-opacity="1"/>
      <stop offset="100%" stop-color="#00D9FF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <style>
    text {{ font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }}
  </style>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="url(#cardBg)" rx="10" stroke="#1A2736" stroke-width="1"/>

  <!-- Header -->
  <text x="350" y="28" text-anchor="middle" fill="#00D9FF" font-size="11" font-weight="700" letter-spacing="3" opacity="0.9">GITHUB STATISTICS</text>
  <line x1="250" y1="36" x2="450" y2="36" stroke="url(#headerLine)" stroke-width="0.5">
    <animate attributeName="x1" from="350" to="250" dur="1s" fill="freeze"/>
    <animate attributeName="x2" from="350" to="450" dur="1s" fill="freeze"/>
  </line>

  <!-- Left Card: Profile Stats -->
  <rect x="30" y="50" width="320" height="240" rx="8" fill="#05070A" stroke="#1A2736" stroke-width="1"/>
  <rect x="30" y="50" width="320" height="28" rx="8" fill="#111820"/>
  <rect x="30" y="70" width="320" height="8" fill="#111820"/>
  <text x="190" y="69" text-anchor="middle" fill="#EAF7FF" font-size="10" font-weight="600" letter-spacing="1">PROFILE STATS</text>

  {stats_rows}

  <!-- Right Card: Top Languages -->
  <rect x="360" y="50" width="310" height="240" rx="8" fill="#05070A" stroke="#1A2736" stroke-width="1"/>
  <rect x="360" y="50" width="310" height="28" rx="8" fill="#111820"/>
  <rect x="360" y="70" width="310" height="8" fill="#111820"/>
  <text x="515" y="69" text-anchor="middle" fill="#EAF7FF" font-size="10" font-weight="600" letter-spacing="1">TOP LANGUAGES</text>

  {lang_section}

  <!-- Footer -->
  <text x="350" y="{height - 12}" text-anchor="middle" fill="#7F95A5" font-size="8" opacity="0.6">Updated automatically &bull; GitHub API &bull; {updated}</text>
</svg>"""

    return svg


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print("WARNING: No GITHUB_TOKEN set. Some data may be limited.", file=sys.stderr)
        print("  Set GITHUB_TOKEN env var for full statistics.", file=sys.stderr)

    print("=" * 50)
    print("GitHub Statistics Generator")
    print(f"User: {USERNAME}")
    print("=" * 50)

    try:
        stats = calculate_stats(token)
    except Exception as e:
        print(f"\nFATAL: Failed to fetch GitHub data: {e}", file=sys.stderr)
        print("Preserving previous statistics SVG (if it exists).", file=sys.stderr)
        sys.exit(1)

    print("\nGenerating SVG...")
    svg_content = generate_svg(stats)

    # Ensure output directory exists
    output_path = OUTPUT_FILE
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Written to: {output_path}")
    print(f"Size: {len(svg_content)} bytes")

    # Print summary
    print("\n" + "=" * 50)
    print("Statistics Summary:")
    print(f"  Repositories:  {stats['repos_count']}")
    print(f"  Contributions: {stats['contributions']}")
    print(f"  Stars:         {stats['stars']}")
    print(f"  Followers:     {stats['followers']}")
    print(f"  Forks:         {stats['forks']}")
    print(f"  Languages:     {len(stats['languages'])}")
    for lang in stats["languages"]:
        print(f"    {lang['name']}: {lang['percent']}%")
    print(f"  Updated:       {stats['updated_at']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
