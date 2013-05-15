from fabric.api import local,lcd
import os

#Add settings module so fab file can see it
os.environ['DJANGO_SETTINGS_MODULE'] = "dice_pool.settings"
from django.conf import settings


def prepare_deployment(branch_name):

	local('python manage.py test dice_pool')
	local('git add -p && git commit')


def setup():

	# set up the virtual environment
	if not os.path.exists('virt'):
		os.mkdir('virt');
		local('virtualenv ./virt')

	# update the local working directory
	local('git pull')

	# make sure all required libraries are present
	local('source virt/bin/activate && pip install -r requirements.txt')

	# make sure the suer databases are up to date
	for app in list(settings.INSTALLED_APPS)[7:]:
		local('python manage.py migrate '+app)
