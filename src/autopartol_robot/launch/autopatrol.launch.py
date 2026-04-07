import launch
import launch_ros

from ament_index_python.packages import get_package_share_directory # 根据包 找到里面的share路径
import os


# 启动两个结点 一个是partol_node 另一个是speaker
# 在启动partol_node时需要传递参数配置文件partol_config.yaml
def generate_launch_description():
    # 添加环境变量 然后rviz2的界面就变大了
    env_var = launch.actions.SetEnvironmentVariable(
        'QT_FONT_DPI',
        '144'
    )

    # 获取默认的urdf文件路径   
    autopartol_robot_package_path = get_package_share_directory('autopartol_robot') # 先找到功能包中的share目录
    default_patrol_config_path =  os.path.join(autopartol_robot_package_path, 'config', 'partol_config.yaml')
    # patrol_node结点动作
    action_patrol_node = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='partol_node',
        parameters=[
            default_patrol_config_path
        ],
        output='screen',
    )

    action_speaker_node = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='speaker',
        output='screen',
    )


    # 返回值的类型也是固定的
    return launch.LaunchDescription([
        # action动作
        env_var, # 添加环境变量 调整rviz2的界面大小
        action_patrol_node, # 启动patrol_node结点
        action_speaker_node, # 启动speaker结点
    ])