"""
email_template.py – Wandelt briefing.md in gestyltes HTML-Email um.

Wird von briefing.py aufgerufen ODER standalone:
  python email_template.py briefing.md briefing_email.html
"""

import re
import datetime
import sys
import os

# ============================================================
# DESIGN TOKENS
# ============================================================

DARK = "#0f0f1a"
GOLD = "#c9a96e"
GOLD_LIGHT = "#e8d5a3"
BLUE = "#2d5bba"
BLUE_BG = "#f5f7fb"
BLUE_TEXT = "#3d5a8a"
GREEN = "#1a8a6e"
GRAY_BG = "#faf9f7"
GRAY_BORDER = "#e0ddd8"
BODY_BG = "#e8e6e1"
TEXT_DARK = "#333"
TEXT_MID = "#444"
TEXT_LIGHT = "#777"
TEXT_MUTED = "#999"
TEXT_FAINT = "#bbb"

SERIF = "Georgia,'Times New Roman',Times,serif"
SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"

# Farben für Summary-Karten (zyklisch)
CARD_COLORS = [GOLD, BLUE, GREEN, "#9b59b6", "#e67e22", "#888"]

# ============================================================
# GERMAN DATE
# ============================================================

MONTHS_DE = {
    1: "Januar", 2: "Februar", 3: "März", 4: "April",
    5: "Mai", 6: "Juni", 7: "Juli", 8: "August",
    9: "September", 10: "Oktober", 11: "November", 12: "Dezember"
}

def german_date():
    today = datetime.date.today()
    return f"{today.day}. {MONTHS_DE[today.month]} {today.year}"

def german_date_short():
    today = datetime.date.today()
    return f"{today.day}", MONTHS_DE[today.month], str(today.year)


# ============================================================
# INLINE FORMATTING
# ============================================================

