python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pipenv
pipenv shell
pipenv install -r requirement.txt
uvicorn main:app --reload

//in case of errors , upgrade your dependencies to latest version:
pip install --upgrade motor
