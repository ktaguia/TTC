"""Fetch real U.S. Treasury auction bid-to-cover data and write to CSV.

Columns written: year, us_2y_bid_to_cover, us_5y_bid_to_cover
Source: U.S. Treasury FiscalData API — fiscaldata.treasury.gov
"""

import requests
import pandas as pd
from pathlib import Path

BASE = (
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    "/v1/accounting/od/auctions_query"
)
OUT = Path("data/auction_tail_divergence.csv")


def get_btc(term: str, start_year: int = 2016) -> pd.DataFrame:
    rows, page = [], 1
    while True:
        resp = requests.get(
            BASE,
            params={
                "filter": f"security_term:eq:{term}",
                "fields": "auction_date,bid_to_cover_ratio",
                "sort": "auction_date",
                "page[number]": page,
                "page[size]": 1000,
            },
            timeout=30,
        )
        resp.raise_for_status()
        payload = resp.json()
        rows.extend(payload.get("data", []))
        total_pages = int(payload.get("meta", {}).get("total-pages", page))
        if page >= total_pages:
            break
        page += 1

    df = pd.DataFrame(rows)
    df["auction_date"] = pd.to_datetime(df["auction_date"])
    df["bid_to_cover_ratio"] = pd.to_numeric(df["bid_to_cover_ratio"], errors="coerce")
    df["year"] = df["auction_date"].dt.year
    df = df[df["year"] >= start_year]
    return df.groupby("year", as_index=False)["bid_to_cover_ratio"].mean()


print("Fetching 2-Year auction data...")
us2 = get_btc("2-Year")
print(f"  Got {len(us2)} annual rows ({us2['year'].min()}-{us2['year'].max()})")

print("Fetching 5-Year auction data...")
us5 = get_btc("5-Year")
print(f"  Got {len(us5)} annual rows ({us5['year'].min()}-{us5['year'].max()})")

out = (
    us2.rename(columns={"bid_to_cover_ratio": "us_2y_bid_to_cover"})
    .merge(us5.rename(columns={"bid_to_cover_ratio": "us_5y_bid_to_cover"}), on="year")
)

out.to_csv(OUT, index=False)
print("\nSaved to data/auction_tail_divergence.csv")
print(out.to_string(index=False))
