import json
import random
from datetime import datetime, timedelta

REGIONS = [
    "BW", "BY", "HE", "NW", "RP", "SL",
    "SN", "TH", "HB", "HH", "NI", "SH", "BE", "BB", "MV", "SN"
]

HEAT_PUMP_MODELS = [
    ("Alpha Innotec LWD 70A", 4.3),
    ("Daikin Altherma 3", 4.5),
    ("Vaillant aroTHERM plus", 4.1)
]


def random_date(start, end):
    """Return a random datetime between `start` and `end`."""
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)


def generate_project(project_id):
    region = random.choice(REGIONS)
    install_date = random_date(datetime(2023, 1, 1), datetime(2024, 12, 31))
    size_kwp = round(random.uniform(5.0, 20.0), 1)
    num_panels = random.randint(10, 40)
    model, cop = random.choice(HEAT_PUMP_MODELS)

    panel_data = []
    for i in range(1, 6):
        daily_yield = [round(random.uniform(1.0, 6.0), 2) for _ in range(30)]
        panel_data.append({
            "panel_id": f"P-{i:02d}",
            "orientation_deg": random.randint(90, 270),
            "tilt_deg": random.randint(15, 40),
            "daily_yield_kwh": daily_yield,
        })

    return {
        "project_id": f"PV-{project_id:05d}",
        "customer_region": region,
        "installation_date": install_date.strftime("%Y-%m-%d"),
        "system_size_kwp": size_kwp,
        "num_panels": num_panels,
        "heat_pump": {"model": model, "rated_cop": cop},
        "panel_data": panel_data,
    }


def generate_dataset(num_projects=50):
    return [generate_project(i + 1) for i in range(num_projects)]


def main():
    projects = generate_dataset()
    with open("data/projects.json", "w") as f:
        json.dump(projects, f, indent=2)
    print(f"Generated {len(projects)} projects to data/projects.json")


if __name__ == "__main__":
    main()
