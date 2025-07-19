import rclpy
from rclpy.node import Node
from interbotix_xs_msgs.msg import JointGroupCommand

class rx200gohome(Node):
    def __init__(self):
        super().__init__('rx200_go_home')
        self.publisher1 = self.create_publisher(
            JointGroupCommand,
            '/arm_1/commands/joint_group',
            10
        )
        self.publisher2 = self.create_publisher(
            JointGroupCommand,
            '/arm_2/commands/joint_group',
            10
        )
        cmd1 = JointGroupCommand()
        cmd1.name = "arm"
        cmd1.cmd = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.publisher1.publish(cmd1)
        cmd2=JointGroupCommand()
        cmd2.name="arm"
        cmd2.cmd=[0.0, 0.0, 0.0, 0.0, 0.0]
        self.publisher2.publish(cmd2)
        print("arm_1 and arm_2 sent to home pose")

def main(args=None):
    rclpy.init(args=args)
    node = rx200gohome()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
