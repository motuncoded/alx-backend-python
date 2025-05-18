def stream_user_ages():
    # Simulated large dataset of ages (could come from a file, DB, etc.)
    # Replace this with code to read from a real data source as needed
    ages = [25, 30, 22, 40, 28, 35, 19, 50, 45, 33, 29]
    for age in ages:
        yield age

def compute_average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    average_age = total_age / count if count else 0
    print(f"Average age of users: {average_age}")

if __name__ == "__main__":
    compute_average_age()