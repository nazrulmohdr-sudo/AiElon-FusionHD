# AiElon-FusionHD Requirements

## Python Version
Python 3.7 or higher

## Dependencies
This project uses only Python standard library. No external dependencies required.

### Standard Library Modules Used:
- logging - System logging
- typing - Type hints
- enum - Enumeration support
- hashlib - Cryptographic hashing
- time - Time operations
- json - JSON handling
- sys - System-specific parameters
- pathlib - File path operations

## Optional Dependencies (for development)

### Testing
- pytest>=7.0.0 (for unit testing)
- pytest-cov>=4.0.0 (for coverage reports)

### Code Quality
- pylint>=2.15.0 (for code linting)
- black>=22.0.0 (for code formatting)
- mypy>=0.990 (for type checking)

## Installation

### Basic Installation (No dependencies needed)
```bash
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD
python main.py status
```

### Development Installation
```bash
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD

# Install development dependencies (optional)
pip install pytest pytest-cov pylint black mypy
```

## System Requirements

### Minimum:
- CPU: 2 cores
- RAM: 4 GB
- Storage: 100 MB
- OS: Linux, macOS, Windows

### Recommended:
- CPU: 4+ cores
- RAM: 8 GB
- Storage: 1 GB
- OS: Linux (Ubuntu 20.04+), macOS (10.15+), Windows 10+

## Compatibility

- Python 3.7+
- Cross-platform (Linux, macOS, Windows)
- No external service dependencies
- Standalone operation

## Notes

- The system is designed to be dependency-free for maximum portability
- All functionality implemented using Python standard library
- Optional development tools enhance code quality but are not required for operation
