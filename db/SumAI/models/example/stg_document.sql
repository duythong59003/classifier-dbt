SELECT 
    ROW_NUMBER() OVER (ORDER BY data) as id,
    TRIM(data) as data,
    TRIM(labels) as actual_label,
    LENGTH(data) as text_length,
    ARRAY_LENGTH(STRING_TO_ARRAY(data, ' '), 1) as word_count,
    CURRENT_TIMESTAMP as processed_at
FROM {{ source('raw_text', 'documents') }}
WHERE data IS NOT NULL 
  AND labels IS NOT NULL
  AND LENGTH(TRIM(data)) > 10