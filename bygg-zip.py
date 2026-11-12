"""Lager dist/amalie-lite.zip: hele Amalie som én skill for Claude-appen (claude.ai og desktop)."""
import pathlib, shutil, zipfile
rot = pathlib.Path(__file__).parent
ut = rot / "dist" / "amalie"
shutil.rmtree(rot / "dist", ignore_errors=True)
shutil.copytree(rot / "skills" / "skriveregler", ut / "skriveregler")
shutil.copytree(rot / "skills" / "gjennomgang", ut / "gjennomgang")
shutil.copy(rot / "skills" / "amalie" / "SKILL.md", ut / "SKILL.md")
bytt = {"`amalie:skriveregler`": "`skriveregler/SKILL.md`", "`amalie:gjennomgang`": "`gjennomgang/SKILL.md`",
        "amalie:gjennomgang": "gjennomgang/SKILL.md", "amalie:skriveregler": "skriveregler/SKILL.md",
        "Last skillen før du gjør noe annet.": "Les filen før du gjør noe annet."}
for f in ut.rglob("*.md"):
    s = f.read_text()
    for a, b in bytt.items(): s = s.replace(a, b)
    f.write_text(s)
with zipfile.ZipFile(rot / "dist" / "amalie-lite.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(ut.rglob("*")):
        if f.is_file(): z.write(f, f.relative_to(ut.parent))
print("dist/amalie-lite.zip")
