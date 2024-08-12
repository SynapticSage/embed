# Variables
SCRIPT_NAMES = embed.sh aggocluster.sh
TARGET_DIR = /usr/local/bin
REQUIREMENTS = requirements.txt
VENV_DIR = env

# Default target
all: install

# Create virtual environment
create-venv:
	python3 -m venv $(VENV_DIR)

# Install dependencies
install-deps: create-venv
	./$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

# Make the script executable
make-executable:
	chmod +x $(SCRIPT_NAMES)

# Move the scripts to the target directory
install-script:
	for SCRIPT_NAME in $(SCRIPT_NAMES); do \
		sudo ln -sf $(PWD)/$$SCRIPT_NAME $(TARGET_DIR)/$$SCRIPT_NAME; \
	done

# Install target
install: install-deps make-executable install-script

# Uninstall target
uninstall:
	rm -f $(VENV_DIR)
	for SCRIPT_NAME in $(SCRIPT_NAMES); do \
		sudo rm -f $(TARGET_DIR)/$$SCRIPT_NAME; \
	done

# Clean target
clean:
	rm -rf __pycache__ $(VENV_DIR)

# Help target
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all            Default target, runs install"
	@echo "  install        Install dependencies and the script"
	@echo "  create-venv    Create a virtual environment"
	@echo "  install-deps   Install Python dependencies"
	@echo "  make-executable  Make the scripts executable"
	@echo "  install-script Move the scripts to $(TARGET_DIR)"
	@echo "  uninstall      Remove the installed scripts"
	@echo "  clean          Clean up temporary files"
	@echo "  help           Display this help message"

.PHONY: all install install-deps make-executable install-script uninstall clean help create-venv
