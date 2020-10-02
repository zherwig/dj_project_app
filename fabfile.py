# pylint: disable=import-error,unused-import,import-outside-toplevel,wildcard-import,unused-wildcard-import,wrong-import-position,useless-suppression,unused-argument
import sys
import os
from fabric.api import sudo, lcd, task, local, run, settings, env, execute  # noqa


# --------------------------------------
# Add Library Paths
# --------------------------------------

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
SYSADMIN_PATH = os.path.abspath(os.path.join(PROJECT_PATH, 'repo_libs', 'sysadmin'))

if SYSADMIN_PATH not in sys.path:
    sys.path.insert(1, SYSADMIN_PATH)


# --------------------------------------
# Import Fabric Modules
# --------------------------------------

from sysadmin.fabric import *


# --------------------------------------
# Deployment
# --------------------------------------

from sysadmin.fabric.deploy import set_deployment_settings, \
    WebfactionDeploymentSettings, WebAirDeploymentSettings
from sysadmin.fabric.modules import psql


class HSTalksWebfactionDeploymentSettings(WebfactionDeploymentSettings):
    hosts = ['hstalks@webfaction.hstalks.com']
    project_name = 'dj_project_app'
    django_webapp_name = 'pm_django'
    static_webapp_name = 'pm_django_static'
    src_dirs = [PROJECT_PATH]

    # def pre_process(self, deployment_settings, *args, **kwargs):
    #     local('npm run build')


@task
def prod():
    set_deployment_settings(HSTalksWebfactionDeploymentSettings)