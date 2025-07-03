from fpdf import FPDF
from datetime import datetime
from pathlib import Path

FONT_PATH = Path("assets/DejaVuSans.ttf")

def _safe(txt: str) -> str:
    return (
        txt.replace("–", "-").replace("—", "-")
           .replace("“", '"').replace("”", '"')
           .replace("‘", "'").replace("’", "'")
    )

def make_pdf(report: dict) -> bytes:
    pdf = FPDF(unit="pt", format="A4")
    pdf.set_auto_page_break(auto=True, margin=50)
    pdf.add_page()
    pdf.add_font("DejaVu", "", str(FONT_PATH), uni=True)
    pdf.set_font("DejaVu", "", 10)

    # --- Header ------------------------------------------------------
    pdf.image("assets/shield_logo_exact.png", x=40, y=30, w=40)
    pdf.set_font("DejaVu", "", 20)
    pdf.set_xy(90, 35)
    pdf.cell(0, 20, "NichoSec Threat Report", ln=1)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_xy(90, 58)
    pdf.cell(0, 14, f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}", ln=1)
    pdf.ln(20)

    # Effective printable width --------------------------------------
    epw = pdf.w - pdf.l_margin - pdf.r_margin   # <- key line

    # --- Verdict banner ---------------------------------------------
    level = report.get("level", "YELLOW").upper()
    r, g, b = {"RED": (220, 53, 69),
               "YELLOW": (255, 193, 7),
               "GREEN": (40, 167, 69)}.get(level, (108, 117, 125))
    pdf.set_fill_color(r, g, b)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("DejaVu", "", 16)
    pdf.cell(epw, 28, _safe(f"{level} - {report.get('summary','')}"),
             ln=1, fill=True)
    pdf.ln(12)
    pdf.set_text_color(0, 0, 0)

    # --- Reasons -----------------------------------------------------
    pdf.set_font("DejaVu", "", 12)
    pdf.cell(0, 16, "Reasons:", ln=1)
    for r in report.get("reasons", []):
        pdf.multi_cell(epw, 14, _safe(f"- {r}"))   # use epw
    pdf.ln(8)

    # --- IPs ---------------------------------------------------------
    pdf.cell(0, 16, "IPs:", ln=1)
    ips = ", ".join(report.get("ips", [])) or "—"
    pdf.multi_cell(epw, 14, _safe(ips))
    pdf.ln(8)

    # --- Scan time ---------------------------------------------------
    pdf.set_font("DejaVu", "", 10)
    pdf.cell(0, 12, f"Scan time: {report.get('scan_time',0)} s", ln=1)

    # --- Output bytes -----------------------------------------------
    raw = pdf.output(dest="S")              # bytes on fpdf2 ≥2.7
    return raw.encode("latin-1") if isinstance(raw, str) else raw
