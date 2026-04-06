from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy

def main():

    # 初始化
    rclpy.init()
    nav = BasicNavigator() # 节点

    # 设置初始位姿
    init_pose = PoseStamped()
    init_pose.header.frame_id = 'map'
    init_pose.header.stamp = nav.get_clock().now().to_msg()
    init_pose.pose.position.x = 0.0
    init_pose.pose.position.y = 0.0
    init_pose.pose.orientation.w = 1.0

    # 设置初始位姿
    nav.setInitialPose(init_pose)
    nav.waitUntilNav2Active() # 等待导航可用

    # 运行
    rclpy.spin(nav)
    rclpy.shutdown()