#!/usr/bin/env zsh
# Bridge Codex's stdio MCP transport to RapidAPI without storing credentials in
# the project configuration.
set -eu

script_dir="${0:A:h}"
env_file="${script_dir:h}/.env"

if [[ ! -f "$env_file" ]]; then
  print -u2 "Fresh LinkedIn MCP requires $env_file"
  exit 1
fi

set -a
source "$env_file"
set +a

if [[ -z "${FRESH_LINKEDIN_MCP_KEY:-}" ]]; then
  print -u2 "FRESH_LINKEDIN_MCP_KEY is required in $env_file"
  exit 1
fi

exec npx --yes mcp-remote https://mcp.rapidapi.com \
  --header 'x-api-host:fresh-linkedin-profile-data.p.rapidapi.com' \
  --header 'x-api-key:${FRESH_LINKEDIN_MCP_KEY}'
