# robointern2WTS

A simple program written in Python that allows you to convert an array of tasks from RoboIntern to an array of tasks for the Windows Task Scheduler.

## How it works

Launch robointern2wts in python shell and call the robointern2wts function with:
- the WTS file (single task) as a template for the first argument
- the RoboIntern configfile (taskarray) as the second argument

For now, this program translates the task if it is a "execute program" task. It copies
- task name
- taks command file path
- task exec time (time only, no date/repetition...)

Not actually guaranteed to work.

WTS tasks are in C:\Windows\System32\Tasks
