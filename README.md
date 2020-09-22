# Labs Vladimir lila

### Зависимости

- Python3.8+
- Make

# Запуск

Для проверки работы, можно запустить тесты, установив на локальный компьютер необходимую утилиту pytest

Сделать это можно с помощью Makefile командой

```bash
make deps
```

Это создаст виртуальное окружение, и установит в него pytest

После чего, прогнать тесты можно командой

```bash
make test
```

или вручную активирова venv с помощью команды

```bash
pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate
```

Запустить тесты командой

```bash
pytest
```


