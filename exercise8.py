print("=== SECONDS CONVERTER ===")
total_seconds = int(input("Enter the total number of seconds: "))
years = total_seconds // 31536000
remaining_seconds = total_seconds % 31536000
months = remaining_seconds // 2592000
remaining_seconds = remaining_seconds % 2592000
days = remaining_seconds // 86400
remaining_seconds = remaining_seconds % 86400
hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print("----------------------------------------------------")
print("Years:", years)
print("Months:", months)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
