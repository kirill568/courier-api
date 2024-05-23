from fastapi import FastAPI

from app.container import Container


class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI()

        # set db and container
        self.container = Container()
        self.db = self.container.db()

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container