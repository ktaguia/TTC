"""
Fetches real G7 credit data from the World Bank API and writes to
data/credit_allocation_spread.csv. Run from the Warehouse_Edition/ directory.

Sources:
  - GC.DOD.TOTL.GD.ZS : Central government debt, total (% of GDP)
  - FS.AST.PRVT.GD.ZS  : Domestic credit to private sector (% of GDP)
  World Bank Open Data — api.worldbank.org/v2
"""

import sys
from pathlib import Path

import pandas as pd
import requests

G7 = ["US", "GB", "DE", "FR", "IT", "JP", "CA"]
BASE = "https://api.worldbank.org/v2"
OUT = Path(__file__).parent / "data" / "credit_allocation_spread.csv"
START_YEAR = 2013
END_YEAR = 2024


def fetch_indicator(indicator: str, countries: list[str]) -> pd.DataFrame:
    """Return a tidy DataFrame with columns [year, country_code, value]."""
    codes = ";".join(countries)
    url = (
        f"{BASE}/country/{codes}/indicator/{indicator}"
        f"?format=json&date={START_YEAR}:{END_YEAR}&per_page=1000"
    )
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    payload = resp.json()
    if len(payload) < 2:
        raise ValueError(f"Unexpected payload for {indicator}: {payload}")
    rows = [
        {
            "year": int(r["date"]),
            "country": r["countryiso3code"],
            "value": r["value"],
        }
        for r in payload[1]
        if r["value"] is not None
    ]
    print(f"  {len(rows)} observations across {len(set(r['country'] for r in rows))} countries")
    return pd.DataFrame(rows)


def main() -> None:
    print("Fetching G7 government debt (% GDP)...")
    gov_df = fetch_indicator("GC.DOD.TOTL.GD.ZS", G7)

    print("Fetching G7 private credit (% GDP)...")
    priv_df = fetch_indicator("FS.AST.PRVT.GD.ZS", G7)

    # G7 annual average government debt % GDP
    gov_avg = (
        gov_df.groupby("year")["value"]
        .mean()
        .rename("g7_govt_debt_pct_gdp")
        .reset_index()
    )

    # G7 annual average private credit % GDP, then YoY change
    priv_avg = (
        priv_df.groupby("year")["value"]
        .mean()
        .rename("priv_credit_pct_gdp")
        .reset_index()
        .sort_values("year")
    )
    priv_avg["private_credit_growth"] = priv_avg["priv_credit_pct_gdp"].diff()

    # Merge and keep years where both are available
    merged = pd.merge(gov_avg, priv_avg[["year", "private_credit_growth"]], on="year")
    merged = merged.dropna().sort_values("year").reset_index(drop=True)

    # Rename to match the column expected by Chart 2
    merged = merged.rename(columns={"g7_govt_debt_pct_gdp": "g7_sovereign_share_bank_assets"})
    merged = merged[["year", "g7_sovereign_share_bank_assets", "private_credit_growth"]]

    merged.to_csv(OUT, index=False, float_format="%.4f")
    print(f"\nWrote {len(merged)} rows to {OUT}")
    print(merged.to_string(index=False))


if __name__ == "__main__":
    main()
