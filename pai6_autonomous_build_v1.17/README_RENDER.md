# pai6 v1.17 — Render Edition

## Quick Deploy on Render (Free)
1) Push this folder to a GitHub repo.
2) In Render: New → Web Service → connect repo.
3) Set:
   - Build Command:
     ```
     pip install -r requirements.txt
     ```
   - Start Command:
     ```
     uvicorn backend.app:app --host 0.0.0.0 --port 10000
     ```
   - Environment: Python 3
   - PORT env (optional): 10000
4) Deploy. Open the link → you should see the frontend.
- Health: `/health`
- Demo API: POST `/api/echo`

## Notes
- Frontend is served statically from `/frontend` via FastAPI StaticFiles.
- No Procfile needed on Render; set Start Command in dashboard.
