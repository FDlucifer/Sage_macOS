import subprocess
import os
from dev_id import DEV_ID
entitlement_file = 'entitlement.plist'
framework_path = os.path.abspath('build/Sage.framework/Versions/Current')
extra_files = ['local/share/cmake-3.21/Modules/Internal/CPack/CPack.OSXScriptLauncher.in']

file_args = ['codesign', '-v', '-s', DEV_ID, '--timestamp', '--options', 'runtime', '--force',
                 '--entitlements', entitlement_file]
with open('files_to_sign') as infile:
    for path in infile.readlines():
        signee = path.strip()
        result = subprocess.run(file_args + [signee], capture_output=True)
        if result.returncode:
            print('Failed on %s'%path)
            print(result.stderr)

for path in extra_files:
    signee = os.path.join(framework_path, path)
    result = subprocess.run(file_args + [signee], capture_output=True)
    if result.returncode:
        print('Failed on %s'%path)
        print(result.stderr)
            
print('Signing framework ...')
subprocess.run(file_args + ['build/Sage.framework'])


