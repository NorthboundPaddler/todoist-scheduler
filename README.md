# ✅Todoist-Scheduler🕝
A simple, fast, no-frills web interface to easily drag and drop a filtered list of tasks onto the day you want to do them.  

I'm a user of Carl Pullein's ["Time Sector System"](https://youtu.be/XRl3zkWAKvU) and the weekly review/scheduling of my upcoming tasks is tedious in the current Todoist interface. It lacks a good overview of each day's workload. This project aim's to help make that weekly review/scheduling as quick and painless as possible.

## Goals
- No explanation needed (simple)
- Easy to self-host
- Speed up weekly task reviews

## Front-End Design
- Kanban-board style interface for 5/7 days of the week
- Calendar view with condensed task count
- Sidebar with filter input box and resulting tasks in list below
  - Filter validator icon (either on-click button or on-change input)
- Settings page to enter API key and general appearance settings

## Components
- Flask (Python) back-end
- Bootstrap or mini.css 
- jQuery for client-side logic

## Tasks
- [] Server-side "get tasks by filter", "edit task", "validate filter"
- [] Front-end interface structure (week view, month view, settings page)
- [] Front-end interactive components (i.e. drag and drop)
- [] Client-side filter/token storage handler
- [] Error handling/feedback 


## General thoughts
- Would it be more private to do all logic client-side to negate sending personal data back to a server? This would only be relevant if there was a commercial hoster of this project. 
- I don't think I want to even add things like task editing or task deletion - just more features that I need to maintain that stray from the core goal (scheduling existing tasks). 
- Todoist's filter input does not suggest existing labels/projects... so why should this? 
