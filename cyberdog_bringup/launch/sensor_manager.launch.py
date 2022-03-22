# Copyright (c) 2021 Beijing Xiaomi Mobile Software Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# sensors/sensor_manager/launch/sensor_manager.launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    allow_sensor_abnormality_arg = DeclareLaunchArgument(
        'allow_sensor_abnormality', default_value='False'   # 是否允许传感器异常
    )

    sensor_manager_node = Node(
            package='sensor_manager',
            namespace='cyberdog',
            executable='sensor_manager',
            name='sensor_manager',
            output='screen',
            parameters=[{
                'allow_sensor_abnormality': LaunchConfiguration('allow_sensor_abnormality'),
            }]
        )

    return LaunchDescription([
        allow_sensor_abnormality_arg,
        sensor_manager_node,
    ])
