#!/usr/bin/env python

import re
import subprocess
import sys
import asyncio
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define color patterns
patterns = [
    (r'^Failed, modules loaded:', Fore.RED),
    (r'done\.', Fore.GREEN),
    (r'::', Fore.MAGENTA),
    (r'->', Fore.MAGENTA),
    (r'=>', Fore.MAGENTA),
    (r'[+\-/*]', Fore.MAGENTA),
    (r"'\\?.'", Fore.RED),
    (r'"[^"]*"', Fore.RED),
    (r'[{}()]', Fore.BLUE),
    (r'\[\(\)', Fore.BLUE + '[' + Style.RESET_ALL),
    (r'\]', Fore.BLUE),
    (r'^\s*No instance', Fore.RED),
    (r'^<[^>]*>', Fore.RED),
]

def colorize(line):
    for pattern, color in patterns:
        line = re.sub(pattern, color + r'\g<0>' + Style.RESET_ALL, line)
    return line

async def read_stream(stream, callback):
    while True:
        chunk = await stream.read(1024)
        if not chunk:
            break
        callback(chunk.decode('utf-8'))

async def main():
    process = await asyncio.create_subprocess_exec(
        "ghci", *sys.argv[1:],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    await asyncio.gather(
        read_stream(process.stdout, lambda chunk: print(colorize(chunk), end=''))
    )

    await process.wait()

if __name__ == "__main__":
    asyncio.run(main())
