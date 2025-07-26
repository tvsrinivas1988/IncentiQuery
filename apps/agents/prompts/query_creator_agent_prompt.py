query_creator_agent_prompt="""
Given an input question, create a syntactically correct PostgreSQL query.
Only use the following tables and columns:

Table: sales_reps(id, name, email, region,start_date)
Table: territories(id, name, region, manager)
Table: drugs(id, name, therapeutic_area, launch_date)
Table: sales(id, rep_id, territory_id,drug_id, sale_date,units_sold,revenue)
Table: quotas(id, rep_id, drug_id, start_period,end_period,target_revenue)
Table: incentive_plans(id, name, effective_start, effective_end,description)
Table: payouts(id, rep_id, plan_id, payout_date,payout_amount,notes)
Table: adjustments(id, payout_id, reason, adjustment_amount,created_at)


Use table aliases where appropriate.
Return only the SQL query.

Question: {question}
"""