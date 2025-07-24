# Custom exception
class LowCreditScoreError(Exception):
    pass

def check_loan_eligibility():
    try:
        income = float(input("Enter your annual income in INR: "))
        assert income > 0, "Income must be positive."

        credit_score = int(input("Enter your credit score (300-900): "))
        if credit_score < 300 or credit_score > 900:
            raise ValueError("Credit score must be between 300 and 900.")

        if credit_score < 650:
            raise LowCreditScoreError("Credit score too low for loan approval.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except AssertionError as ae:
        print(f"Input error: {ae}")
    except LowCreditScoreError as le:
        print(f"Loan Denied: {le}")
    else:
        print("🎉 Congratulations! You are eligible for the loan.")
    finally:
        print("✅ Loan eligibility check complete.")

# Run the function
check_loan_eligibility()
