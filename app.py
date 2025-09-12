"""
Seeded content comes from your Resume.pdf. :contentReference[oaicite:0]{index=0}
"""
from pathlib import Path
import csv
from flask import Flask, render_template, url_for

app = Flask(__name__)
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def _write_csv(path: Path, fieldnames, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

def ensure_seed_data():
    # Create CSVs only if missing
    # ---- skills.csv ----
    skills_csv = DATA_DIR / "skills.csv"
    if not skills_csv.exists():
        _write_csv(
            skills_csv,
            ["category", "item"],
            [
                # ML Engineering
                {"category":"ML Engineering","item":"Python"},
                {"category":"ML Engineering","item":"C++"},
                {"category":"ML Engineering","item":"TensorFlow"},
                {"category":"ML Engineering","item":"TensorFlow Lite"},
                {"category":"ML Engineering","item":"Classification"},
                {"category":"ML Engineering","item":"CNNs"},
                {"category":"ML Engineering","item":"LSTMs"},
                {"category":"ML Engineering","item":"Audio DSP"},
                {"category":"ML Engineering","item":"MFCCs"},
                {"category":"ML Engineering","item":"Confusion Matrices"},
                # Data Pipelines
                {"category":"Data Pipelines","item":"NumPy"},
                {"category":"Data Pipelines","item":"Pandas"},
                {"category":"Data Pipelines","item":"SQL"},
                {"category":"Data Pipelines","item":"Data Cleaning"},
                {"category":"Data Pipelines","item":"Data Labeling"},
                {"category":"Data Pipelines","item":"Feature Engineering"},
                {"category":"Data Pipelines","item":"Data Provenance"},
                {"category":"Data Pipelines","item":"ETL Scripts"},
                {"category":"Data Pipelines","item":"Linux"},
                {"category":"Data Pipelines","item":"Visualization"},
                # MLOps
                {"category":"MLOps","item":"CI/CD"},
                {"category":"MLOps","item":"GitHub Actions"},
                {"category":"MLOps","item":"Docker"},
                {"category":"MLOps","item":"GCP / Cloud Run"},
                {"category":"MLOps","item":"Model Versioning"},
                {"category":"MLOps","item":"Experiment Tracking"},
                {"category":"MLOps","item":"A/B Testing"},
                {"category":"MLOps","item":"Testing Automation"},
                {"category":"MLOps","item":"Documentation"},
                # Performance
                {"category":"Performance","item":"Quantization"},
                {"category":"Performance","item":"Latency Tuning"},
                {"category":"Performance","item":"Memory Optimization"},
                {"category":"Performance","item":"Profiling"},
                {"category":"Performance","item":"Tensor Arena"},
                {"category":"Performance","item":"DMA / I2S / I2C"},
                {"category":"Performance","item":"Thread Priorities"},
                {"category":"Performance","item":"UI Optimization"},
            ],
        )

    # ---- education.csv ----
    edu_csv = DATA_DIR / "education.csv"
    if not edu_csv.exists():
        _write_csv(
            edu_csv,
            ["degree", "school", "date", "notes"],
            [
                {"degree":"Masters of Science, Artificial Intelligence",
                 "school":"San Jose State University",
                 "date":"May 2027",
                 "notes":""},
                {"degree":"Bachelor of Science, Data Science",
                 "school":"San Jose State University",
                 "date":"May 2025",
                 "notes":"Summa Cum Laude; Presidents Scholar; AS Leadership Scholar"},
            ],
        )

    # ---- experience.csv ----
    exp_csv = DATA_DIR / "experience.csv"
    if not exp_csv.exists():
        _write_csv(
            exp_csv,
            ["role","company","location","start","end","bullets"],
            [
                {"role":"Embedded ML Engineer",
                 "company":"Nuvoton",
                 "location":"San Jose, CA",
                 "start":"Aug 2024","end":"Present",
                 "bullets":"Built scalable data pipelines with Python/NumPy/Pandas; "
                           "Deployed TF/TFLite audio models and cut RAM ~21% via quantization; "
                           "Implemented C++ inference architecture for multi-model deployment; "
                           "Automated experiments with standardized metrics and confusion matrices; "
                           "Established model lineage, config emission, and CI/CD with GitHub Actions"},
                {"role":"Machine Learning Engineer Intern",
                 "company":"Nuvoton",
                 "location":"San Jose, CA",
                 "start":"May 2024","end":"Aug 2024",
                 "bullets":"Raised on-device accuracy 49%→90% with TF and rigorous evaluation; "
                           "Built YAML-driven pipeline with checksums for reproducibility; "
                           "Applied int8 quantization and memory profiling for latency and footprint; "
                           "Automated end-to-end CI/CD to on-device tests; "
                           "Engineered C++ harness and Python evaluator with nightly monitoring"},
                {"role":"Machine Learning Intern",
                 "company":"Yandex",
                 "location":"Remote",
                 "start":"May 2023","end":"Aug 2023",
                 "bullets":"Automated Pandas/NumPy pipelines processing 1M+ records daily; "
                           "Unified preprocessing for train/validation via CI/CD; "
                           "Built dashboards to expose sampling bias and monitor drift; "
                           "Automated remote servers with Bash/Cron and logging; "
                           "Authored standardized preprocessing docs and workshop"},
            ],
        )

    # ---- projects.csv ----
    proj_csv = DATA_DIR / "projects.csv"
    if not proj_csv.exists():
        _write_csv(
            proj_csv,
            ["title","bullets"],
            [
                {"title":"Audio Data – Training",
                 "bullets":"End-to-end audio classification with TF CNNs achieving ~85% accuracy; "
                           "Converted to TFLite with quantization; "
                           "Integrated autogenerated C++ model and real-time audio streaming; "
                           "Sliding-window MFCC/Spectrogram pipeline and reliability filters"},
                {"title":"Audio Data – Auto Testing",
                 "bullets":"Automated end-to-end data and on-device classification; "
                           "Controlled repeated runs and A/B testing; "
                           "Confusion matrix, precision, recall, F1 with Pandas; "
                           "Captured edge predictions via serial with reproducible logs"},
                {"title":"Personal Portfolio Website",
                 "bullets":"LLM-powered assistant with Python backend; "
                           "Docker + GCP Cloud Run CI/CD; "
                           "Cloudflare SSL/security; "
                           "MySQL sessions and low-latency WebSockets"},
            ],
        )

    # ---- involvement.csv ----
    inv_csv = DATA_DIR / "involvement.csv"
    if not inv_csv.exists():
        _write_csv(
            inv_csv,
            ["role","org","start","end","bullets"],
            [
                {"role":"President","org":"AI & ML Club @ SJSU","start":"Jan 2025","end":"Present",
                 "bullets":"Grew attendance 25→85; Expanded leadership 5→27; "
                           "Partnered with industry speakers; Led club ML projects"},
                {"role":"Officer","org":"AI & ML Club @ SJSU","start":"Dec 2023","end":"Jan 2025",
                 "bullets":"Organized events and workshops; Supported student projects"},
            ],
        )

    # ---- links.csv ----
    links_csv = DATA_DIR / "links.csv"
    if not links_csv.exists():
        _write_csv(
            links_csv,
            ["label","url"],
            [
                {"label":"Resume (PDF)","url":"/static/Resume.pdf"},
                {"label":"Website","url":"https://maxdokukin.com"},
                {"label":"GitHub","url":"https://github.com/maxdokukin"},
                {"label":"LinkedIn","url":"https://linkedin.com/in/maxdokukin"},
            ],
        )

def read_csv_dicts(name, split_bullets=False):
    path = DATA_DIR / name
    rows = []
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if split_bullets and "bullets" in row and row["bullets"]:
                    row["bullets"] = [b.strip() for b in row["bullets"].split(";") if b.strip()] \
                                     if ";" in row["bullets"] else [b.strip() for b in row["bullets"].split("•")] \
                                     if "•" in row["bullets"] else [s.strip() for s in row["bullets"].split(" | ")]
                rows.append(row)
    return rows

@app.route("/")
def index():
    ensure_seed_data()
    # group skills by category
    skills = read_csv_dicts("skills.csv")
    skills_by_cat = {}
    for s in skills:
        skills_by_cat.setdefault(s["category"], []).append(s["item"])
    context = {
        "name": "Max Dokukin",
        "tagline": "Student at SJSU",
        "email": "max.dokukin@sjsu.edu",
        "skills_by_cat": skills_by_cat,
        "education": read_csv_dicts("education.csv"),
        "experience": read_csv_dicts("experience.csv", split_bullets=True),
        "projects": read_csv_dicts("projects.csv", split_bullets=True),
        "involvement": read_csv_dicts("involvement.csv", split_bullets=True),
        "links": read_csv_dicts("links.csv"),
    }
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
