from pathlib import Path
import pandas as pd

STORE = Path(__file__).parent.absolute() / "data"
STORE.mkdir(parents=True, exist_ok=True)


def beds(url="https://stopcorona.tn.gov.in/beds.php"):
    df = pd.read_html(url, attrs={"id": "dtBasicExample"})
    df = df[0]
    df.columns = [c[0] if c[0] == c[1] else " ".join(c) for c in df.columns]
    df.to_csv(STORE / "beds.csv", index=False)
    # archive hourly
    now = pd.to_datetime('now').tz_localize('UTC').tz_convert('Asia/Calcutta')
    now = now.strftime("%Y-%m-%d--%H")
    print(f"{now}.csv with {len(df)} rows")
    df.to_csv(STORE / f"beds-{now}.csv", index=False)


if __name__ == "__main__":
    #
    beds()