# cool_gpt

Cool-GPT is a Python library that allows you to use ChatGPT for free using the Selenium framework. 
By utilizing Selenium, you can automate use chatgpt like api, this helps you to generate text and engage in conversations programmatically.
It doesn't require any API keys and it's easy to use and straightforward.
It also doesn't scrape openai or chatgpt website.

## Prerequisites

Before using Cool-GPT, ensure that you have the following prerequisites installed:

- Python 3.6 or above
- Selenium (install via `pip install selenium`)
- element-manager (install via `pip install element-manager`)
- A compatible web driver for Selenium (e.g., ChromeDriver)  [Link](https://chromedriver.chromium.org/downloads)
- Put the web driver in the same folder as the script
- A stable internet connection


## Installation

You can install cool_gpt via pip:

```bash
pip install cool_gpt
```

## Getting Started

To get started, follow these steps:

Here's a basic example of how to use cool_gpt:

```
from cool_gpt import bot

driver = bot.setup_driver()
print('Enter 'q' to quit')
while True:
    message = input('You: ')
    if message == 'q':
        break
    print('Bot:', bot.ask(message, driver))
```


## Limitations

Please note the following limitations of cool_gpt:

cool_gpt is dependent on the availability and reliability of the toolbot.ai interface.

Usage of cool_gpt may be subject to the terms and conditions of the service providing the toolbot.ai interface.

Selenium automation may be slower compared to the OpenAI API, and rate limits may apply depending on the provider and toolbot.ai interface.


## Contributing

Contributions to cool_gpt are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request or open an issue on the GitHub repository.

## License

cool_gpt is licensed under the MIT License. Feel free to use and modify the library according to your needs.

## Acknowledgements

cool_gpt was inspired by the amazing work done by toolbot.ai in developing this amazing website.


## Thank me on-

 - Follow me on Instagram:  [https://www.instagram.com/dipesh_pal17](https://www.instagram.com/dipesh_pal17/)    
        
- Subscribe me on YouTube:  [https://www.youtube.com/dipeshpal17](https://www.youtube.com/dipeshpal17)    