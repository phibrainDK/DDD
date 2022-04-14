# DDD

## Initial steps

For `Windows`:
    - First at all, be sure to `uninstall` python from your PC
    - Install `choco` via powershell using admin mode typing 
    ```bash 
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) 
    ```
    - Then install `pyenv` via choco using
    ```bash
    install pyenv-win
    ```
    - Then upgrade `pyenv` via choco using
    ```bash
    choco upgrade pyenv-win
    ```
    - Open the repository path and then install python 3.8.9 doing
    ```bash
    pyenv install 3.8.9
    ```
    - Set python version doing
    ```bash
    pyenv local 3.8.9
    ```
    - Sanity check: check the python version set on your path
    ```bash
    python --version
    ```
    - Create a virtual enviromments doing
    ```bash
    python -m venv .venv
    ```
    - To activate the virtual enviromment going to `Scripts` file doing
    ```bash
    cd .venv/Scripts
    ```
    - Then type `activate`
    ```bash
    activate
    ```
    - Go back to the current path
    ```bash
    cd ..
    cd ..
    ```
    - Then install pip-tools doing
    ```bash
    python -m pip install pip-tools
    ```
    - Then setup-tools
    ```bash
    pip install --no-cache-dir -U pip setuptools wheel
    ```
    - Then install requirements
    ```bash
    pip install -r pip/with-dep-requirements.txt
    ```
    - Extra: Using pip-compile to generate exact requirements using as base `pip/no-dep-requirement.in`
    ```bash
    pip-compile pip/no-dep-requirements.in --output-file=pip/with-dep-requirements.txt
    ```


