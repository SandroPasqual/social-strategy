const express = require('express');
const { Pool } = require('pg');
const path = require('path');

const app = express();
const PORT = 3001;

const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '5432'),
  database: process.env.DB_NAME || 'bexiter',
  user: process.env.DB_USER || 'bexiter',
  password: process.env.DB_PASS || 'bexiter',
});

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Get all posts
app.get('/api/posts', async (req, res) => {
  try {
    const result = await pool.query(
      'SELECT id, number, theme, title, text_s1, text_s2, text_s3, status, image_path, created_at, exported_at, updated_at FROM image_builder_posts ORDER BY number'
    );
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get single post
app.get('/api/posts/:id', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM image_builder_posts WHERE id = $1', [req.params.id]);
    if (result.rows.length === 0) return res.status(404).json({ error: 'Post not found' });
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update post text
app.put('/api/posts/:id', async (req, res) => {
  try {
    const { text_s1, text_s2, text_s3 } = req.body;
    const result = await pool.query(
      `UPDATE image_builder_posts SET text_s1 = $1, text_s2 = $2, text_s3 = $3,
       status = CASE WHEN status = 'exported' THEN 'modified' ELSE status END,
       updated_at = NOW()
       WHERE id = $4 RETURNING *`,
      [text_s1, text_s2 || null, text_s3 || null, req.params.id]
    );
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update post title
app.put('/api/posts/:id/title', async (req, res) => {
  try {
    const { title } = req.body;
    const result = await pool.query(
      `UPDATE image_builder_posts SET title = $1, updated_at = NOW()
       WHERE id = $2 RETURNING *`,
      [title, req.params.id]
    );
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Mark post as exported
app.put('/api/posts/:id/export', async (req, res) => {
  try {
    const { image_path } = req.body;
    const result = await pool.query(
      `UPDATE image_builder_posts SET status = 'exported', image_path = $1,
       exported_at = NOW(), updated_at = NOW()
       WHERE id = $2 RETURNING *`,
      [image_path, req.params.id]
    );
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Import from posts.txt
app.post('/api/import', async (req, res) => {
  try {
    const fs = require('fs');
    const postsPath = path.join(__dirname, 'posts.txt');
    const content = fs.readFileSync(postsPath, 'utf-8');
    const blocks = content.split('---').filter(b => b.trim());

    for (const block of blocks) {
      const lines = block.trim().split('\n').map(l => l.trim()).filter(l => l);
      if (lines.length < 2) continue;

      const titleLine = lines[0];
      const match = titleLine.match(/^(\d+)-(white|black)-(.+)$/);
      if (!match) continue;

      const number = parseInt(match[1]);
      const theme = match[2];
      const title = titleLine;
      const textLines = lines.slice(1);

      // Check if already exists
      const existing = await pool.query('SELECT id FROM image_builder_posts WHERE number = $1', [number]);
      if (existing.rows.length > 0) {
        await pool.query(
          `UPDATE image_builder_posts SET title = $1, text_s1 = $2, text_s2 = $3, text_s3 = $4, updated_at = NOW()
           WHERE number = $5`,
          [title, textLines[0] || null, textLines[1] || null, textLines[2] || null, number]
        );
      } else {
        await pool.query(
          `INSERT INTO image_builder_posts (number, theme, title, text_s1, text_s2, text_s3, status, created_at)
           VALUES ($1, $2, $3, $4, $5, $6, 'draft', NOW())`,
          [number, theme, title, textLines[0] || null, textLines[1] || null, textLines[2] || null]
        );
      }
    }

    res.json({ message: 'Import complete' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`LinkedIn Image Builder running on http://localhost:${PORT}`);
});
