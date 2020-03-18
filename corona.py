import pandas as pd

# https://github.com/CSSEGISandData/COVID-19

# enter date for daily data
date = '03-17-2020'

# csv data sources
daily_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + date + '.csv'
cases_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'

# read csvs
cases = pd.read_csv(cases_url)
recovered = pd.read_csv(recovered_url)
deaths = pd.read_csv(deaths_url)
daily = pd.read_csv(daily_url)

# Michigan daily report
daily[daily['Province/State'] == 'Michigan']

# Michigan cases
# cases[cases['Province/State'] == 'Michigan']