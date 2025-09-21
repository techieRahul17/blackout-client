from setuptools import setup, find_packages

setup(
    name="blackout-client",
    version="0.1.0",
    description="Client blackout screen overlay with Socket.IO and Tkinter",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-username/blackout-client",
    packages=find_packages(),
    install_requires=[
        "python-socketio"
    ],
    entry_points={
        "console_scripts": [
            "blackout-client = blackout_client.client:main"
        ]
    },
    python_requires=">=3.7",
)
