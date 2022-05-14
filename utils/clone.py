import os
import shutil

import pygit2
from PySide6.QtWidgets import QMessageBox


def check_save_path(save_path):
    """
    Check if the save path is correct, and you have the necessary permissions
    :return: True if the path is correct, and you have the necessary permissions or False if not and the reason
    """

    check = False
    msg_err = ""
    if os.path.exists(save_path):
        if os.path.isdir(save_path):
            if os.access(save_path, os.R_OK | os.W_OK):
                check = True
            else:
                msg_err = "No tienes permisos en el directorio"
        else:
            msg_err = "La ruta especificada no es un directorio"
    else:
        msg_err = "La ruta especificada no existe"
    return check, msg_err


def check_if_repo_exists(repo_path):
    """
    Check if the repository exists
    :param repo_path: Path to the repository
    :return: True if the repository exists, False if not
    """
    response = False
    if os.path.exists(repo_path):
        response = True
    return response


def clone(clone_url, clone_path, user):
    """
    Clone the repository to the specified path
    :param clone_url:  URL of the repository
    :param clone_path:  Path to save the repository
    :param user:  User info to obtain the pygit callback to clone private repositories
    :return:
    """
    res = True, ""
    repo_name = clone_url.split('.git')[0].split('/')[-1]
    full_path = os.path.join(clone_path, repo_name)
    check1 = check_save_path(clone_path)
    check2 = check_if_repo_exists(full_path)
    if check1[0]:
        if check2:
            message_box = QMessageBox()
            message_box.setText("A folder with the same name as the repository already exists in the directory")
            message_box.setInformativeText("Do you want to overwrite it?")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            message_box.setDefaultButton(QMessageBox.No)
            response = message_box.exec_()
            if response == QMessageBox.Yes:
                try:
                    shutil.rmtree(full_path, ignore_errors=True)
                    pygit2.clone_repository(clone_url, full_path, callbacks=user.pygit_callback)
                except Exception:
                    res = False, "Failed to clone repository " + repo_name
            else:
                res = False, "A folder with the same name as the repository already exists in the directory"
        else:
            try:
                pygit2.clone_repository(clone_url, full_path, callbacks=user.pygit_callback)
            except Exception as e:
                res = False, "Failed to clone repository " + repo_name
    return res
