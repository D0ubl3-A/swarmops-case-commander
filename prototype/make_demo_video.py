import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps
import imageio_ffmpeg


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
FRAMES = ARTIFACTS / "video_frames"
OUT = ARTIFACTS / "swarmops-case-commander-demo.mp4"
APP_SCREENSHOT = Path(r"C:\Users\aaron\.barz\artifacts\swarmops-case-commander-screenshot.png")
DECK_SCREENSHOT = Path(r"C:\Users\aaron\.barz\artifacts\swarmops-deck-screenshot.png")
PENDING_JSON = ARTIFACTS / "SO-CASE-001-evidence-report.json"
APPROVED_JSON = ARTIFACTS / "SO-CASE-001-approved-evidence-report.json"

W, H = 1280, 720
BG = (246, 248, 244)
INK = (16, 27, 22)
MUTED = (82, 98, 90)
GREEN = (22, 115, 72)
DARK = (18, 34, 26)
LINE = (214, 224, 218)
WHITE = (255, 255, 255)
RED = (172, 48, 48)
AMBER = (154, 101, 12)


def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


F_TITLE = font(58, True)
F_H2 = font(38, True)
F_BODY = font(26)
F_BODY_BOLD = font(26, True)
F_SMALL = font(20)
F_SMALL_BOLD = font(20, True)


