import filecmp

def detect_drift(baseline, current):
    if filecmp.cmp(baseline, current):
        print("Configuration matches baseline.")
    else:
        print("Drift detected!")

detect_drift("/etc/config-baseline.cfg", "/etc/current-config.cfg")
