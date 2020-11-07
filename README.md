# Automate House

Prototipo de uma casa automatizada

## Como rodar

### Criar venv

`Linux/MacOS`
```shell
python3 -m venv venv
```

`Windows`
```shell
python -m venv venv
```

### Ativar venv

`Linux/MacOS`
```shell
source tutorial-env/bin/activate
```

`Windows`
```
tutorial-env\Scripts\activate.bat
```

### Install requirements

```shell
pip install -r requirements.txt
```

### Copiar copiar conf.sample e alterar conf

`cp conf.sample conf`

Faça alterações necessárias no arquivo conf, adicione suas chaves


---

`python pub_geladeira.py`

`python sub_geladeira.py`