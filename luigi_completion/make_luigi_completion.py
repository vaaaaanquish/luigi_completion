import re
import sys
import os
import subprocess


def default_arg():
    return {
        '--local-scheduler', '--pidfile', '--background', '--logdir', '--state-path', '--unix-socket', '--help-all', '--help', '--assistant', '--module',
        '--log-level', '--logging-conf-file', '--workers', '--parallel-scheduling', '--parallel-scheduling-processes', '--take-lock', '--lock-pid-dir',
        '--no-lock', '--lock-size', '--scheduler-url', '--scheduler-port', '--scheduler-host', '--use-cmdline-section', '--worker-force-multiprocessin',
        '--rerun'
    }


def _get_params(x):
    parameter_set = set()
    parameter_set.add(x[0].strip())
    if len(x) == 2:
        s = x[1].lower().replace('._', '.').lstrip('_').split('.')
        a = x[0].replace('.-', '.').replace('---', '--').replace('.'.join(s[:-1]).replace('_', '-') + '.', '').lower().replace(s[-1].split('_')[0] + '-', '')
        parameter_set.add(a.strip())
    return parameter_set


def _get_modules(x):
    module_set = set()
    if len(x) == 2 and '.' in x[0] and not x[0].startswith('---'):
        x = x[0].lstrip('--')
        x = x.split('.')
        x[-1] = x[-1].split('-')[0]
        if x[-1]:
            module_set.add('.'.join(x))
    return module_set


def _parse_help_all(t):
    parameter_set = default_arg()
    module_set = set()
    for x in re.findall(r'\[\-\-[0-9a-zA-Z\-\.\s\_]+\]', t):
        x = x.replace('[', '').replace(']', '').split(' ')
        parameter_set |= _get_params(x)
        module_set |= _get_modules(x)

    with open('.luigi_completion', 'w') as f:
        f.write('\n'.join(['module:' + x for x in module_set]))
        f.write('\n'.join(['parameter:' + x for x in parameter_set]))
    print('[DONE] update completion')


def main():
    if not len(sys.argv) >= 2 or not sys.argv[1]:
        print('please set file name arg')
        return
    if not os.path.exists(sys.argv[1]):
        print('not found:', sys.argv[1])
        return

    print(f'[RUNNING] python {sys.argv[1]} --help-all')
    help_all = subprocess.run(['python', sys.argv[1], '--help-all'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    _parse_help_all(help_all.stdout.decode("utf8"))
