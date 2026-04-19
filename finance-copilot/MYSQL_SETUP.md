# MySQL Setup for Finance Copilot

## Local Development with MySQL

1. Install MySQL on your machine
2. Create a database: `CREATE DATABASE finance_copilot;`
3. Set environment variable: `DATABASE_URL=mysql+pymysql://user:password@localhost/finance_copilot`

## Vercel Deployment with PlanetScale (Free)

1. Go to [PlanetScale](https://planetscale.com) and sign up
2. Create a new database
3. Get the connection string from PlanetScale dashboard
4. In Vercel, add environment variable: `DATABASE_URL=mysql+pymysql://username:password@host/database?ssl_ca=/etc/ssl/certs/ca-certificates.crt`

## Vercel Deployment with Railway (Free)

1. Go to [Railway.app](https://railway.app) and sign up
2. Create a new MySQL database
3. Get the connection details
4. Set `DATABASE_URL` in Vercel environment variables

## Environment Variables for Vercel

Add these in Vercel Project Settings > Environment Variables:

- `DATABASE_URL` - Your MySQL connection string
- `OPENAI_API_KEY` - Your OpenAI API key
- `GEMINI_API_KEY` - Your Gemini API key
- `SECRET_KEY` - Random string for Flask sessions
- `LLM_PROVIDER` - "gemini" or "openai"

## Migration from SQLite

If you have existing SQLite data, you'll need to migrate it manually or start fresh with MySQL.