from database.container import Container


class Table:
    def __init__(self, entities: Container) -> None:
        self.entities = entities

    def save_all(self) -> None:
        for entity in self.entities:
            entity.put()
