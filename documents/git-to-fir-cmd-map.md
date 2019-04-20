|git command                           | corresponding fir command              |
|--------------------------------------|----------------------------------------|
| `add <file>`                         | `stage <file>`                         |
| `branch`                             | `branch list --local`                  |
| `branch --unset-upstream`            | `branch untrack`                       |
| `branch -D <branch>`                 | `branch remove -f <branch>`            |
| `branch -a`                          | `branch list`                          |
| `branch -a`                          | `branch`                               |
| `branch -d <branch>`                 | `branch remove <branch>`               |
| `branch -u <remote/branch>`          | `branch track <remote/branch>`         |
| `checkout -b <branch>`               | `branch new <branch>`                  |
| `checkout <branch/tag/commit>`       | `switch <branch/tag/commit>`           |
| `clone <uri>`                        | `repo clone <uri>`                     |
| `commit`                             | `commit`                               |
| `fetch <remote[/branch]>`            | `synch fetch <remote/branch>`          |
| `init`                               | `repo new`                             |
| `merge --ff-only <branch>`           | `follow <branch>`                      |
| `merge --no-ff <branch>`             | `merge <branch>`                       |
| `pull --ff-only <remote/branch>`     | `synch fetch-follow <remote/branch>`   |
| `pull --no-ff <remote/branch>`       | `synch fetch-merge <remote/branch>`    |
| `push <remote/branch>`               | `synch push <remote/branch>`           |
| `push --remove <remote/branch>`      | `branch remove --remote <branch>`      |
| `rebase -i <commit>..<commit>`       | `squash <commit>..<commit>`            |
| `rebase <branch>`                    | `replay --onto <branch>`               |
| `remote -v`                          | `remote list`                          |
| `remote -v`                          | `remote`                               |
| `remote add <name> <uri>`            | `remote new <uri> -n <name>`           |
| `remote rm <remote-name>`            | `remote remove <remote>`               |
| `reset <file[s]>`                    | `unstage <file[s]>`                    |
| `reset --hard HEAD~1`                | `uncommit`                             |
| `reset --hard <commit>`              | `branch revert-to <commit>`            |
| `show <object>`                      | `info <object>`                        |
