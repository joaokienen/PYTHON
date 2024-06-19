/ --------------------------------------------------------------------------------------------------------------------- /

- Projeto: NetskopeUseAPI
- Data de criação: 01/06/2024

---

# -----> Modo de uso:

---

# Windows

(Caso não exista diretório ./.venv)
1. Criar o Ambiente Virtual:

   python -m venv .venv


2. Ativar o Ambiente Virtual:
   - Se estiver usando o Prompt de Comando (cmd):

     .venv\Scripts\activate

   - Se estiver usando o PowerShell:

     .venv\Scripts\Activate.ps1

   - Se estiver usando o Git Bash ou WSL (Windows Subsystem for Linux):

     source .venv/Scripts/activate

---

# Linux

(Caso não exista diretório ./.venv)
1. Criar o Ambiente Virtual:

   python3 -m venv .venv


2. Ativar o Ambiente Virtual:

   source .venv/bin/activate

---

# -----> Exemplo de uso:

# Linux Server:

   1. cd /Scripts
   
   2. source .venv/bin/activate

   3. pip install -r requirements.txt

   4. python3 GET_Client-Data.py

   5. deactivate

/ --------------------------------------------------------------------------------------------------------------------- /
