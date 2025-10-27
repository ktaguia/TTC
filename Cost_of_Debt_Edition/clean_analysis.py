#!/usr/bin/env python3
"""
Cost of Debt Analysis: US Federal Interest Expense Burden
Clean Python script version with proper indentation
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import pandas_datareader.data as web
import warnings

warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("Libraries imported successfully!")
print("📊 FRED Data Reader configured for real-time federal debt analysis")
print(f"Analysis date: {datetime.now().strftime('%Y-%m-%d')}")


def fetch_federal_debt_data():
    """Fetch real federal debt data from FRED API"""
    print("🚀 Fetching REAL federal debt data from FRED...")
    print("This may take a moment for the first run...")
    
    # Define date range for analysis
    start_date = '1990-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')
    
    try:
        # FRED Series IDs for key federal debt metrics
        series_dict = {
            'interest_payments': 'A091RC1Q027SBEA',    # Federal government: Interest payments
            'total_receipts': 'FGRECPT',               # Federal Government Current Receipts
            'total_debt': 'GFDEGDQ188S',               # Federal Debt: Total Public Debt
            'treasury_10y': 'GS10',                    # 10-Year Treasury Rate
            'gdp': 'GDP',                              # Gross Domestic Product
            'treasury_3m': 'GS3M',                     # 3-Month Treasury
        }
        
        print(f"📡 Downloading {len(series_dict)} key economic series from FRED...")
        
        # Download data from FRED
        fred_data = {}
        for name, series_id in series_dict.items():
            try:
                print(f"   • Fetching {name} ({series_id})...")
                fred_data[name] = web.DataReader(series_id, 'fred', start_date, end_date)
            except Exception as e:
                print(f"   ⚠️  Warning: Could not fetch {name}: {e}")
                # Create fallback data if series fails
                dates = pd.date_range(start_date, end_date, freq='Q')
                fred_data[name] = pd.DataFrame(index=dates, columns=[series_id])
                fred_data[name][series_id] = np.nan
        
        print("✅ Data download complete!")
        
        # Convert to quarterly frequency and align all series
        df_quarterly = pd.DataFrame()
        
        # Process each series
        for name, data in fred_data.items():
            if not data.empty:
                # Resample to quarterly and take last value of period
                quarterly_data = data.resample('Q').last()
                df_quarterly[name] = quarterly_data.iloc[:, 0]
        
        # Remove rows with too many missing values
        df_quarterly = df_quarterly.dropna(thresh=4)
        
        # Calculate key derived metrics
        df_federal = df_quarterly.copy()
        
        # Interest Burden: The Core Metric!
        df_federal['interest_burden_pct'] = (
            df_federal['interest_payments'] / df_federal['total_receipts']
        ) * 100
        
        # Debt-to-GDP ratio
        df_federal['debt_to_gdp'] = (df_federal['total_debt'] / df_federal['gdp']) * 100
        
        # Implied average interest rate on federal debt
        df_federal['implied_avg_rate'] = (
            df_federal['interest_payments'] * 4 / df_federal['total_debt']
        ) * 100  # Annualized
        
        # Clean the data
        df_federal = df_federal.dropna(subset=['interest_burden_pct', 'total_debt', 'total_receipts'])
        
        print("\n📊 REAL FEDERAL DEBT DATA LOADED SUCCESSFULLY!")
        print(f"   • Data Range: {df_federal.index[0].strftime('%Y-%m')} to {df_federal.index[-1].strftime('%Y-%m')}")
        print(f"   • Total Quarters: {len(df_federal)}")
        print(f"   • Current Interest Burden: {df_federal['interest_burden_pct'].iloc[-1]:.2f}% of revenue")
        
        return df_federal
        
    except Exception as e:
        print(f"❌ Error fetching FRED data: {e}")
        print("🔄 Falling back to realistic demonstration data...")
        return create_demo_data()


def create_demo_data():
    """Create realistic demonstration data"""
    # Create realistic demonstration data based on actual historical patterns
    years = pd.date_range('1990-01-01', '2024-10-01', freq='Q')
    n_periods = len(years)
    
    # Set random seed for reproducible demo data
    np.random.seed(42)
    
    # Create realistic federal data patterns
    base_receipts = 800  # Starting point in billions
    receipts_growth = np.random.normal(1.02, 0.05, n_periods)
    total_receipts = [base_receipts]
    for growth in receipts_growth[1:]:
        total_receipts.append(total_receipts[-1] * growth)
    
    # Debt grows faster than receipts (realistic pattern)
    base_debt = 3000  # Starting debt in billions
    debt_growth = np.random.normal(1.025, 0.03, n_periods)
    total_debt = [base_debt]
    for growth in debt_growth[1:]:
        total_debt.append(total_debt[-1] * growth)
    
    # Treasury rates vary over time (realistic cycle)
    treasury_base = np.sin(np.linspace(0, 4*np.pi, n_periods)) * 2 + 4
    treasury_10y = np.maximum(treasury_base + np.random.normal(0, 0.5, n_periods), 0.1)
    
    # Interest payments based on debt and average rates
    avg_debt_rate = treasury_10y * 0.8 + np.random.normal(0, 0.3, n_periods)
    avg_debt_rate = np.maximum(avg_debt_rate, 0.5)  # Floor at 0.5%
    interest_payments = np.array(total_debt) * np.array(avg_debt_rate) / 400
    
    df_federal = pd.DataFrame({
        'total_receipts': total_receipts,
        'total_debt': total_debt,
        'treasury_10y': treasury_10y,
        'interest_payments': interest_payments,
        'gdp': np.array(total_receipts) * 5.2  # Rough GDP multiplier
    }, index=years)
    
    # Calculate key metrics
    df_federal['interest_burden_pct'] = (
        df_federal['interest_payments'] / df_federal['total_receipts']
    ) * 100
    df_federal['debt_to_gdp'] = (df_federal['total_debt'] / df_federal['gdp']) * 100
    df_federal['implied_avg_rate'] = (
        df_federal['interest_payments'] * 4 / df_federal['total_debt']
    ) * 100
    
    print("✅ Realistic demonstration data created successfully!")
    print(f"   • Data Range: {df_federal.index[0].strftime('%Y-%m')} to {df_federal.index[-1].strftime('%Y-%m')}")
    print(f"   • Demo Interest Burden: {df_federal['interest_burden_pct'].iloc[-1]:.2f}% of revenue")
    print(f"   • Demo Peak Burden: {df_federal['interest_burden_pct'].max():.2f}% of revenue")
    
    return df_federal


def create_visualization(df_federal):
    """Create the main Interest Expense Burden visualization"""
    print("📊 Creating Interest Expense Burden visualization...")
    
    plt.figure(figsize=(14, 8))
    
    # Main chart
    plt.plot(df_federal.index, df_federal['interest_burden_pct'],
             linewidth=3, color='#d62728', marker='o', markersize=3, alpha=0.8)
    
    # Risk threshold lines
    plt.axhline(y=20, color='red', linestyle='--', alpha=0.7, linewidth=2, label='Critical Level (20%)')
    plt.axhline(y=15, color='orange', linestyle='--', alpha=0.7, linewidth=2, label='High Risk (15%)')
    plt.axhline(y=10, color='gold', linestyle='--', alpha=0.7, linewidth=2, label='Moderate Risk (10%)')
    plt.axhline(y=5, color='green', linestyle='--', alpha=0.5, linewidth=2, label='Comfortable (5%)')
    
    # Highlight recent trend (last 5 years)
    recent_data = df_federal.tail(20)
    plt.plot(recent_data.index, recent_data['interest_burden_pct'],
             linewidth=6, color='darkred', alpha=0.6, label='Recent 5Y Trend')
    
    # Current point highlighting
    current_point = df_federal.iloc[-1]
    plt.scatter(current_point.name, current_point['interest_burden_pct'],
               s=200, color='red', zorder=5, edgecolor='black', linewidth=2)
    plt.annotate(f'Current: {current_point["interest_burden_pct"]:.1f}%',
                xy=(current_point.name, current_point['interest_burden_pct']),
                xytext=(20, 20), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.9),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'),
                fontsize=12, fontweight='bold')
    
    # Styling
    plt.title('🎯 US Federal Interest Payments as % of Revenue\n(The Ultimate Fiscal Stress Indicator)',
              fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Interest Payments (% of Revenue)', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=14, fontweight='bold')
    plt.legend(loc='upper left', fontsize=11)
    plt.grid(True, alpha=0.3)
    
    # Add background shading for risk zones
    plt.axhspan(20, 25, alpha=0.1, color='red', label='_nolegend_')
    plt.axhspan(15, 20, alpha=0.1, color='orange', label='_nolegend_')
    plt.axhspan(10, 15, alpha=0.1, color='gold', label='_nolegend_')
    plt.axhspan(0, 10, alpha=0.05, color='green', label='_nolegend_')
    
    plt.tight_layout()
    plt.show()
    
    return current_point


def generate_analysis_summary(df_federal):
    """Generate final analysis summary"""
    print("📰 COST OF DEBT NEWSLETTER - BOJ EDITION")
    print("=" * 60)
    print("🎯 CORE ANALYSIS: Federal Interest Expense Burden")
    print("=" * 60)
    
    print(f"\n📊 DATASET OVERVIEW:")
    print(f"   • Time Period: {df_federal.index[0].strftime('%Y-%m')} to {df_federal.index[-1].strftime('%Y-%m')}")
    print(f"   • Total Quarters: {len(df_federal)}")
    
    print(f"\n🔥 KEY FINDINGS:")
    current_burden = df_federal['interest_burden_pct'].iloc[-1]
    peak_burden = df_federal['interest_burden_pct'].max()
    avg_burden = df_federal['interest_burden_pct'].mean()
    
    print(f"   • CURRENT Interest Burden: {current_burden:.2f}% of federal revenue")
    print(f"   • PEAK Interest Burden: {peak_burden:.2f}% (historical maximum)")
    print(f"   • AVERAGE Interest Burden: {avg_burden:.2f}% (34-year average)")
    print(f"   • Current vs Peak: {current_burden/peak_burden*100:.1f}% of historical peak")
    
    # Risk Assessment
    if current_burden > 20:
        risk_level = "🚨 CRITICAL"
    elif current_burden > 15:
        risk_level = "⚠️  HIGH RISK"
    elif current_burden > 10:
        risk_level = "⚡ MODERATE"
    else:
        risk_level = "✅ MANAGEABLE"
    
    print(f"\n🎯 RISK ASSESSMENT: {risk_level} ({current_burden:.1f}%)")
    
    print("\n" + "=" * 60)
    print("📰 ANALYSIS COMPLETE - Ready for Newsletter Publication!")
    print("=" * 60)


def main():
    """Main analysis function"""
    print("🚀 Starting Federal Interest Expense Burden Analysis...")
    
    # Fetch data
    df_federal = fetch_federal_debt_data()
    
    # Create visualization
    current_point = create_visualization(df_federal)
    
    # Generate summary
    generate_analysis_summary(df_federal)
    
    print("✅ Analysis complete!")
    return df_federal


if __name__ == "__main__":
    df_federal = main()