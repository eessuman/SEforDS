import pandas as pd
from scipy.stats import linregress

def fit_trendline(year_timestamps, data):
    result = linregress(year_timestamps, data)
    slope = round(result.slope, 3)
    r_squared = round(result.rvalue**2, 3)
    return slope, r_squared

def process_sdg_data(input_excel_file, columns_to_drop):
    df = pd.read_csv(input_excel_file)
    df = df.drop(columns_to_drop)
    df = df.set_index("GeoAreaName").transpose()
    
def country_trendline(country_name):
    df = process_sdg_data(
        r'C:\Users\kwaob\Anim&Simu\FastAPTtest\data\SG_GEN_PARL.csv',
        [
            "Goal",
            "Target",
            "Indicator",
            "SeriesCode",
            "SeriesDescription",
            "GeoAreaCode",
            "Reporting Type",
            "Sex",
            "Units"
        ],
    )