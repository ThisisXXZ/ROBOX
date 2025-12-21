#!/usr/bin/env python
"""
Check if at least 5 different robox_90 tasks have successful trajectories.
Output: YES or NO
"""

import json
import os
import sys


def is_robox_90_task(task_data):
    """Check if task belongs to robox_90 dataset by examining the bddl_file path."""
    bddl_file = task_data.get("bddl_file", "")
    # Normalize path separators
    bddl_file = bddl_file.replace("\\", "/")
    return "robox_90" in bddl_file


def main():
    log_file = "demonstration_data/collection_log.json"
    
    if not os.path.exists(log_file):
        print("NO")
        return 1
    
    with open(log_file, 'r') as f:
        log_data = json.load(f)
    
    # Count robox_90 tasks with successful trajectories
    successful_robox_90_tasks = [
        task for task, data in log_data.items()
        if is_robox_90_task(data) and data.get("successful", 0) > 0
    ]
    
    if len(successful_robox_90_tasks) >= 1:
        print("YES")
        return 0
    else:
        print("NO")
        return 1


if __name__ == "__main__":
    sys.exit(main())
