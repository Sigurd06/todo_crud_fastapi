import uvicorn

from app.core.settings import settings

if __name__ == '__main__':
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=settings.RELOAD, log_level="info", workers=1, use_colors=True)

