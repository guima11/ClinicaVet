# ClinicaVet

Sistema de gerenciamento para clínica veterinária desenvolvido em Django.

---

## Pré-requisitos

- Python 3.11+
- PostgreSQL
- Git
- Ambiente virtual (venv)

---

## Preparação do ambiente

### 1. Clonar o repositório

```
git clone https://github.com/guima11/ClinicaVet.git
cd ClinicaVet/clinica_vet
```


### 2. Criar e ativar ambiente virtual

#### Linux/Mac
```
python3 -m venv venv
source venv/bin/activate
```

#### Windows(cmd)
```
python -m venv venv
.\venv\Scripts\activate.bat
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Configurar banco de dados PostgreSQL
Instale e configure o PostgreSQL.

Crie um banco de dados (exemplo: clinica_db) e um usuário com permissões.

Atualize o arquivo clinica_vet/settings.py com as credenciais do banco:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clinica_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Executar migrações

```
python manage.py migrate
```

### 6. Criar superusuário para acessar o admin
```
python manage.py createsuperuser
```

### 7. Rodar o servidor de desenvolvimento
```
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/api/vets
http://127.0.0.1:8000/api/tutores
http://127.0.0.1:8000/api/cadastros
```

Cadastre em cada link ao menos um dado.

### 8. Adminstre os dados

Logue com o usuário superadmin em: 
```
http://127.0.0.1:8000/admin/
```

Faça a adminstração dos seus dados da forma que de desejar.
