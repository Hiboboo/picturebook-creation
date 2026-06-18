CREATE TABLE IF NOT EXISTS picturebook_records (
  id TEXT PRIMARY KEY,
  series TEXT NOT NULL DEFAULT '',
  theme TEXT NOT NULL DEFAULT '',
  title TEXT NOT NULL,
  series_key TEXT NOT NULL DEFAULT '',
  theme_key TEXT NOT NULL DEFAULT '',
  title_key TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('draft', 'completed', 'archived')),
  summary TEXT NOT NULL DEFAULT '',
  characters TEXT NOT NULL DEFAULT '',
  style TEXT NOT NULL DEFAULT '',
  output_dir TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_picturebook_records_title_key
  ON picturebook_records(title_key);

CREATE INDEX IF NOT EXISTS idx_picturebook_records_lookup_keys
  ON picturebook_records(series_key, theme_key, title_key);
