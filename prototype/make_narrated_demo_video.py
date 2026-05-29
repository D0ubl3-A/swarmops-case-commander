import subprocess
from pathlib import Path

import imageio_ffmpeg

from make_demo_video import FRAMES, ARTIFACTS, render_frames


OUT = ARTIFACTS / "swarmops-case-commander-narrated-demo.mp4"
NARRATION = ARTIFACTS / "swarmops-case-commander-narration.wav"

SCRIPT = """
SwarmOps Case Commander is a governed agent command center for enterprise case work.
The demo uses vendor onboarding and rush purchase approval because it has the exact pattern enterprises struggle with:
messy intake, missing documents, compliance risk, and state-changing actions that need approval.

The system opens a case, delegates safe analysis to bounded agents, blocks high-risk actions for human approval,
and produces audit-ready evidence JSON. The local prototype already runs with a seeded case, five agent outputs,
a pending approval gate, approval-state verification, and generated evidence artifacts.

For UiPath AgentHack, the target integration is UiPath Maestro Case. Maestro owns the case stages and the human task.
SwarmOps returns the plan, risk flags, agent outputs, and evidence manifest.
That turns agent chaos into governed automation: fast enough for operations, controlled enough for enterprise trust.
""".strip()


def powershell_literal(value):
    return "'" + value.replace("'", "''") + "'"


def render_narration():
    ps = f"""
Add-Type -AssemblyName System.Speech
$voice = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voice.Rate = 0
$voice.Volume = 100
$voice.SetOutputToWaveFile({powershell_literal(str(NARRATION))})
$voice.Speak({powershell_literal(SCRIPT)})
$voice.Dispose()
"""
    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
        check=True,
    )


def render_video():
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg,
        "-y",
        "-framerate",
        "1/10",
        "-i",
        str(FRAMES / "frame_%02d.png"),
        "-i",
        str(NARRATION),
        "-shortest",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-r",
        "30",
        "-c:a",
        "aac",
        "-b:a",
        "160k",
        str(OUT),
    ]
    subprocess.run(cmd, check=True)
    print(OUT)


def main():
    render_frames()
    render_narration()
    render_video()


if __name__ == "__main__":
    main()