def _inline(text):
    """**bold** → <strong>, preserve rest."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = text.replace('„', '&bdquo;').replace('"', '&ldquo;')
    return text


# ============================================================
# MARKDOWN PARSER → STRUCTURED SECTIONS
# ============================================================

def parse_briefing(md_text):
    """Parse briefing.md into structured sections."""
    lines = md_text.strip().split("\n")

    sections = {
        "summary_themes": [],
        "deep_dives": [],
        "further_segments": [],
        "thought_impulses": [],
    }

    current_section = None  # 'summary', 'deep_dive', 'further', 'impulses'
    current_dive = None
    current_dive_part = None  # 'body', 'details', 'limits', 'eu'
    current_impulse = None

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        # ── H1 headers ──
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            if "Executive Summary" in title or "Summary" in title:
                current_section = "summary"
            elif "Deep-Dive" in title or "Kern-Analyse" in title:
                current_section = "deep_dives"
            elif "Nachdenken" in title or "LinkedIn" in title or "Impuls" in title:
                current_section = "impulses"
            else:
                current_section = None
            i += 1
            continue

        # ── H2 headers ──
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            if "Weitere" in title or "bemerkenswerte" in title:
                current_section = "further"
                i += 1
                continue
            elif current_section == "deep_dives" or current_section is None:
                current_section = "deep_dives"
                # Start new deep dive
                if current_dive:
                    sections["deep_dives"].append(current_dive)
                current_dive = {
                    "title": re.sub(r'^[\U0001F300-\U0001FAFF\U00002702-\U000027B0\U0000FE00-\U0000FE0F\U0001F900-\U0001F9FF]+\s*', '', title).strip(),
                    "emoji": _extract_emoji(title),
                    "body": [],
                    "details": [],
                    "limits": [],
                    "eu": [],
                }
                current_dive_part = "body"
                i += 1
                continue

        # ── Summary table rows ──
        if current_section == "summary" and stripped.startswith("|"):
            if stripped.replace("|", "").replace("-", "").replace(" ", "") == "":
                i += 1
                continue
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 4 and cells[0] not in ("Thema", "---"):
                theme = re.sub(r'\*\*(.+?)\*\*', r'\1', cells[0])
                sections["summary_themes"].append({
                    "theme": theme,
                    "thesis": cells[1] if len(cells) > 1 else "",
                    "persons": cells[2] if len(cells) > 2 else "",
                    "source": cells[3] if len(cells) > 3 else "",
                })
            i += 1
            continue

        # ── Deep dive content ──
        if current_section == "deep_dives" and current_dive:
            # Section labels
            if "Konkrete Details" in stripped and stripped.startswith("**"):
                current_dive_part = "details"
                i += 1
                continue
            if ("Einschränkung" in stripped or "Offene Fragen" in stripped) and stripped.startswith("**"):
                current_dive_part = "limits"
                i += 1
                continue
            if "Europa-Relevanz" in stripped or "🇪🇺" in stripped:
                current_dive_part = "eu"
                # Check if content is on same line
                eu_text = re.sub(r'.*Europa-Relevanz[:\*]*\s*', '', stripped).strip()
                eu_text = re.sub(r'^\*\*\s*', '', eu_text).strip()
                if eu_text:
                    current_dive["eu"].append(eu_text)
                i += 1
                continue

            if stripped.startswith("- "):
                content = stripped[2:].strip()
                if current_dive_part == "details":
                    current_dive["details"].append(content)
                elif current_dive_part == "limits":
                    current_dive["limits"].append(content)
                elif current_dive_part == "eu":
                    current_dive["eu"].append(content)
                else:
                    current_dive["body"].append(stripped)
            elif stripped:
                if current_dive_part == "eu":
                    current_dive["eu"].append(stripped)
                elif current_dive_part in ("details", "limits"):
                    # Continuation line
                    target = current_dive[current_dive_part]
                    if target:
                        target[-1] += " " + stripped
                    else:
                        current_dive["body"].append(stripped)
                else:
                    current_dive["body"].append(stripped)

            i += 1
            continue

        # ── Further segments ──
        if current_section == "further":
            if stripped.startswith("- "):
                sections["further_segments"].append(stripped[2:].strip())
            elif stripped.startswith("-   "):
                sections["further_segments"].append(stripped[4:].strip())
            elif stripped and sections["further_segments"]:
                sections["further_segments"][-1] += " " + stripped
            i += 1
            continue

        # ── Thought impulses ──
        if current_section == "impulses":
            if stripped.startswith("**Impuls") or stripped.startswith("**Hook"):
                if current_impulse:
                    sections["thought_impulses"].append(current_impulse)
                title = re.sub(r'\*\*(.+?)\*\*\s*', r'\1', stripped).strip()
                title = re.sub(r'^(Impuls|Hook)\s*\d+[:\s]*', '', title).strip()
                current_impulse = {"title": title, "lines": []}
                i += 1
                continue
            if current_impulse and stripped.startswith("- "):
                current_impulse["lines"].append(stripped[2:].strip())
            elif current_impulse and stripped:
                current_impulse["lines"].append(stripped)
            i += 1
            continue

        i += 1

    # Flush remaining
    if current_dive:
        sections["deep_dives"].append(current_dive)
    if current_impulse:
        sections["thought_impulses"].append(current_impulse)

    return sections


def _extract_emoji(text):
    """Extract leading emoji from text."""
    emoji_pattern = re.compile(r'^([\U0001F300-\U0001FAFF\U00002702-\U000027B0\U0000FE00-\U0000FE0F\U0001F900-\U0001F9FF📋🎙💡💭📌]+)')
    match = emoji_pattern.match(text.strip())
    return match.group(1) if match else ""


# ============================================================
# HTML GENERATORS
# ============================================================

def build_email_html(sections):
    """Build complete email HTML from parsed sections."""
    day, month, year = german_date_short()
    parts = []

    # ── Opening ──
    parts.append(f"""<!DOCTYPE html>
<html lang="de">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background-color:{BODY_BG};font-family:{SERIF};-webkit-font-smoothing:antialiased;">

<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">
  {_build_preheader(sections)}
</div>

<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{BODY_BG};">
<tr><td align="center" style="padding:24px 12px;">
<table width="660" cellpadding="0" cellspacing="0" border="0" style="background-color:#ffffff;max-width:660px;width:100%;">
""")

    # ── Masthead ──
    parts.append(f"""
