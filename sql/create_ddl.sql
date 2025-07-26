-- Table: Sales Representatives
CREATE TABLE sales_reps (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    region VARCHAR(50),
    start_date DATE
);

-- Table: Territories
CREATE TABLE territories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    region VARCHAR(50),
    manager VARCHAR(100)
);

-- Table: Drugs
CREATE TABLE drugs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    therapeutic_area VARCHAR(100),
    launch_date DATE
);

-- Table: Sales Transactions
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    rep_id INTEGER REFERENCES sales_reps(id),
    territory_id INTEGER REFERENCES territories(id),
    drug_id INTEGER REFERENCES drugs(id),
    sale_date DATE NOT NULL,
    units_sold INTEGER,
    revenue DECIMAL(12,2)
);

-- Table: Quotas
CREATE TABLE quotas (
    id SERIAL PRIMARY KEY,
    rep_id INTEGER REFERENCES sales_reps(id),
    drug_id INTEGER REFERENCES drugs(id),
    start_period DATE,
    end_period DATE,
    target_revenue DECIMAL(12,2)
);

-- Table: Incentive Plans
CREATE TABLE incentive_plans (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    effective_start DATE,
    effective_end DATE,
    description TEXT
);

-- Table: Payouts
CREATE TABLE payouts (
    id SERIAL PRIMARY KEY,
    rep_id INTEGER REFERENCES sales_reps(id),
    plan_id INTEGER REFERENCES incentive_plans(id),
    payout_date DATE,
    payout_amount DECIMAL(12,2),
    notes TEXT
);

-- Table: Adjustments
CREATE TABLE adjustments (
    id SERIAL PRIMARY KEY,
    payout_id INTEGER REFERENCES payouts(id),
    reason TEXT,
    adjustment_amount DECIMAL(12,2),
	created_at timestamp
);
