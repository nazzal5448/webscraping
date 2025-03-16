# Stream Site Scraper

This project is designed to scrape a streaming site and pull details about games that are currently on sale. It uses `playwright` for rendering web pages and `selectolax` for parsing HTML content.

## Features

- Scrapes game details from a streaming site.
- Extracts information about games on sale.
- Outputs data in a structured format.

## Requirements

- Python 3.x
- `playwright`
- `selectolax`
- `requests`

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the necessary browser binaries for `playwright`:

   ```bash
   playwright install
   ```

## Usage

1. Ensure that the configuration file is set up correctly with the URL of the streaming site.

2. Run the main script:

   ```bash
   python main.py
   ```

3. The output will be saved in `outputs/output.json`.

## Configuration

- The configuration settings are managed in the `config` directory. Ensure that the `url` is correctly specified in the configuration file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 