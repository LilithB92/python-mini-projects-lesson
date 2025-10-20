import os
from datetime import datetime
from functools import wraps
from typing import Any
from typing import Callable
from typing import Union


def log(filename: Union[str | None] = None) -> Callable[..., Any]:
    """
    Декоратор может логировать работу функции и ее результат как в файл, так и в консоль.

    :param filename: Название файла, где регистрирует детали выполнения функций
    :return:  написание логи (в файл или в консоль) и результат функции(если функция не выдает ошибки)
    """

    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_message = ""
            try:
                result = func(*args, **kwargs)
                func_message += f"{func.__name__} ok"
                return result
            except Exception as e:
                exception_type = type(e).__name__
                func_message += f"{func.__name__} error: {exception_type}. Inputs: {args}, {kwargs}"
            finally:
                if filename:
                    directory_name = os.path.split(os.getcwd())[0]
                    log_dir = os.path.join(directory_name, "data")
                    if not os.path.exists(log_dir):
                        os.makedirs(log_dir)
                    log_file = os.path.join(log_dir, filename + ".txt")
                    with open(log_file, "w") as file:
                        file.write(f"{current_date} {func_message}\n")
                else:
                    print(func_message)

        return inner

    return wrapper
