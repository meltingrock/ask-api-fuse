#!/bin/bash

# Check if help is requested
if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    echo "Usage: $0 [--backup] <path>"
    echo "  --backup    Create backup files before modifying"
    echo "  path       File or directory to process"
    echo ""
    echo "Examples:"
    echo "  $0 myfile.py              # Process single file"
    echo "  $0 --backup myfile.py     # Process single file with backup"
    echo "  $0 /path/to/dir           # Process all Python files in directory"
    echo "  $0 --backup /path/to/dir  # Process directory with backups"
    exit 0
fi

# Parse arguments
BACKUP=false
PATH_TO_PROCESS=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --backup)
            BACKUP=true
            shift
            ;;
        *)
            PATH_TO_PROCESS="$1"
            shift
            ;;
    esac
done

# Check if path is provided
if [ -z "$PATH_TO_PROCESS" ]; then
    echo "Error: No path specified"
    echo "Use --help for usage information"
    exit 1
fi

# Verify path exists
if [ ! -e "$PATH_TO_PROCESS" ]; then
    echo "Error: Path '$PATH_TO_PROCESS' not found"
    exit 1
fi

# Create a Python script to do the replacement
cat > remove_openapi.py << 'EOF'
import sys
import shutil
import re

def remove_openapi_extra(content):
    pattern = r',\s*openapi_extra=\{[^{]*"x-codeSamples":\s*\[[^]]*\]\s*\}'
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    return new_content

def process_file(filepath, create_backup=False):
    try:
        # Check if file is a Python file
        if not filepath.endswith('.py'):
            return

        if create_backup:
            shutil.copy2(filepath, filepath + '.bak')

        with open(filepath, 'r') as f:
            content = f.read()

        new_content = remove_openapi_extra(content)

        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Modified: {filepath}")
        else:
            print(f"No changes needed: {filepath}")

    except Exception as e:
        print(f"Error processing {filepath}: {e}", file=sys.stderr)

if __name__ == "__main__":
    create_backup = len(sys.argv) > 2 and sys.argv[2] == '--backup'
    process_file(sys.argv[1], create_backup)
EOF

# Make the Python script executable
chmod +x remove_openapi.py

# Process based on whether it's a file or directory
if [ -f "$PATH_TO_PROCESS" ]; then
    echo "Processing file: $PATH_TO_PROCESS"
    if [ "$BACKUP" = true ]; then
        python3 remove_openapi.py "$PATH_TO_PROCESS" --backup
    else
        python3 remove_openapi.py "$PATH_TO_PROCESS"
    fi
elif [ -d "$PATH_TO_PROCESS" ]; then
    echo "Processing directory: $PATH_TO_PROCESS"
    if [ "$BACKUP" = true ]; then
        find "$PATH_TO_PROCESS" -type f -name "*.py" -exec python3 remove_openapi.py {} --backup \;
    else
        find "$PATH_TO_PROCESS" -type f -name "*.py" -exec python3 remove_openapi.py {} \;
    fi
fi

# Clean up the temporary Python script
rm remove_openapi.py