#!/bin/bash

# Step 1: Download and install Scarb
curl --proto '=https' --tlsv1.2 -sSf https://docs.swmansion.com/scarb/install.sh | sh

# Step 2: Restart the terminal

# Step 3: Verify the installation
bash -c "scarb --version"