import launch
import launch_ros

from ament_index_python.packages import get_package_share_directory # 根据包 找到里面的share路径
import os


def generate_launch_description():
    # 添加环境变量 然后rviz2的界面就变大了
    env_var = launch.actions.SetEnvironmentVariable(
        'QT_FONT_DPI',
        '144'
    )

    # 获取默认的urdf文件路径   
    urdf_package_path = get_package_share_directory('dongbot_description') # 先找到功能包中的share目录
    # default_urdf_path =  os.path.join(urdf_package_path, 'urdf', 'first_robot.urdf')
    default_urdf_path =  os.path.join(urdf_package_path, 'urdf', 'dongbot.urdf')
    default_rsiv_path = os.path.join(urdf_package_path, 'config', 'dongbot_config.rviz')

    # 声明一个urdf目录的参数，方便修改
    action_declare_arg_mode_path = launch.actions.DeclareLaunchArgument(
        name='model',
        default_value=str(default_urdf_path),
        description='加载的模型文件路径'
    )

    # 得到robot_state_publisher的参数值对象
    substitutions_command_result = launch.substitutions.Command([
        'cat ', launch.substitutions.LaunchConfiguration('model') 
    ])

    # substitutions_command_result = launch.substitutions.Command([
    #     'xacro ', launch.substitutions.LaunchConfiguration('model') 
    # ])


    
    # 转换为launch的参数值对象 因为robot_state_publisher的参数内容 不是文件路径而是文件的内容
    robot_description_value = launch_ros.parameter_descriptions.ParameterValue(
        substitutions_command_result,
        value_type=str
    )


    # 启动robot_state_publisher结点 得到数据后 向Rviz发送检测到的机器人约束关系
    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher', #功能包 与 里面的可执行文件一个名称
        executable='robot_state_publisher',
        parameters=[
            {
                'robot_description':robot_description_value # parameters将数据传递给结点的参数
            }
        ]
    )


    # 启动joint_state_publisher结点 检测URDF文件中的关节关系 并向Rviz发送关系数据
    action_joint_state_publisher = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )


    # 启动rviz结点 显示机器人模型
    action_rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=[ # 命令行后面加东西
            '-d', default_rsiv_path
        ]
    )

    # 返回值的类型也是固定的
    return launch.LaunchDescription([
        # action动作
        env_var, # 添加环境变量 调整rviz2的界面大小
        action_declare_arg_mode_path, # 声明参数

        action_robot_state_publisher, # 把urdf中的信息发送到Rviz
        action_joint_state_publisher, # 配合上面解析urdf文件
        action_rviz_node # 启动rviz结点
    ])