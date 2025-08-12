# Callback plugin to log changed tasks (installs/updates)
# Place in project callback_plugins/ and set ANSIBLE_CALLBACK_PLUGINS to this dir.

from __future__ import annotations
from datetime import datetime
import json
import os
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'change_logger'
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self):
        super(CallbackModule, self).__init__()
        self._changes = {}  # host -> list of changes
        self._start_time = datetime.utcnow().isoformat() + 'Z'
        # Output path (env override or default)
        self._out_path = os.environ.get('DOTFILES_CHANGE_LOG', os.path.expanduser('~/.dotfiles.changes.json'))

    def v2_runner_on_ok(self, result, **kwargs):
        try:
            res = result._result or {}
            if res.get('changed'):
                host = result._host.get_name()
                task = result._task
                action = getattr(task, 'action', None) or res.get('_ansible_no_log') and 'no_log' or 'unknown'
                name = getattr(task, 'name', '') or ''
                item = res.get('item')
                change = {
                    'task_name': name,
                    'action': action,
                    'item': item,
                    'changed': True,
                }
                self._changes.setdefault(host, []).append(change)
        except Exception:  # noqa
            # Never fail the run due to callback issues
            pass

    def v2_playbook_on_stats(self, stats):
        try:
            data = {
                'generated_at': datetime.utcnow().isoformat() + 'Z',
                'started_at': self._start_time,
                'hosts': self._changes,
            }
            # Ensure directory exists
            out_dir = os.path.dirname(self._out_path)
            if out_dir and not os.path.isdir(out_dir):
                os.makedirs(out_dir, exist_ok=True)
            with open(self._out_path, 'w') as f:
                json.dump(data, f, indent=2, sort_keys=True)

            # Also print a concise summary to stdout
            total = sum(len(v) for v in self._changes.values())
            if total > 0:
                self._display.display(
                    f"[change_logger] Recorded {total} changed task(s). See {self._out_path}",
                    color='green'
                )
            else:
                self._display.display(
                    f"[change_logger] No changed tasks recorded. See {self._out_path}",
                    color='blue'
                )
        except Exception:  # noqa
            pass
