## **Setup**

It is recommended to install [Pyenv](https://github.com/pyenv-win/pyenv-win) to manage Python versions.

To install version 3.12.2 required for the project, if using Pyenv, run `pyenv install 3.12.2` in the terminal. To set the project folder to use the correct version, use `pyenv local 3.12.2`.

We also use the `virtualenv` library to create a virtual environment for the project, ensuring dependencies do not mix with the global Python environment. Additionally, we use the `pre-commit` library to standardize code across all contributors before committing.

```powershell
# Install virtual environment library
> python -m pip install virtualenv
# Create virtual environment
> virtualenv .venv
# Activate virtual environment
> .venv\Scripts\activate
# Install pip-tools
(.venv) > python -m pip install pip-tools
# Generate requirements.txt
(.venv) > python -m piptools compile --upgrade
# Install dependencies
(.venv) > python -m piptools sync
# Install pre-commit (code standards)
(.venv) > pre-commit install
```

For simplicity, all together:

```powershell
python -m pip install virtualenv ; python -m virtualenv .venv ; .venv\Scripts\activate ; python -m pip install pip-tools ; python -m piptools compile --upgrade ; python -m piptools sync ; pre-commit install
```

---

## **Requirements**

Whenever installing a new dependency, add it to `requirements.in` and then run:

```bash
# Activate virtual environment
> .venv\Scripts\activate
# Generate requirements.txt
(.venv) > python -m piptools compile --upgrade
# Install dependencies
(.venv) > python -m piptools sync
```

For simplicity, all together:

```powershell
.venv\Scripts\activate ; python -m piptools compile --upgrade ; python -m piptools sync
```

This will generate a new `requirements.txt` file with the new/updated dependency and install it in the virtual environment.

---

## **Preparing to Run Code**

Always activate the virtual environment before running any code:

```powershell
.venv\Scripts\activate
```

Then proceed to run the code normally with Python.

```powershell
(.venv) > python main.py
```

---

## **Pre-commit**

To check if changed files follows the code standards using pre-commit, run:

```powershell
(.venv) > pre-commit run --all-files
```

---

## **Notes**

To deactivate the virtual environment, use `deactivate`.

```powershell
(.venv) >            # Active
(.venv) > deactivate # Deactivation command
>                    # Not active
```

Another important point is to ensure the virtual environment is activated before running requirement commands. If not activated, it may uninstall/update dependencies in your global environment, which can cause issues.
