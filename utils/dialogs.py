from PySide6.QtWidgets import QMessageBox


def delete_repository_dialog(source):
    """
    Dialog to confirm deletion of a repository.
    :param source: remote if remote repository, local if local repository
    :return:  True if user confirms deletion, False otherwise
    """
    res = False
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    if source == 'local':
        msg.setText("You are about to delete the repository from the disk, this action cannot be undone.")
    elif source == 'remote':
        msg.setText("You are about to delete the repository from GitHub, this action cannot be undone.")
    msg.setInformativeText("Are you sure you want to continue?")
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    response = msg.exec()
    if response == QMessageBox.Yes:
        double_check = QMessageBox()
        double_check.setIcon(QMessageBox.Warning)
        double_check.setText("Are you really sure you want to continue?")
        double_check.setInformativeText("This action cannot be undone.")
        double_check.setWindowTitle("Warning")
        double_check.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        response2 = double_check.exec()
        if response2 == QMessageBox.Yes:
            res = True
    return res


def message(type_, message, additional_info=None):
    """
    Show a message box with the given type and message.
    :param type_:  Type of the message box.
    :param message:  Message to show.
    :param additional_info:  Additional information to show.
    :return:  True if the user clicked the Yes button, False if the user clicked the No button,
    or None if the user clicked the OK button.
    """
    messagebox = QMessageBox()
    if type_ == 'error':
        messagebox.setIcon(QMessageBox.Critical)
        messagebox.setWindowTitle('Error')
        messagebox.setStandardButtons(QMessageBox.Ok)
    elif type_ == 'warning':
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setWindowTitle('Warning')
        messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    elif type_ == 'success':
        messagebox.setIcon(QMessageBox.Information)
        messagebox.setWindowTitle('Success')
        messagebox.setStandardButtons(QMessageBox.Ok)

    messagebox.setText(message)
    if additional_info:
        messagebox.setDetailedText(additional_info)

    result = messagebox.exec()
    if result == QMessageBox.Yes:
        ret = True
    elif result == QMessageBox.No:
        ret = False
    else:
        ret = None

    return ret
