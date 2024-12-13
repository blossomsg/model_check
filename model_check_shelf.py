# For Windows
import sys

sys.path.append("<provide_file_path>\\model_check\\")
import main_widget

if __name__ == "__main__":
    ui = main_widget.UiCheckWidget()
    ui.show()
