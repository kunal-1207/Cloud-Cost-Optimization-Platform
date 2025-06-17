import subprocess

def remediate(recommendations):
    for r in recommendations:
        if r['action'] == 'shutdown':
            subprocess.run(["terraform", "apply", "-auto-approve"], cwd="./iac")
