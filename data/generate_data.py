import csv
import random
import datetime

random.seed(42)

acts = ['Registration', 'Triage', 'X-Ray', 'Blood Test',
        'Consultation', 'Surgery', 'Recovery', 'Discharge']

depts = {
    'Registration': 'OPD',
    'Triage': 'ER',
    'X-Ray': 'Radiology',
    'Blood Test': 'Lab',
    'Consultation': 'OPD',
    'Surgery': 'OT',
    'Recovery': 'ICU',
    'Discharge': 'OPD'
}

names = ['Ravi Kumar', 'Meena Sharma', 'Arjun Patel', 'Priya Singh',
         'Ahmed Khan', 'Sneha Reddy', 'Vikram Joshi', 'Anita Desai',
         'Rahul Verma', 'Kavita Nair', 'Suresh Iyer', 'Pooja Gupta',
         'Manish Rao', 'Deepa Menon', 'Ajay Kulkarni', 'Neha Bose',
         'Rohit Malhotra', 'Sonia Chatterjee', 'Kiran Pillai', 'Amit Trivedi']

rows = [['case_id', 'patient_name', 'event_activity', 'event_time', 'department']]

for i in range(1, 501):
    case_id = f'P{str(i).zfill(4)}'
    patient = random.choice(names)
    num_events = random.randint(4, 8)
    chosen_acts = random.sample(acts, num_events)

    case_events = []
    start = datetime.datetime(2024, 1, 15) + datetime.timedelta(days=random.randint(0, 20))
    for a in chosen_acts:
        start += datetime.timedelta(hours=random.randint(1, 3), minutes=random.choice([0, 15, 30, 45]))
        case_events.append([case_id, patient, a, start.strftime('%Y-%m-%d %H:%M:%S'), depts[a]])

    case_events.sort(key=lambda r: r[3])
    rows.extend(case_events)

with open('clinical_events.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f'Done. Total rows written: {len(rows) - 1}')