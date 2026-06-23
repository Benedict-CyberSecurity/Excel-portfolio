"""synthetic_phishing_log_generator.ipynb

Original file is located at
    https://colab.research.google.com/drive/19zlnnLcxQVUVEArgBz-5GB0gq2-M96Ta
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Setup parameters
num_records = 5000
start_date = datetime(2026, 1, 1)

departments = ['Finance', 'HR', 'IT', 'Sales', 'Operations', 'Executive']
phish_types = ['Credential Harvesting', 'Malware Delivery', 'BEC/Whaling', 'Urgent Invoice']
employee_actions = ['Ignored', 'Deleted', 'Reported to IT', 'Clicked Link', 'Downloaded Attachment']

# Top-Level Domains to simulate lookalikes
spoofed_domains = ['micros0ft-security.com', 'secure-bank-login.net', 'hr-benefits-portal.org', 'invoice-processing.co']

data = []

for i in range(num_records):
    # Generate a realistic timestamp over a 90-day period
    random_days = random.randint(0, 90)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    timestamp = start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

    # Injecting logical bias
    if random.random() < 0.40:
        dept = 'Finance'
        phish_type = 'Urgent Invoice'
    else:
        dept = random.choice(departments)
        phish_type = random.choice(phish_types)

    # Executives are rare but highly targeted by Whaling
    if dept == 'Executive':
        phish_type = 'BEC/Whaling'

    # Match actions with some risk probability (Executives might click less, Sales might click more)
    if dept == 'Sales':
        action = random.choice(['Clicked Link', 'Ignored', 'Reported to IT'])
    else:
        action = np.random.choice(employee_actions, p=[0.4, 0.3, 0.15, 0.10, 0.05]) # Weighted probabilities

    sender = random.choice(spoofed_domains)

    data.append({
        'Incident_ID': f'INC-2026-{i+10000}',
        'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'Target_Department': dept,
        'Sender_Domain': sender,
        'Phishing_Type': phish_type,
        'Employee_Action': action
    })

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('synthetic_phishing_logs.csv', index=False)
print("Dataset generated successfully as 'synthetic_phishing_logs.csv'!")