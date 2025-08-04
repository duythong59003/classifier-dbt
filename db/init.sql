CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT
);

CREATE TABLE tfidf (
  doc_id INT,
  term TEXT,
  tfidf_score FLOAT
);
