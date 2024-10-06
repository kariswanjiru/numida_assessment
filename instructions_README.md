![Numida](logo.numida.png)

# What are we looking for in an engineer?

We are looking for an experienced Machine Learning engineer who is well-versed in modern ML frameworks and techniques, and can lead the development, optimization, and deployment of scalable models and data pipelines.

Now, before we start. Let's apply the algorithm for model training success:

```py
while not success:
    try:
        model.train(data)
    except ConvergenceError:
        adjust_hyperparameters()
    if model.overfits():
        break
```

## Expectations

- Although we strive for perfection we don't expect everything to be perfect, **just do you**.
- Given the size of the assignment we don't expect everything to be done, **do what you can given the time**.

> The assignment should take about a maximum of **3 hours** to complete.

# Assessment:

Imagine you’re Numida’s first Machine Learning Engineer. You are tasked with building a model that will predict the performance of future loan applications. The model will be used to set interest rates and support Loan Officers’ decision making when completing Due Diligence.

## Overview of Numida and its products:

- Numida provides 30-day working capital loans to small and medium sized businesses in Uganda
- Loan officers are responsible for reviewing and approving (or declining) loan applications
    - Sometimes a customer can cancel their application
    - An application will expire if we are waiting for information from the client which they never provide
- Numida tries to find a reason to lend, rather than looking for a reason to not lend

## Objective:

You have access to training data on ~25k loan applications, and the ~80k payments made against those loans.

Your goal is to use that data to build a model that would be able to predict the performance of 2,000 loans that are currently in Due Diligence (the test data).

> Notes
> - None of the 2,000 loans in Due Diligence are first time applicants.  They are all from businesses that have previously received at least one loan from Numida.  The data on their previous loans is in the training data set.
> - There is no predetermined target variable or definition of good performance - you are encouraged to come up with your own.  That being said, this is how Numida generally thinks about performance
>     - Customers that repay on-time are more likely to be retained which is good for our business
>     - It’s rare for us to relend to a customer that pays back more than 15 days late
>     - Ultimately, yield is one of our most important metrics
> - We generally expect 5% - 10% of loans to be written off

## Requirements

1. **Tools and Technologies**
    - Use Python to implement the solution.
    - You may use Jupyter Notebook if desired.

2. **Clearly defined target variable**
   - Clearly defined target variable and explanation for the choice.
   - Include any assumptions about the problem or data that you make.

3. **A process for training a model that another analyst or engineer could replicate without too much troublet**

4. **The approach should be able to handle the addition of new input variables gracefully**

5. **A list of steps you would take next**

## Bonus

- Training and validating your model (or making predictions) against the 2,000 loans in the test data.
    - This part of the assignment is primarily to provide context and help explain the nature of the challenges faced by Numida
- Note down additional suggestions, given more time


## Instructions:

All the resources you require to do this assessment will be provided along with this README.

### Data sets

- train_loan_data.csv
    - These are all the loans previously taken by the 2,000 customers that currently have a loan application in due diligence
    - There are around 25,000 loans
- train_payment_data.csv
    - These are all the payments made against the loans in the training loan data
    - Customers are encouraged to make payments throughout their loan (rather than relying on a singular payment at the end), though this is not a requirement
- test_loan_data.csv
    - These are all the loans previously taken by the 2,000 customers

### Loan Data Set

| Column Name              | Description                                                                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| loan_id                  |                                                                                                                                                                      |
| business_id              |                                                                                                                                                                      |
| credit_officer_id         | Identifier for the Numida member of staff responsible for approving (and collecting on) the loan                                                                      |
| acquisition_channel      | The channel through which the customer first came to Numida                                                                                                           |
| sector                   | The type of business the customer has - Clinic, or Beauty & Fashion for instance                                                                                      |
| principal                | If the loan was approved, this is the amount (in UGX) that was disbursed. If the loan wasn't approved, this is the amount that the CRO evaluated.                     |
| total_owing_at_issue     | The amount of money the customer was required to pay back when the loan was disbursed. It includes the principal, fees, and interest but does NOT include any penalties. |
| application_number       | Running count of how many times the customer has submitted a loan application.                                                                                        |
| applying_for_loan_number | The `loan_number` that the customer is applying for. There can be many loans for the same customer with the same value since a customer can be declined, and re-apply. |
| employee_count           | The customer-reported number of employees working for the customer.                                                                                                   |
| **The following are only available after the loan has been approved (or declined). The information is missing, null or in an intermediary step before then.**                                     |
| loan_number              | Running count of how many loans the customer has taken up to and including the current loan. Null if the loan has not been approved.                                   |
| approval_status          | Status used to determine whether or not a loan was disbursed. If not, it provides the reason.                                                                         |
| dismissal_description    | The reason for the loan being declined or cancelled.                                                                                                                 |
| payment_status           | The status of the loan (Current: loan is outstanding and before due date, Arrears: outstanding after the due date).                                                   |
| paid_late                | Boolean indicating if the loan was paid back late. If true, the loan was paid back late.                                                                              |
| total_recovered_on_time  | Sum of all payments made before the due date. NULL until the due date has passed.                                                                                      |
| total_recovered_15_dpd   | Sum of all payments made within 15 days after the due date. NULL until 15 days after the due date.                                                                    |
| cash_yield_15_dpd        | Sum of all payments received from the customer by 15 days past the due date, less the principal disbursed. A measure of the gross profit or loss from the loan.        |

### Payment Data

| Column Name       | Description                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------------------|
| loan_id           |                                                                                                     |
| paid_at           | Timestamp of when the payment was made.                                                             |
| amount            | Value of the payment.                                                                               |
| transaction_type  | `Deposit` for a customer payment, `Discount` for a bonus or other discount provided by Numida. Both count equally towards paying off a loan. |

### Submission

- Ensure your code is well-documented and formatted.
    - Include a short README in your repository explaining how to run your code and listing any dependencies.
- Push your code to your GitHub repository.
- Provide a link to your repository and a brief description of your approach.

### Follow-Up Questions

- Be prepared to explain your code, discuss your approach, and suggest improvements during a follow-up session.
- You may be asked to add a few other input variables to your model during the follow-up.

## Evaluation Criteria:

- **Correctness and completeness:** Ensure that your model works as intended, and all key steps are addressed.
- **Scalability:** Your solution should be able to handle the addition of new input variables without breaking or needing major refactoring.
- **Approach clarity:** Be prepared to explain your decisions, assumptions, and results. Clear explanations demonstrate your understanding.
- **Code readability:** Well-documented, clean code is highly valued. It should be easy for another engineer to follow and replicate.
- **Predictive accuracy:** Bonus points if you train and validate your model against the test data.

## Hints

- **Keep it simple:** Solutions that are easy to understand and explain are often more valuable than complex, over-engineered ones.
- **Clarity:** Use clear and easy-to-understand setup instructions. Make sure someone else could pick up your work and reproduce your results.
- **Have fun!** This challenge is as much about demonstrating how you approach a real-world problem as it is about the technical solution itself. Enjoy the process.

At Numida, we thrive on tackling unique challenges to make a difference for small businesses in East Africa. As a Machine Learning Engineer, your work will shape the future of our loan products and the financial success of our clients. We're excited to see your innovative approach to predicting loan performance, and we can't wait to welcome you to the team!
