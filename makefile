# Variables
SCRIPT_NAME = embed.py
TARGET_DIR = /usr/local/bin
REQUIREMENTS = requirements.txt
VENV_DIR = venv

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
	chmod +x $(SCRIPT_NAME)

# Move the script to the target directory
install-script:
	sudo ln -sf $(PWD)/$(SCRIPT_NAME) $(TARGET_DIR)/embed

# Install target
install: install-deps make-executable install-script

# Uninstall target
uninstall:
	sudo rm -f $(TARGET_DIR)/embed

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
	@echo "  make-executable  Make the script executable"
	@echo "  install-script Move the script to $(TARGET_DIR)"
	@echo "  uninstall      Remove the installed script"
	@echo "  clean          Clean up temporary files"
	@echo "  help           Display this help message"

.PHONY: all install install-deps make-executable install-script uninstall clean help create-venv
