# Deploy pipeline setup for sagarsutaria.com

The workflow at `.github/workflows/deploy.yml` auto-deploys to `quantalynk-new` on every push to `main`.

It needs four GitHub Actions secrets configured in this repo (Settings → Secrets and variables → Actions → New repository secret).

## Required secrets

| Name | Value |
|------|-------|
| `DEPLOY_HOST` | `89.167.40.182` |
| `DEPLOY_USER` | `root` |
| `DEPLOY_PATH` | `/opt/sagarsutaria/public` |
| `DEPLOY_SSH_KEY` | Private key for the deploy account. Paste full contents including BEGIN / END lines. See setup below. |

## One-time SSH key setup

Run on your local Mac (or anywhere with SSH access to `quantalynk-new`):

```bash
# 1. Generate a dedicated deploy key (no passphrase)
ssh-keygen -t ed25519 -C "github-actions-sagarsutaria" \
  -f ~/.ssh/sagarsutaria_deploy -N ""

# 2. Add the public key to quantalynk-new authorized_keys
cat ~/.ssh/sagarsutaria_deploy.pub | ssh quantalynk-new 'cat >> ~/.ssh/authorized_keys'

# 3. Print the PRIVATE key. Paste the full output into the DEPLOY_SSH_KEY GitHub secret.
cat ~/.ssh/sagarsutaria_deploy

# 4. Optional hardening: restrict the new key to deploy commands only.
# On quantalynk-new, edit ~/.ssh/authorized_keys and prefix the new line with:
#   command="rsync --server -lDuvogtprz . /opt/sagarsutaria/public/",no-pty,no-port-forwarding ssh-ed25519 AAAA...
# Restricts the key to the rsync deploy path only. The nginx-reload step
# will then need a second permitted command or a separate key.
# For first launch, the unrestricted key is fine. Tighten later.
```

## What it does on every push to main

1. Checkout the repo
2. Configure SSH with the deploy key
3. Rsync the working tree to `/opt/sagarsutaria/public` with the same exclusions used for manual deploys (.git, .github, node_modules, docs, scripts, package-lock, .gitignore, .DS_Store, CNAME)
4. Run `docker exec sagarsutaria_web nginx -s reload` so the served files refresh without a container restart
5. Verify the site is up by curling `https://sagarsutaria.com` and checking for HTTP 200. Job fails if not 200.

## Triggers

- `push` to `main` (auto)
- `workflow_dispatch` (manual run from the Actions tab)

## Concurrency

Marked as `cancel-in-progress: false` so simultaneous pushes queue rather than cancel each other. Avoids partial-rsync states.

## Troubleshooting

- **First push after setup fails on host-key verification** — the workflow uses `ssh-keyscan` to add the host on the fly. If the server runs on a non-default SSH port, update the `ssh-keyscan` line in the workflow.
- **Permission denied during rsync** — verify the public key is in `/root/.ssh/authorized_keys` on the server and the private key in the secret matches.
- **`docker: command not found`** — the deploy user must be able to run docker. If a non-root deploy user is created later, add them to the `docker` group on the server.
- **Rsync deletes files I wanted to keep** — adjust the `--exclude` list or remove the `--delete` flag. Default is destructive-rsync to keep the served tree exactly matching the repo.
