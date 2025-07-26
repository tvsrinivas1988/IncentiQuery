from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()

NUM_REPS = 100
NUM_TERRITORIES = 10
NUM_DRUGS = 15
NUM_SALES = 10000
NUM_QUOTAS = NUM_REPS * 5
NUM_PLANS = 5
NUM_PAYOUTS = NUM_REPS * 4
NUM_ADJUSTMENTS = 200

# Generate sales reps
sales_reps = []
for i in range(NUM_REPS):
    sales_reps.append({
        'rep_id': i + 1,
        'name': fake.name(),
        'email': fake.email(),
        'region': random.choice(['North', 'South', 'East', 'West', 'Central']),
        'start_date': fake.date_between(start_date='-5y', end_date='-1y')
    })

# Generate territories
territories = []
for i in range(NUM_TERRITORIES):
    territories.append({
        'territory_id': i + 1,
        'name': f"Territory {i + 1}",
        'region': random.choice(['North', 'South', 'East', 'West', 'Central']),
        'manager': fake.name()
    })

# Generate drugs
therapeutic_areas = ['Diabetes', 'Cardiovascular', 'Oncology', 'Respiratory', 'Neurology']
drugs = []
for i in range(NUM_DRUGS):
    drugs.append({
        'drug_id': i + 1,
        'name': f"Drug_{i+1}",
        'therapeutic_area': random.choice(therapeutic_areas),
        'launch_date': fake.date_between(start_date='-10y', end_date='-1y')
    })

# Helper for random date
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Generate sales
sales = []
start_sale_date = datetime(2023, 1, 1)
end_sale_date = datetime(2024, 6, 30)
for i in range(NUM_SALES):
    sale_date = random_date(start_sale_date, end_sale_date)
    sales.append({
        'sale_id': i + 1,
        'rep_id': random.randint(1, NUM_REPS),
        'territory_id': random.randint(1, NUM_TERRITORIES),
        'drug_id': random.randint(1, NUM_DRUGS),
        'sale_date': sale_date.strftime("%Y-%m-%d"),
        'units_sold': random.randint(10, 500),
        'revenue': round(random.uniform(1000, 50000), 2)
    })

# Generate quotas
quotas = []
for i in range(NUM_QUOTAS):
    rep_id = (i % NUM_REPS) + 1
    drug_id = random.randint(1, NUM_DRUGS)
    start_period = datetime(2024, 1, 1)
    end_period = datetime(2024, 3, 31)
    target_revenue = round(random.uniform(20000, 100000), 2)
    quotas.append({
        'quota_id': i + 1,
        'rep_id': rep_id,
        'drug_id': drug_id,
        'start_period': start_period.strftime("%Y-%m-%d"),
        'end_period': end_period.strftime("%Y-%m-%d"),
        'target_revenue': target_revenue
    })

# Incentive plans
incentive_plans = [
    {'plan_id': 1, 'name': 'Q1 2024 Diabetes Incentive', 'effective_start': '2024-01-01', 'effective_end': '2024-03-31', 'description': 'Incentive plan for diabetes drugs in Q1 2024'},
    {'plan_id': 2, 'name': 'Q1 2024 Cardiovascular Incentive', 'effective_start': '2024-01-01', 'effective_end': '2024-03-31', 'description': 'Incentive plan for cardiovascular drugs in Q1 2024'},
    {'plan_id': 3, 'name': 'Q2 2024 Oncology Incentive', 'effective_start': '2024-04-01', 'effective_end': '2024-06-30', 'description': 'Incentive plan for oncology drugs in Q2 2024'},
    {'plan_id': 4, 'name': 'Q2 2024 Respiratory Incentive', 'effective_start': '2024-04-01', 'effective_end': '2024-06-30', 'description': 'Incentive plan for respiratory drugs in Q2 2024'},
    {'plan_id': 5, 'name': 'Q2 2024 Neurology Incentive', 'effective_start': '2024-04-01', 'effective_end': '2024-06-30', 'description': 'Incentive plan for neurology drugs in Q2 2024'},
]

# Generate payouts
payouts = []
for i in range(NUM_PAYOUTS):
    rep_id = (i % NUM_REPS) + 1
    plan = incentive_plans[i % len(incentive_plans)]
    payout_date = datetime.strptime(plan['effective_end'], "%Y-%m-%d") + timedelta(days=15)
    payout_amount = round(random.uniform(5000, 25000), 2)
    notes = random.choice(['Met quota', 'Exceeded quota', 'Below quota', 'Bonus for early achievement', 'Clawback adjustment'])
    payouts.append({
        'payout_id': i + 1,
        'rep_id': rep_id,
        'plan_id': plan['plan_id'],
        'payout_date': payout_date.strftime("%Y-%m-%d"),
        'payout_amount': payout_amount,
        'notes': notes
    })

# Generate adjustments
adjustments = []
for i in range(NUM_ADJUSTMENTS):
    payout_id = random.randint(1, NUM_PAYOUTS)
    reason = random.choice(['Clawback', 'Bonus', 'Correction', 'Penalty', 'Data entry error'])
    adjustment_amount = round(random.uniform(-2000, 2000), 2)
    created_at = fake.date_time_between(start_date='-3M', end_date='now')
    adjustments.append({
        'adjustment_id': i + 1,
        'payout_id': payout_id,
        'reason': reason,
        'adjustment_amount': adjustment_amount,
        'created_at': created_at.strftime("%Y-%m-%d %H:%M:%S")
    })

# Function to print INSERTs
def print_insert(table_name, rows, columns):
    for row in rows:
        values = []
        for col in columns:
            val = row[col]
            if isinstance(val, str):
                val = val.replace("'", "''")  # escape single quotes
                values.append(f"'{val}'")
            elif val is None:
                values.append("NULL")
            else:
                values.append(str(val))
        print(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});")
        # Open the file in write mode ("w")
        with open("sqls.txt", "a") as file:
            file.write(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});")

        print("Content written to sql.txt")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
print("-- Sales Reps")
print_insert("sales_reps", sales_reps, ['name', 'email', 'region', 'start_date'])

print("\n-- Territories")
print_insert("territories", territories, ['name', 'region', 'manager'])

print("\n-- Drugs")
print_insert("drugs", drugs, ['name', 'therapeutic_area', 'launch_date'])

print("\n-- Sales")
print_insert("sales", sales, ['rep_id', 'territory_id', 'drug_id', 'sale_date', 'units_sold', 'revenue'])

print("\n-- Quotas")
print_insert("quotas", quotas, ['rep_id', 'drug_id', 'start_period', 'end_period', 'target_revenue'])

print("\n-- Incentive Plans")
print_insert("incentive_plans", incentive_plans, ['name', 'effective_start', 'effective_end', 'description'])

print("\n-- Payouts")
print_insert("payouts", payouts, ['rep_id', 'plan_id', 'payout_date', 'payout_amount', 'notes'])

print("\n-- Adjustments")
print_insert("adjustments", adjustments, ['payout_id', 'reason', 'adjustment_amount', 'created_at'])
