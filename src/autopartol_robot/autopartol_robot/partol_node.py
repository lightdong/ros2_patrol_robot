# 开始吟唱
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped,Pose
from nav2_simple_commander.robot_navigator import BasicNavigator,TaskResult

from tf2_ros import TransformListener, Buffer # 坐标监听器
from tf_transformations import euler_from_quaternion,quaternion_from_euler# 四元数转欧拉角函数
import math # 角度转弧度函数


# 继承BasicNavigator的原因是，BasicNavigator本身也是继承自Node，这样的话PartolNode的功能更多
# 继承BasicNavigator 就可以使用BasicNavigator中封装好的方法
class PartolNode(BasicNavigator):
    def __init__(self,node_name='partol_node'):
        super().__init__(node_name)
        # 声明相关参数
        self.declare_parameter('initila_point',[0.0,0.0,0.0])
        self.declare_parameter('target_points',[0.0,0.0,0.0,1.0,1.0,1.57])
        # 最后加一个下划线 表示这是类里面的一个变量
        # 把初始化点 与 目标点集合 提取成参数 可以使用文件来表示
        self.initial_point_ = self.get_parameter('initila_point').value
        self.target_points_ = self.get_parameter('target_points').value
        # Buffer来存储监听者 监听到的机器人坐标
        self.buffer_ = Buffer()
        self.listener_ = TransformListener(self.buffer_, self)
    
    def get_pose_by_xyyaw(self,x,y,yaw):
        """
        return PoseStamped对象
        通过参数值合成一个 PoseStamped对象
        """
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.pose.position.x = x
        pose.pose.position.y = y
        
        # 返回顺序是 xyzw
        quat = quaternion_from_euler(0, 0, yaw)
        pose.pose.orientation.x = quat[0]
        pose.pose.orientation.y = quat[1]
        pose.pose.orientation.z = quat[2]
        pose.pose.orientation.w = quat[3]

        return pose

    def init_robot_pose(self):
        """
        初始化机器人位姿
        """
        self.initial_point_ = self.get_parameter('initila_point').value
        init_pose = self.get_pose_by_xyyaw(self.initial_point_[0],self.initial_point_[1],self.initial_point_[2])

        # 设置初始位姿
        self.setInitialPose(init_pose)
        self.waitUntilNav2Active() # 等待导航可用
        
    def get_target_points(self):
        """
        通过参数值获取目标点的集合
        """
        points = []
        self.target_points_ = self.get_parameter('target_points').value
        for index in range(int(len(self.target_points_)/3)):
            x = self.target_points_[index*3]
            y = self.target_points_[index*3+1]
            yaw = self.target_points_[index*3+2]
            points.append([x,y,yaw])
            # 打印一下看一下获取到的目标点
            self.get_logger().info(f"获取到的目标点{index}->{x},{y},{yaw}")
        return points

    def nav_to_pose(self,target_point):
        """
        导航到目标点
        """
        self.goToPose(target_point) # 直接使用库函数发送goal点
        # 打印导航过程中的信息
        while not self.isTaskComplete():
            feedback = self.getFeedback()
            if feedback is not Node:
                self.get_logger().info(f'剩余距离:{feedback.distance_remaining}')
        result = self.getResult()
        self.get_logger().info(f'导航结果: {result}')

    
    def get_current_pose(self):
        """
        获取机器人当前的位姿
        """
        # 可以直接使用TF
        while rclpy.ok():
            try:
                result = self.buffer_.lookup_transform("map", "base_footprint", 
                                                       rclpy.time.Time(seconds=0), 
                                                       rclpy.time.Duration(seconds=1))
                transform = result.transform
                self.get_logger().info(f"平移:{transform.translation}")
                return transform
            except Exception as e:
                self.get_logger().warn(f"不能够获取坐标变换，原因: {str(e)}")

def main():

    # 初始化
    rclpy.init()
    # 创建一个巡航相关的节点
    patrol = PartolNode() # 节点

    # 为了得到yaml文件 先spin一下
    # rclpy.spin(patrol)

    # 1. 初始化机器人位姿
    patrol.init_robot_pose()

    while rclpy.ok():
        # 2. 获取目标点集合
        target_points = patrol.get_target_points()

        # 3. 导航到目标点
        # 循环遍历这些点
        for point in target_points:
            x,y,yaw = point[0],point[1],point[2]
            target_pose = patrol.get_pose_by_xyyaw(x,y,yaw)
            patrol.nav_to_pose(target_pose)

    # 不需要下面的两个是因为BasicNavigator有很多spin
    # rclpy.spin(nav)
    rclpy.shutdown()