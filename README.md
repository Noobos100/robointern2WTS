# robointern2WTS

A simple program written in Python that allows you to convert an array of tasks from RoboIntern to an array of tasks for the Windows Task Scheduler.

## How it works

Launch robointern2wts in python shell
Call the copyxml function with:
- the WTS file (single task) as a template for the first argument
- the RoboIntern configfile (taskarray) as the second argument

For now, this program translates the task if it is a "execute program" task. It copies
- task name
- taks command file path
- task exec time (time only, no data/repetition...)

Not actually guaranteed to work.