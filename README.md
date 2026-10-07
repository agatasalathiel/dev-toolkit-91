# dev-toolkit-91

`dev-toolkit-91` is a robust Python-based CLI utility designed to streamline game development workflows and asset management. It provides modular automation for developers looking to bridge the gap between engine prototyping and production-ready code.

### Features
*   **Asset Pipeline Automation:** Automatically optimizes textures and compresses audio files for direct engine integration.
*   **Engine Hook-in:** Rapidly initializes boilerplates for common Python-based frameworks like Pygame and Arcade.
*   **Data Serialization Engine:** Simplifies the translation of JSON/YAML configuration files into typed Python dataclasses for game state management.
*   **Build Validator:** Runs automated sanity checks on directory structures to prevent common deployment failures.

### Installation

Ensure you have Python 3.8+ installed. You can install the toolkit via pip:

```bash
# Clone the repository
git clone https://github.com/Developer/dev-toolkit-91.git
cd dev-toolkit-91

# Install requirements
pip install -r requirements.txt

# Install the package locally
pip install .
```

### Usage

Once installed, use the command-line interface to initialize your project structure or process assets:

```bash
# Initialize a new game project directory
dtk init --name "MyGameProject" --framework pygame

# Batch process asset optimization
dtk assets --input ./raw_assets --output ./dist --quality 85
```

### Roadmap
*   Support for automated unit testing in Pygame environments.
*   Cross-platform build scripts for Windows/macOS exports.
*   Integration with Steamworks SDK wrappers.

---

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.