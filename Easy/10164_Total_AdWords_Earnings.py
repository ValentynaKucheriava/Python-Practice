-- https://platform.stratascratch.com/coding/10164-total-adwords-earnings?code_type=2

import pandas as pd
total_earnings = google_adwords_earnings.groupby('business_type')['adwords_earnings'].sum().reset_index()
total_earnings.columns = ['business_type', 'total_adwords_earnings']
print(total_earnings)
