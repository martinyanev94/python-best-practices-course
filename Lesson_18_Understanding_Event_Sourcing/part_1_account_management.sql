CREATE TABLE accounts (
    id INT PRIMARY KEY,
    balance DECIMAL(10, 2) NOT NULL
);
CREATE TABLE account_events (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
