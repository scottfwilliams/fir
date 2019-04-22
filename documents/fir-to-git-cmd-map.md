|fir command                             |corresponding git command                           |
|----------------------------------------|--------------------------------------|
| `branch`                               | `branch -a`                          |
| `branch list --local`                  | `branch`                             |
| `branch list`                          | `branch -a`                          |
| `branch new <branch>`                  | `checkout -b <branch>`               |
| `branch remove --remote <branch>`      | `push --remove <remote/branch>`      |
| `branch remove -f <branch>`            | `branch -D <branch>`                 |
| `branch remove <branch>`               | `branch -d <branch>`                 |
| `branch revert-to <commit>`            | `reset --hard <commit>`              |
| `branch track <remote/branch>`         | `branch -u <remote/branch>`          |
| `branch untrack`                       | `branch --unset-upstream`            |
| `commit`                               | `commit`                             |
| `discard`                              | `reset HEAD`           |
| `follow <branch>`                      | `merge --ff-only <branch>`           |
| `info <object>`                        | `show <object>`                      |
| `merge <branch>`                       | `merge --no-ff <branch>`             |
| `remote`                               | `remote -v`                          |
| `remote list`                          | `remote -v`                          |
| `remote new <uri> -n <name>`           | `remote add <name> <uri>`            |
| `remote remove <remote>`               | `remote rm <remote-name>`            |
| `replay --onto <branch>`               | `rebase <branch>`                    |
| `repo clone <uri>`                     | `clone <uri>`                        |
| `repo new`                             | `init`                               |
| `squash <commit>..<commit>`            | `rebase -i <commit>..<commit>`       |
| `stage <file[s]>`                      | `add <file[s]>`                      |
| `switch <branch/tag/commit>`           | `checkout <branch/tag/commit>`       |
| `sync fetch <remote/branch>`          | `fetch <remote[/branch]>`            |
| `sync fetch-follow <remote/branch>`   | `pull --ff-only <remote/branch>`     |
| `sync fetch-merge <remote/branch>`    | `pull --no-ff <remote/branch>`       |
| `sync push <remote/branch>`           | `push <remote/branch>`               |
| `uncommit`                             | `reset --hard HEAD~1`                |
| `unstage <file>`                       | `reset <file>`                       |
