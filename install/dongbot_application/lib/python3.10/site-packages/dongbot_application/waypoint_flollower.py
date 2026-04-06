from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy

def main():

    # 初始化
    rclpy.init()
    nav = BasicNavigator() # 节点
    nav.waitUntilNav2Active() # 等待导航可用

    # 设置初始位姿
    goal_poses = []

    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = nav.get_clock().now().to_msg()
    goal_pose.pose.position.x = 2.0
    goal_pose.pose.position.y = 1.0
    goal_pose.pose.orientation.w = 1.0
    goal_poses.append(goal_pose)

    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = nav.get_clock().now().to_msg()
    goal_pose1.pose.position.x = -2.0
    goal_pose1.pose.position.y = -1.0
    goal_pose1.pose.orientation.w = 1.0
    goal_poses.append(goal_pose1)

    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = nav.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 0.0
    goal_pose2.pose.position.y = 0.0
    goal_pose2.pose.orientation.w = 1.0
    goal_poses.append(goal_pose2)

    nav.followWaypoints(goal_poses) # 直接使用库函数发送goal点
    # 打印导航过程中的信息
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        nav.get_logger().info('导航中...')
        nav.get_logger().info(f'结点编号:{feedback.current_waypoint}')

    result = nav.getResult()
    nav.get_logger().info(f'导航结果:{result}')

    # 运行
    # rclpy.spin(nav)
    # rclpy.shutdown()