def wrap(draw, text, fnt, width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(draw, text, xy, fnt, fill, width, line_gap=8):
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += draw.textbbox((0, 0), line, font=fnt)[3] + line_gap
    return y


def card(draw, box, fill=WHITE, outline=LINE):
    draw.rounded_rectangle(box, radius=14, fill=fill, outline=outline, width=2)


def paste_fit(canvas, img_path, box):
    img = Image.open(img_path).convert("RGB")
    x1, y1, x2, y2 = box
    fitted = ImageOps.contain(img, (x2 - x1, y2 - y1))
    frame = Image.new("RGB", (x2 - x1, y2 - y1), WHITE)
    frame.paste(fitted, ((frame.width - fitted.width) // 2, (frame.height - fitted.height) // 2))
    canvas.paste(frame, (x1, y1))


def base():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)


def header(draw, label):
    draw.text((48, 34), label.upper(), font=F_SMALL_BOLD, fill=GREEN)


def save(img, idx):
    path = FRAMES / f"frame_{idx:02d}.png"
    img.save(path)
    return path


def frame_title(idx):
    img, draw = base()
    draw.rounded_rectangle((44, 44, W - 44, H - 44), radius=18, fill=DARK)
    draw.text((92, 118), "UIPATH AGENTHACK - MAESTRO CASE TRACK", font=F_SMALL_BOLD, fill=(202, 247, 215))
    draw.text((92, 190), "SwarmOps Case\nCommander", font=F_TITLE, fill=WHITE, spacing=8)
    draw.text((92, 410), "Governed agent swarms for enterprise case work.", font=F_H2, fill=(224, 245, 232))
    for i, text in enumerate(["Bounded agents", "Human approval", "Audit-ready evidence"]):
        x = 92 + i * 365
        draw.rounded_rectangle((x, 548, x + 330, 616), radius=10, fill=(32, 55, 43), outline=(73, 96, 84))
        draw.text((x + 22, 566), text, font=F_BODY, fill=WHITE)
    save(img, idx)


def frame_problem(idx):
    img, draw = base()
    header(draw, "Problem")
    draw.text((48, 92), "Enterprise teams want agent speed\nwithout agent chaos.", font=F_TITLE, fill=INK, spacing=8)
    draw_wrapped(draw, "Procurement, finance, HR, claims, and operations need approvals, evidence, stage control, and auditability before agents can touch real workflows.", (52, 265), F_BODY, MUTED, 920)
    labels = [("Approvals", "Risky actions need human control."), ("Evidence", "Every output needs an audit trail."), ("Stages", "Work moves through governed case states.")]
    for i, (title, body) in enumerate(labels):
        x = 52 + i * 390
        card(draw, (x, 470, x + 350, 620))
        draw.text((x + 24, 500), title, font=F_BODY_BOLD, fill=INK)
        draw_wrapped(draw, body, (x + 24, 542), F_SMALL, MUTED, 285)
    save(img, idx)


def frame_workflow(idx):
    img, draw = base()
    header(draw, "Demo workflow")
    draw.text((48, 90), "Vendor onboarding + rush purchase approval", font=F_H2, fill=INK)
    quote = "Onboard Northstar Components as a new vendor for a $48,500 rush purchase. Validate risk, prepare approval, and create the procurement handoff."
    card(draw, (52, 160, W - 52, 305), fill=(237, 247, 241))
    draw_wrapped(draw, quote, (84, 190), F_BODY_BOLD, INK, 1080)
    stages = ["Intake", "Vendor Data", "Compliance", "Approval", "Handoff", "Audit"]
    for i, stage in enumerate(stages):
        x = 62 + (i % 3) * 390
        y = 390 + (i // 3) * 110
        card(draw, (x, y, x + 340, y + 76))
        draw.text((x + 22, y + 22), f"{i+1:02d}  {stage}", font=F_BODY_BOLD, fill=GREEN)
    save(img, idx)


def frame_app(idx):
    img, draw = base()
    header(draw, "Working prototype")
    draw.text((48, 82), "The command center is already running.", font=F_H2, fill=INK)
    paste_fit(img, APP_SCREENSHOT, (52, 150, 842, 655))
    card(draw, (875, 150, 1228, 655))
    bullets = ["Case timeline renders", "Five bounded agent outputs", "Human approval gate", "Audit-ready JSON", "Export evidence control"]
    y = 185
    for bullet in bullets:
        draw.rounded_rectangle((905, y + 8, 925, y + 28), radius=5, fill=GREEN)
        y = draw_wrapped(draw, bullet, (942, y), F_BODY_BOLD, INK, 245, line_gap=5) + 18
    save(img, idx)


def frame_agents(idx):
    img, draw = base()
    header(draw, "Bounded agents")
    draw.text((48, 82), "Each agent has one scope and one evidence ID.", font=F_H2, fill=INK)
    agents = json.loads(PENDING_JSON.read_text(encoding="utf-8"))["bounded_agents"]
    for i, agent in enumerate(agents):
        x = 52 + (i % 2) * 595
        y = 170 + (i // 2) * 150
        card(draw, (x, y, x + 545, y + 118))
        draw.text((x + 22, y + 18), agent["agent"], font=F_BODY_BOLD, fill=INK)
        draw.text((x + 420, y + 18), agent["evidence_id"], font=F_SMALL_BOLD, fill=GREEN)
        draw_wrapped(draw, agent["output"], (x + 22, y + 58), F_SMALL, MUTED, 485, line_gap=4)
    save(img, idx)


def frame_gate(idx):
    img, draw = base()
    header(draw, "Human approval gate")
    draw.text((48, 82), "High-risk actions stop until a person approves.", font=F_H2, fill=INK)
    card(draw, (70, 180, 610, 560), fill=(255, 246, 232))
    draw.text((105, 220), "Blocked action", font=F_BODY_BOLD, fill=AMBER)
    draw_wrapped(draw, "Approve vendor setup after missing artifacts are collected.", (105, 275), F_BODY_BOLD, INK, 430)
    draw.rounded_rectangle((105, 425, 275, 482), radius=8, fill=GREEN)
    draw.text((145, 439), "Approve", font=F_BODY_BOLD, fill=WHITE)
    card(draw, (680, 180, 1210, 560), fill=(234, 248, 240))
    draw.text((715, 220), "Verified state change", font=F_BODY_BOLD, fill=GREEN)
    draw.text((715, 305), "pending_human_approval", font=F_SMALL_BOLD, fill=RED)
    draw.text((715, 360), "-> approved_for_handoff", font=F_BODY_BOLD, fill=GREEN)
    save(img, idx)


def frame_evidence(idx):
    img, draw = base()
    header(draw, "Evidence proof")
    draw.text((48, 82), "The case produces judge-readable evidence artifacts.", font=F_H2, fill=INK)
    approved = json.loads(APPROVED_JSON.read_text(encoding="utf-8"))
    card(draw, (52, 160, W - 52, 620), fill=DARK, outline=DARK)
    snippet = json.dumps({
        "case_id": approved["case_id"],
        "final_status": approved["final_status"],
        "approval_gate": approved["approval_gate"],
        "bounded_agents": len(approved["bounded_agents"]),
        "ui_path_mapping": approved["ui_path_mapping"],
    }, indent=2)
    draw.text((84, 195), snippet, font=font(22), fill=(220, 251, 230))
    save(img, idx)


def frame_uipath(idx):
    img, draw = base()
    header(draw, "UiPath fit")
    draw.text((48, 82), "UiPath owns orchestration. SwarmOps returns evidence.", font=F_H2, fill=INK)
    rows = [
        ("Case stages", "Maestro Case stages"),
        ("Human approval gate", "Human task"),
        ("Safe agent work", "Robot/API step"),
        ("Evidence JSON", "Case artifact"),
        ("Final status", "Case completion state"),
    ]
    y = 170
    for left, right in rows:
        card(draw, (90, y, 1190, y + 76))
        draw.text((125, y + 21), left, font=F_BODY_BOLD, fill=INK)
        draw.text((570, y + 21), "->", font=F_BODY_BOLD, fill=GREEN)
        draw.text((650, y + 21), right, font=F_BODY_BOLD, fill=INK)
        y += 90
    save(img, idx)


def frame_close(idx):
    img, draw = base()
    draw.rounded_rectangle((44, 44, W - 44, H - 44), radius=18, fill=DARK)
    draw.text((92, 120), "FINAL MESSAGE", font=F_SMALL_BOLD, fill=(202, 247, 215))
    draw.text((92, 188), "Fast enough for operations.\nControlled enough for enterprise trust.", font=F_TITLE, fill=WHITE, spacing=8)
    draw_wrapped(draw, "SwarmOps turns agent chaos into governed casework: bounded workers, approval gates, and evidence that judges can inspect.", (96, 445), F_BODY, (224, 245, 232), 960)
    save(img, idx)


def render_frames():
    FRAMES.mkdir(parents=True, exist_ok=True)
    for old in FRAMES.glob("frame_*.png"):
        old.unlink()
    builders = [frame_title, frame_problem, frame_workflow, frame_app, frame_agents, frame_gate, frame_evidence, frame_uipath, frame_close]
    for idx, builder in enumerate(builders, start=1):
        builder(idx)


def render_video():
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg,
        "-y",
        "-framerate", "1/5",
        "-i", str(FRAMES / "frame_%02d.png"),
        "-f", "lavfi",
        "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
        "-shortest",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-c:a", "aac",
        "-b:a", "128k",
        str(OUT),
    ]
    subprocess.run(cmd, check=True)
    print(OUT)


def main():
    render_frames()
    render_video()


if __name__ == "__main__":
    main()
