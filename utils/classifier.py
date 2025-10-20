import pandas as pd

def classify_transactions(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Simple rule-based classification for now
    results = []
    for _, row in df.iterrows():
        amount = row.get('amount', 0)
        risk = 'Low'

        if amount > 10000:
            risk = 'High'
        elif amount > 5000:
            risk = 'Medium'

        results.append({
            "transaction_id": row.get('transaction_id', 'N/A'),
            "amount": amount,
            "risk": risk
        })

    return results
