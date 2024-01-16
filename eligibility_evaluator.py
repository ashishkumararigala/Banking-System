    def collect_applicant_info():
        applicant_name = input("Enter your full name: ")
        annual_income = float(input("Enter your annual income: "))
        years_at_current_job = int(input("Enter the number of years at your current job: "))
        credit_score = int(input("Enter your credit score: "))

        applicant_info = {
            "name": applicant_name,
            "annual_income": annual_income,
            "years_at_current_job": years_at_current_job,
            "credit_score": credit_score
        }

        return applicant_info



    #  eligibility
    def evaluate_eligibility(applicant_info):
        if applicant_info["annual_income"] >= 30000 and applicant_info["years_at_current_job"] >= 1 and applicant_info[
            "credit_score"] >= 600:
            return True
        else:
            return False



    def display_results(applicant_info, eligible):
        if eligible:
            print("Congratulations, " + applicant_info["name"] + "! You are pre-approved for a credit card.")
        else:
            print("We regret to inform you that you are not currently eligible for a credit card.")
            print("Please review our eligibility criteria and reapply at a later time.")



    applicant_info = collect_applicant_info()
    eligible = evaluate_eligibility(applicant_info)
    display_results(applicant_info, eligible)