<tr><td style="background-color:{DARK};padding:0;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td style="height:3px;background:linear-gradient(90deg,{GOLD} 0%,{GOLD_LIGHT} 50%,{GOLD} 100%);font-size:0;">&nbsp;</td></tr>
  <tr><td style="padding:28px 40px 24px 40px;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td valign="bottom">
        <p style="margin:0 0 2px 0;font-family:{SANS};font-size:10px;letter-spacing:4px;text-transform:uppercase;color:{GOLD};font-weight:600;">Transatlantic Tech Intelligence</p>
        <p style="margin:0;font-family:{SERIF};font-size:32px;font-weight:700;color:#ffffff;line-height:1.1;letter-spacing:-0.5px;">KI-Briefing</p>
      </td>
      <td align="right" valign="bottom">
        <p style="margin:0 0 2px 0;font-family:{SANS};font-size:20px;font-weight:300;color:#ffffff;line-height:1;">{day}</p>
        <p style="margin:0;font-family:{SANS};font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8b8fa3;">{month} {year}</p>
      </td>
    </tr>
    </table>
  </td></tr>
  <tr><td style="padding:0 40px 20px 40px;">
    <table cellpadding="0" cellspacing="0" border="0"><tr>
      <td style="padding:4px 12px;background-color:rgba(201,169,110,0.15);border-radius:2px;">
        <span style="font-family:{SANS};font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:{GOLD};">TBPN</span>
        <span style="font-family:{SANS};font-size:10px;color:#555;margin:0 6px;">&middot;</span>
        <span style="font-family:{SANS};font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:{GOLD};">All-In Podcast</span>
      </td>
    </tr></table>
  </td></tr>
  </table>
</td></tr>
""")

    # ── Executive Summary ──
    parts.append(f"""
<tr><td style="padding:28px 40px 8px 40px;">
  <p style="margin:0;font-family:{SANS};font-size:10px;letter-spacing:3px;text-transform:uppercase;color:{GOLD};font-weight:600;">Executive Summary</p>
</td></tr>
""")

    for idx, theme in enumerate(sections["summary_themes"]):
        color = CARD_COLORS[idx % len(CARD_COLORS)]
        source_cat = theme.get("source", "")
        parts.append(f"""
<tr><td style="padding:{'12' if idx == 0 else '4'}px 40px 12px 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-left:3px solid {color};">
  <tr><td style="padding:12px 16px;">
    <p style="margin:0 0 4px 0;font-family:{SANS};font-size:10px;letter-spacing:1px;text-transform:uppercase;color:{TEXT_MUTED};">{_inline(source_cat)}</p>
    <p style="margin:0 0 6px 0;font-family:{SERIF};font-size:16px;font-weight:700;color:{DARK};line-height:1.3;">{_inline(theme['theme'])}</p>
    <p style="margin:0 0 6px 0;font-family:{SERIF};font-size:14px;color:{TEXT_MID};line-height:1.55;">{_inline(theme['thesis'][:250])}{'...' if len(theme['thesis']) > 250 else ''}</p>
    <p style="margin:0;font-family:{SANS};font-size:11px;color:#888;">{_inline(theme['persons'])}</p>
  </td></tr>
  </table>
</td></tr>
""")

    # ── Deep Dives ──
    parts.append(f"""
<tr><td style="padding:20px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td style="border-top:2px solid {DARK};padding-top:20px;">
    <p style="margin:0;font-family:{SANS};font-size:10px;letter-spacing:3px;text-transform:uppercase;color:{GOLD};font-weight:600;">Deep-Dive Analysen</p>
  </td></tr>
  </table>
</td></tr>
""")

    for idx, dive in enumerate(sections["deep_dives"]):
        num = f"{idx+1:02d}"

        # Divider (not before first)
        if idx > 0:
            parts.append(f'<tr><td style="padding:24px 40px 0 40px;"><table width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-top:1px solid {GRAY_BORDER};"></td></tr></table></td></tr>')

        # Title
        parts.append(f"""
