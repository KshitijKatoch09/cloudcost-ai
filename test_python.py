import boto3
import pandas as pd
import numpy as np
from datetime import datetime

print("="*50)
print("CloudCost AI - Environment Test")
print("="*50)

#Test Python
print(f"\n Python Working!")
print(f" Current time: {datetime.now()}")

#Test Pandas
df = pd.DataFrame({'cost': [100,150,200]})
print(f" \n Pandas Working!")
print(f" Average cost: ${df['cost'].mean()}")

#Test Numpy
arr = np.array([1,2,3,4,5])
print(f" \n Numpy Working!")
print(f" Array sum: {arr.sum()}")

#Test Boto3
print(f" \n boto3 (AWS SDK) imported successfully!")

print("\n" + "="*50)
print("All tests passed! Environment ready.")
print("="*50)