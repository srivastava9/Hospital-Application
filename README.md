# Hospital-Application
A Web App to manage appointment of Doctor in Hospital

## Setup

### Python Environment
```sh
VENV_PATH=~/envs/venv
virtualenv -p python3 $VENV_PATH
source $VENV_PATH/bin/activate

pip install -r hospital-application/requirements.txt

# for vscode
cat >> .env << EOF
PYTHONPATH=identity
EOF
```
#### Create a .env file and copy paste
```sh
ENVIRONMENT=LOCAL
DJANGO_SECRET_KEY='django-insecure-f8nn5m3kfs!swtsrvhn3tsati4_5p!!u8uu_muql0mju7&(m-@'
EOF
```

