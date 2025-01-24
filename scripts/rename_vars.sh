#!/usr/bin/env bash
#
# rename_r2r_to_fuse.sh
#
# Recursively replaces:
#   - "R2R" -> "FUSE"
#   - "r2r" -> "fuse"
#   - Replaces `/<NAME>/{id}` with `/by-id/{id}` in files named `<NAME>_router.py`
# in file contents and filenames, excluding .git directory.
#
# USAGE:
#   ./rename_r2r_to_fuse.sh <TARGET_DIRECTORY>
#
# EXAMPLE:
#   ./rename_r2r_to_fuse.sh /path/to/your/repo
#
# REQUIRES:
#   - bash
#   - find
#   - sed (GNU sed on Linux, BSD sed on macOS)
#
# NOTE:
#   Back up or commit your repo before running. These changes can't be undone easily!

set -euo pipefail

#######################################
# Print usage information.
#######################################
usage() {
  cat <<EOF
Usage: $0 <TARGET_DIRECTORY>

This script will recursively rename "R2R" -> "FUSE", "r2r" -> "fuse",
and replace "/<NAME>/{id}" with "/by-id/{id}" in <NAME>_router.py files
within <TARGET_DIRECTORY>, excluding .git and specified directories.

Example:
    $0 /path/to/dir
EOF
}

#######################################
# Check for required argument (TARGET_DIR).
#######################################
if [[ $# -ne 1 ]]; then
  usage
  exit 1
fi

TARGET_DIR="$1"

# Make sure the directory exists
if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Error: Directory '$TARGET_DIR' does not exist."
  exit 1
fi

echo "=== Step 1: Replacing 'R2R' -> 'FUSE' and 'r2r' -> 'fuse' in file contents ==="
if [[ "$(uname -s)" == "Darwin" ]]; then
  # macOS (BSD sed requires a backup extension with -i)
  find "$TARGET_DIR" -type f -not -path '*/.git/*' -not -path '*/scripts/*' -not -path '*/docker/*' \
    -not -path '*/__pycache__/*' \
    -exec sed -i '' 's/R2R/FUSE/g; s/r2r/fuse/g' {} +
else
  # Linux (GNU sed typically)
  find "$TARGET_DIR" -type f -not -path '*/.git/*' -not -path '*/scripts/*' -not -path '*/docker/*' \
    -not -path '*/__pycache__/*' \
    -exec sed -i 's/R2R/FUSE/g; s/r2r/fuse/g' {} +
fi

echo

echo "=== Step 2: Conditional renaming of '/<NAME>/{id}' to '/by-id/{id}' in <NAME>_router.py files ==="
# Array of allowed names
NAMES=("chunks" "collections" "conversations" "documents" "graphs" "indices" "logs" "prompts" "retrieval" "users")
for name in "${NAMES[@]}"; do
  find "$TARGET_DIR" -type f -not -path '*/.git/*' -not -path '*/scripts/*' -not -path '*/docker/*' \
    -name "${name}_router.py" \
    -exec bash -c '
      name="$1"
      shift
      for file in "$@"; do
        if [[ "$(uname -s)" == "Darwin" ]]; then
          sed -i "" "s|/${name}/{id}|/by-id/{id}|g" "$file"
        else
          sed -i "s|/${name}/{id}|/by-id/{id}|g" "$file"
        fi
        echo "Updated: $file"
      done
    ' _ "$name" {} +
done

echo
echo "=== Step 3: Renaming filenames containing 'R2R' -> 'FUSE' ==="
find "$TARGET_DIR" -type f -not -path '*/.git/*' -not -path '*/scripts/*' -not -path '*/docker/*' \
  -not -path '*/__pycache__/*' -name "*R2R*" \
  -exec bash -c '
    for f in "$@"; do
      new="${f//R2R/FUSE}"
      echo "Renaming: $f -> $new"
      mv "$f" "$new"
    done
  ' _ {} +

echo
echo "=== Step 4: Renaming filenames containing 'r2r' -> 'fuse' ==="
find "$TARGET_DIR" -type f -not -path '*/.git/*' -not -path '*/scripts/*' -not -path '*/docker/*' \
  -not -path '*/__pycache__/*' -name "*r2r*" \
  -exec bash -c '
    for f in "$@"; do
      new="${f//r2r/fuse}"
      echo "Renaming: $f -> $new"
      mv "$f" "$new"
    done
  ' _ {} +

echo "=== Step 5: Removing '/<NAME>' prefix from router paths in <NAME>_router.py files ==="
for name in "${NAMES[@]}"; do
  find "$TARGET_DIR" -type f -not -path '*/.git/*' -not -path '*/scripts/*' -not -path '*/docker/*' \
    -name "${name}_router.py" \
    -exec bash -c '
      name="$1"
      shift
      for file in "$@"; do
        if [[ "$(uname -s)" == "Darwin" ]]; then
          sed -i "" "s|\"/${name}|\"/|g" "$file"
        else
          sed -i "s|\"/${name}|\"|g" "$file"
        fi
        echo "Updated router paths in: $file"
      done
    ' _ "$name" {} +
done


echo
echo "All done! Please review changes (e.g., 'git diff' if this is a Git repo) to ensure they look correct."
