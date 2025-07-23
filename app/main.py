import typer
import uvicorn
from app.models import User
from app.storage import add_user

cli = typer.Typer(help="CLI для управления FastAPI приложением")

@cli.command()
def runserver(host: str = "127.0.0.1", port: int = 8000):
    """Запуск FastAPI сервера"""
    typer.echo(f"http://{host}:{port}")
    uvicorn.run("app.api:app", host=host, port=port, reload=True)

@cli.command()
def create_user(id: int, name: str, age: int = typer.Option(0)):
    """Добавить пользователя через CLI"""
    user = User(id=id, name=name, age=age)
    add_user(user)
    typer.echo(f"Пользователь создан: {user.name} (ID: {user.id})")

if __name__ == "__main__":
    cli()
