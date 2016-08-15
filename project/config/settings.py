import os

db_url = os.environ.get('DATABASE_URL', 'postgres://vagrant:dbpass@localhost:5432/djornado_tpl_db')

secret_key = os.environ.get('SECRET_KEY', 'Secure_SeCrEtKEY')

port = os.environ.get('PORT', 8000)

debug = os.environ.get('DEBUG', True)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

static_path = os.environ.get('STATIC_PATH', os.path.join(base_dir, 'static'))

template_path = os.path.join(base_dir, 'templates')
