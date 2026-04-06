from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy

def main():

    # 初始化
    rclpy.init()
    nav = BasicNavigator() # 节点

    # 设置初始位姿
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = nav.get_clock().now().to_msg()
    goal_pose.pose.position.x = -2.0
    goal_pose.pose.position.y = -1.0
    goal_pose.pose.orientation.w = 1.0

    nav.goToPose(goal_pose) # 直接使用库函数发送goal点
    # 打印导航过程中的信息
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        nav.get_logger().info('导航中...')
        nav.get_logger().info('导航进度: {:.2f}'.format(feedback.percent_remaining))


    result = nav.getResult()
    nav.get_logger().info(result.__str__())

    # 设置初始位姿
    nav.setInitialPose(goal_pose)
    nav.waitUntilNav2Active() # 等待导航可用

    # 运行
    # rclpy.spin(nav)
    # rclpy.shutdown()