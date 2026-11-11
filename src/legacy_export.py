"""Old-style export helper — intentionally written in a dated style.

Good "Legacy Modernization" demo target: ask Copilot to convert this to
f-strings, pathlib, and type hints.
"""

import os


def export_summary(tasks, out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    path = os.path.join(out_dir, "summary.txt")
    f = open(path, "w")
    total = len(tasks)
    done = 0
    for t in tasks:
        if t["completed"]:
            done += 1
    f.write("Total tasks: %d\n" % total)
    f.write("Completed: %d\n" % done)
    f.write("Pending: %d\n" % (total - done))
    f.close()
    return path
