
from ui import hello_ui
from inventory import hello_inventory
from db import hello_db


def hello_main() -> str:
    return "hello main"

print(hello_main())
print(hello_db())
print(hello_inventory())
print(hello_ui())