<tr><td style="padding:20px 40px 0 40px;">
  <p style="margin:0 0 2px 0;font-family:{SANS};font-size:10px;letter-spacing:1px;text-transform:uppercase;color:{GOLD};">{num}</p>
  <p style="margin:0 0 12px 0;font-family:{SERIF};font-size:22px;font-weight:700;color:{DARK};line-height:1.25;letter-spacing:-0.3px;">{_inline(dive['title'])}</p>
</td></tr>
""")

        # Body paragraphs
        if dive["body"]:
            body_text = " ".join(dive["body"])
            parts.append(f"""
<tr><td style="padding:0 40px;">
  <p style="margin:0 0 16px 0;font-family:{SERIF};font-size:15px;color:{TEXT_DARK};line-height:1.7;">{_inline(body_text)}</p>
</td></tr>
""")

        # Details
        if dive["details"]:
            parts.append(f"""
<tr><td style="padding:0 40px;">
  <p style="margin:0 0 8px 0;font-family:{SANS};font-size:10px;letter-spacing:2px;text-transform:uppercase;color:{TEXT_MUTED};font-weight:600;">Konkrete Details</p>
</td></tr>
<tr><td style="padding:0 40px 0 52px;">
""")
            for detail in dive["details"]:
                parts.append(f'  <p style="margin:0 0 10px 0;font-family:{SERIF};font-size:14px;color:{TEXT_MID};line-height:1.6;"><span style="color:{GOLD};font-weight:700;">&#9656;</span>&ensp;{_inline(detail)}</p>')
            parts.append("</td></tr>")

        # Limits
        if dive["limits"]:
            parts.append(f"""
<tr><td style="padding:12px 40px 0 40px;">
  <p style="margin:0 0 8px 0;font-family:{SANS};font-size:10px;letter-spacing:2px;text-transform:uppercase;color:{TEXT_MUTED};font-weight:600;">Einschränkungen / Offene Fragen</p>
</td></tr>
<tr><td style="padding:0 40px 0 52px;">
""")
            for limit in dive["limits"]:
                parts.append(f'  <p style="margin:0 0 8px 0;font-family:{SERIF};font-size:13px;color:{TEXT_LIGHT};line-height:1.6;font-style:italic;"><span style="color:#ccc;font-style:normal;">&#9656;</span>&ensp;{_inline(limit)}</p>')
            parts.append("</td></tr>")

        # EU Relevance
        if dive["eu"]:
            eu_text = " ".join(dive["eu"])
            parts.append(f"""
<tr><td style="padding:16px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{BLUE_BG};border-left:3px solid {BLUE};border-radius:0 3px 3px 0;">
  <tr><td style="padding:14px 18px;">
    <p style="margin:0 0 4px 0;font-family:{SANS};font-size:10px;letter-spacing:2px;text-transform:uppercase;color:{BLUE};font-weight:700;">&#x1F1EA;&#x1F1FA; Europa-Relevanz</p>
    <p style="margin:0;font-family:{SERIF};font-size:13px;color:{BLUE_TEXT};line-height:1.6;">{_inline(eu_text)}</p>
  </td></tr>
  </table>
</td></tr>
""")

    # ── Further Segments ──
    if sections["further_segments"]:
        parts.append(f"""
<tr><td style="padding:24px 40px 0 40px;"><table width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-top:1px solid {GRAY_BORDER};"></td></tr></table></td></tr>
<tr><td style="padding:20px 40px 0 40px;">
  <p style="margin:0 0 16px 0;font-family:{SANS};font-size:10px;letter-spacing:3px;text-transform:uppercase;color:{GOLD};font-weight:600;">Weitere bemerkenswerte Segmente</p>
