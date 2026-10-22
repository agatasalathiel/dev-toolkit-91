[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# dev-toolkit-91

`dev-toolkit-91` is a high-performance Python library designed to streamline asset pipelines and engine telemetry for 2D game development. It simplifies texture atlas generation, parses TMX tilemaps into memory-efficient structures, and provides real-time frame budget monitoring for Pygame and Arcade applications.

## Features

* **Automated Sprite Slicing:** Extracts individual animation frames from single RGBA sprite sheets with dynamic padding detection.
* **Fast TMX Map Loader:** Converts Tiled XML map exports into optimized NumPy collision arrays for rapid raycasting and spatial partitioning.
* **Frame Budget Telemetry:** Measures function-level render bottleneck metrics with low-overhead profiling decorators.
* **Texture Atlas Packer:** Combines loose PNG assets into packed spritesheet textures with coordinate JSON mapping to minimize GPU draw calls.

## Installation

Install the package via pip:

```bash
pip install dev-toolkit-91
```

For source builds and developer dependencies:

```bash
git clone https://github.com/Developer/dev-toolkit-91.git
cd dev-toolkit-91
pip install -e .[dev]
```

## Quick Start

```python
from dev_toolkit_91 import AtlasPacker, FrameTracker

# Track render pipeline performance
tracker = FrameTracker(target_fps=60)

@tracker.profile
def render_frame():
    # Slices hero animation frames from atlas
    packer = AtlasPacker(source_dir="./raw_assets")
    atlas = packer.build(output_file="spritesheet.png")
    frames = atlas.get_animation("hero_run")
    return len(frames)

if __name__ == "__main__":
    frame_count = render_frame()
    print(f"Loaded {frame_count} frames. Avg Frame Time: {tracker.avg_ms:.2f}ms")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.