# isaac_ros_navigation_goal

This is a ROS2 package which can be used to set goal pose for the robot. Tested with [Isaac sim ros2 nav example](https://isaac.gitlab-master-pages.nvidia.com/omni_isaac_sim/app_isaacsim/app_isaacsim/tutorial_ros2_navigation.html)


The package will stop processing(setting goals) once any one of the below condition is met:
1. Number of goals published till now >= iteration_count.
2. If GoalReader is being used then if all the goals from file are published, or if condition (1) is true.
3. A goal is rejected by the action server.
4. In case of RandomGoalGenerator if a goal was not generated even after exhausing all the allowed trials, which is rare but could happen in very dense maps.

## Steps to use:
1. Clone the repo to your ros2 workspace.
2. Make the changes in the launch file present in isaac_ros_navigation_goal/launch

| Option | description |
| :---: | :-- |
| map_yaml_path | Required if RandomGoalGenerator is being used. This is the path to the yaml file which has meta of the map generated via isaac sim. Please provide the absolute path of the yaml file. Example yaml file is present at: isaac_ros_navigation_goal/assets/carter_warehouse_navigation.yaml. The map image is being used to identify the obstacles in the vicinity of a generated pose. |
| iteration_count | No of times goal is to be set |
| goal_generator_type | type of the goal generator(RandomGoalGenerator/GoalReader available for now) |
| action_server_name | name of the action server |
| obstacle_search_distance_in_meters | distance in meters in which there should not be any obstacle of a generated pose |
| goal_text_file_path | Required if GoalReader is being used. This is the path to the text file which has static goals. Each line has a single goal in `pose.x pose.y orientation.x orientation.y orientation.z orientation.w` format. Please provide the absolute path of the file. Sample file is present at: isaac_ros_navigation_goal/assets/goals.txt |
| frame_id | value for the frame_id of header | 
| initial_pose | If initial_pose is set, it will be published to `/initialpose` topic and goal poses will be sent to action server after that. Format is `[pose.x, pose.y, pose.z, orientation.x, orientation.y, orientation.z, orientation.w]` |

3. Build and source the package using: `colcon build --packages-select isaac_ros_navigation_goal && source install/setup.bash`
4. Launch the launch file using: `ros2 launch isaac_ros_navigation_goal isaac_ros_navigation_goal.launch.py`
