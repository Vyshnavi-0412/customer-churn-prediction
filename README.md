# Customer Churn Prediction

> ✏️ **Status: in progress.** Replace every `TODO` below with your own results and conclusions before sharing this repository.

Predicting which telecom customers are likely to cancel their subscription, so a retention team can target them before they leave.

## Business problem

TODO: In 2–3 sentences, explain why churn matters to a telecom company (lost revenue, acquisition cost vs retention cost) and what decision your model supports.

## Dataset

- **Source:** [IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d) (sample dataset published by IBM)
- **Size:** 7,043 customers, 21 columns
- **Target:** `Churn` (1 = customer left in the last month)
- **Features:** demographics, account details (tenure, contract, payment method, charges) and subscribed services

## Project structure

```
customer-churn-prediction/
├── data/raw/telco_customer_churn.csv   # original data
├── notebooks/churn_analysis.ipynb      # EDA, modelling and evaluation
├── src/data_prep.py                    # loading and cleaning helpers
├── requirements.txt
└── README.md
```

## Approach

TODO: Summarise the steps you took, for example:
1. Data cleaning: how you handled missing `TotalCharges` and why
2. Exploratory analysis: the 3 most useful findings
3. Feature engineering: encoding, scaling, any new features you created
4. Modelling: which models you compared and how you handled class imbalance
5. Evaluation: which metric you optimised for and why

## Results

TODO: Fill in with your own numbers from the notebook.

| Model | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|
| Logistic Regression (baseline) | | | | |
| Random Forest | | | | |
| XGBoost | | | | |

TODO: Add your feature-importance chart and a short explanation of the top drivers of churn.

## Business recommendations

TODO: 2–3 concrete actions a retention team could take based on your findings.

## Dashboard

TODO: If you build the Tableau dashboard, add a screenshot and a link to Tableau Public here.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/churn_analysis.ipynb
```

## What I would do next

TODO: Limitations of this analysis and how you would improve it with more time or data.