</td></tr>
<tr><td style="padding:0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{GRAY_BG};border-radius:3px;">
""")
        for idx, seg in enumerate(sections["further_segments"]):
            # Extract label from bold text
            label_match = re.match(r'\*\*(.+?)\*\*[:\s]*(.*)', seg, re.DOTALL)
            if label_match:
                label = label_match.group(1)
                content = label_match.group(2).strip()
            else:
                label = f"Segment {idx+1}"
                content = seg

            border = f'border-bottom:1px solid #eee;' if idx < len(sections["further_segments"]) - 1 else ''
            parts.append(f"""
  <tr><td style="padding:16px 20px;{border}">
    <p style="margin:0 0 4px 0;font-family:{SANS};font-size:10px;letter-spacing:1px;text-transform:uppercase;color:{GOLD};font-weight:600;">{_inline(label)}</p>
    <p style="margin:0;font-family:{SERIF};font-size:13px;color:{TEXT_MID};line-height:1.6;">{_inline(content)}</p>
  </td></tr>
""")
        parts.append("</table></td></tr>")

    # ── Thought Impulses ──
    if sections["thought_impulses"]:
        parts.append(f"""
<tr><td style="padding:28px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-top:2px solid {DARK};padding-top:20px;">
    <p style="margin:0 0 14px 0;font-family:{SANS};font-size:10px;letter-spacing:3px;text-transform:uppercase;color:{GOLD};font-weight:600;">&#x1F4AD; Zum Drüber Nachdenken</p>
  </td></tr></table>
</td></tr>
""")
        for idx, impulse in enumerate(sections["thought_impulses"]):
            title = impulse["title"]
            lines_html = ""
            for line in impulse["lines"]:
                lines_html += f'<p style="margin:4px 0 0 0;font-family:{SERIF};font-size:13px;color:#aaa;line-height:1.55;">{_inline(line)}</p>'

            margin_top = "0" if idx == 0 else "10"
            parts.append(f"""
<tr><td style="padding:{margin_top}px 40px 0 40px;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{DARK};border-radius:3px;">
  <tr><td style="padding:20px 24px;">
    <p style="margin:0 0 8px 0;font-family:{SERIF};font-size:15px;font-weight:700;color:#ffffff;line-height:1.4;">{_inline(title)}</p>
    {lines_html}
  </td></tr>
  </table>
</td></tr>
""")

    # ── Footer ──
    parts.append(f"""
<tr><td style="padding:28px 0 0 0;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td style="height:3px;background:linear-gradient(90deg,{GOLD} 0%,{GOLD_LIGHT} 50%,{GOLD} 100%);font-size:0;">&nbsp;</td></tr>
  </table>
</td></tr>
<tr><td style="padding:20px 40px 24px 40px;background-color:{GRAY_BG};">
  <p style="margin:0 0 8px 0;font-family:{SANS};font-size:11px;color:{TEXT_MUTED};line-height:1.6;">
    <strong style="color:{TEXT_LIGHT};">Quellen-Hinweis:</strong> Dieses Briefing basiert auf TBPN und All-In Podcast &ndash; US-Tech-Podcasts mit Gr&uuml;nder- &amp; Investor-Perspektive. Es bildet die Sicht der US-Tech-Elite ab, nicht die gesamte US-Debatte.
  </p>
  <table width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-top:1px solid #e8e6e1;padding-top:12px;">
    <p style="margin:0;font-family:{SANS};font-size:11px;color:{TEXT_FAINT};">
      Kuratiert von <strong style="color:{TEXT_MUTED};">Julius von Dryander</strong>&ensp;&middot;&ensp;Transatlantic Tech Intelligence
    </p>
  </td></tr></table>
</td></tr>

</table>
</td></tr></table>
</body></html>
""")

    return "".join(parts)


def _build_preheader(sections):
    """Build hidden preheader text from summary themes."""
    themes = [t["theme"] for t in sections["summary_themes"][:3]]
    return " · ".join(themes) if themes else "KI-Briefing"


# ============================================================
# MAIN CONVERSION FUNCTION
# ============================================================

def convert_md_to_email(md_text):
    """Main entry point: Markdown → styled HTML email."""
    sections = parse_briefing(md_text)
    return build_email_html(sections)


# ============================================================
# STANDALONE CLI
# ============================================================

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "briefing.md"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "briefing_email.html"

    if not os.path.exists(input_file):
        print(f"FEHLER: {input_file} nicht gefunden!")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        md = f.read()

    html = convert_md_to_email(md)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Email-HTML erstellt: {output_file} ({len(html):,} Zeichen)")
