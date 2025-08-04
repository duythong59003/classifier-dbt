CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  data TEXT,
  labels TEXT
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    input_text TEXT NOT NULL,
    predicted_label VARCHAR(100) NOT NULL,
    confidence_score FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);