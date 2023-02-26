"""
WSGI config for recipe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
python_home='/home/ubuntu/Recipe/recipeenv'
activate_this= python_home + '/bin/activate_this.py'
with open(activate_this)as f:
    code=compile(f.read(),activate_this,'exec')
    exec(code, dict(__file__=activate_this))

import os
import sys
sys.path.append('/home/ubuntu/Recipe')
sys.path.append('/home/ubuntu/Recipe/recipe')
sys.path.append('/home/ubuntu/Recipe/recipe_app')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe.settings')

application = get_wsgi_application()
