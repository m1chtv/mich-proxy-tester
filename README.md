# mich-proxy-tester

## Telegram MTProto Proxy Tester

This script tests the validity and performance of MTProto proxies for Telegram. It reads proxy links from a file, checks their latency, and saves the valid ones to a separate file.

## Features

- **Proxy Parsing:** Extracts server, port, and secret from MTProto proxy links.
- **Performance Testing:** Measures the ping of each proxy.
- **Validation:** Only proxies with a ping time below 250ms are considered valid.
- **Result Saving:** Saves valid proxies to a specified output file.

## Requirements

- Python 3.x
- `requests` module
- `telethon` module

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/telegram-mtproto-proxy-tester.git
cd telegram-mtproto-proxy-tester
```

2. Install the required Python packages:
```bash
pip install -r requests telethon
```

3. Replace `TELEGRAM_API_ID` and `TELEGRAM_API_HASH` in the script with your own Telegram API credentials.

## Usage

1. Create a file named `mich.txt` in the project directory and add your proxy links (one per line) in the following format:
```bash
tg://proxy?server=yourserver&port=yourport&secret=yoursecret
```

2. Run the script:
```bash
python mich.py
```

3. If valid proxies are found, they will be saved to `proxy.txt` in the project directory.

## Example

Example of a proxy link format:
```bash
tg://proxy?server=example.com&port=443&secret=abcdef1234567890abcdef1234567890
```

## Contributing

Feel free to submit issues or pull requests for any improvements or features you'd like to see.
