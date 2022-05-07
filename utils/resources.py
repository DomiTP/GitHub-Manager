import os
from pathlib import Path

USER_HOME_PATH = Path.home()
PROJECT_FOLDER = os.path.dirname(os.path.dirname(__file__))
RESOURCES_FOLDER = os.path.join(PROJECT_FOLDER, 'resources')
ICONS_FOLDER = os.path.join(RESOURCES_FOLDER, 'icons')


def get_icon(icon_name):
    icon = os.path.join(ICONS_FOLDER, icon_name)
    if not file_exists(icon):
        icon = False

    return icon


def file_exists(file):
    """
    Comprueba si un fichero existe
    :return: True si existe, False si no existe
    """
    return os.path.exists(file)


LOGO = get_icon("GitHub_Manager.png")
