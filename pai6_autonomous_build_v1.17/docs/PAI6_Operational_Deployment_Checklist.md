# PAI6 Operational Deployment Checklist

Generated: 2025-10-25T21:27:57.607219Z

- Render Web Service: Python + Uvicorn
- Build: `pip install -r requirements.txt`
- Start: `uvicorn backend.app:app --host 0.0.0.0 --port 10000`
- Health: `/health`
