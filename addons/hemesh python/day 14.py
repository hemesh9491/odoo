completed_tasks = 45
total_tasks = 50
attendence_day = 20
total_working_day = 22
total_leaves = 2
penalty_per_leave = 2
#calculate task percentage
task_percentage = (completed_tasks/total_tasks)*100
#calculate attendence percentage
attendence_percentage = (attendence_day/total_working_day)*100
#apply planty for excess leaves
leave_penalty = max(0,total_leaves-(total_working_day-attendence_day))*penalty_per_leave
#calculate overall percentage
overall_percentage = (task_percentage + attendence_percentage-leave_penalty)/2
#display result
print(f"Employee performance:task{task_percentage:.2f}%,attendence{attendence_percentage:.2f}%,leave penalty{leave_penalty:.2f}%,overall{overall_percentage:.2f}%")
