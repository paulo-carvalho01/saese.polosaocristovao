from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
scripts = root / 'scripts'

for script in ('import_applications.py', 'build_page.py'):
	subprocess.run([sys.executable, str(scripts / script)], cwd=root, check=True)
