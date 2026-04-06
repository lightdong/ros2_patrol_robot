import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vim3/myros/12-navigation/navigation_ws/install/autopartol_robot'
